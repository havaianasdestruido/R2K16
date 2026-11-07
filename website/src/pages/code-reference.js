import React, {useEffect, useState} from 'react';
import Layout from '@theme/Layout';
import useBaseUrl from '@docusaurus/useBaseUrl';

const repo = 'https://github.com/havaianasdestruido/R2K16/blob/';
function sourceUrl(revision, path, line, end) {
  return repo + revision + '/' + path.split('/').map(encodeURIComponent).join('/') + '#L' + line + (end && end !== line ? '-L' + end : '');
}
async function getJson(url) {
  const response = await fetch(url);
  if (!response.ok) throw new Error(`Could not load ${url} (${response.status}). Generate the reference before building.`);
  return response.json();
}
async function nameBucket(name) {
  const digest = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(name));
  return Array.from(new Uint8Array(digest)).map(x => x.toString(16).padStart(2, '0')).join('').slice(0, 2);
}
function Location({revision, location}) {
  return <a href={sourceUrl(revision, location[0], location[1])}>{location[0]}:{location[1]}</a>;
}
function Detail({item, manifest, base}) {
  const [data, setData] = useState(null);
  const [error, setError] = useState('');
  useEffect(() => {
    let active = true;
    setData(null); setError('');
    nameBucket(item.name).then(key => getJson(`${base}names/${key}.json`))
      .then(result => {if (active) setData(result[item.name]);})
      .catch(e => {if (active) setError(e.message);});
    return () => {active = false;};
  }, [item, base]);
  return <section>
    <h2>{item.name}</h2>
    <p><a href={sourceUrl(manifest.revision, item.path, item.line, item.end)}>{item.path}:{item.line}–{item.end}</a></p>
    <pre><code>{item.signature}</code></pre>
    <p><strong>Body structure:</strong> {item.controls.length ? item.controls.join(', ') : 'No recognized control-flow statements.'}</p>
    <p><strong>Calls found in body:</strong> {item.calls.length ? item.calls.join(', ') : 'None recognized.'} (up to 30 distinct names)</p>
    <p>Read the linked body for the implementation and its context. These structural hints are not a semantic explanation.</p>
    {error && <p role="alert">{error}</p>}
    {!data && !error && <p>Loading name matches…</p>}
    {data && <>
      <h3>Potential test uses ({data.tests.length})</h3>
      <p>Calls with the same spelling in test-like paths, not verified call targets or coverage.</p>
      <ul>{data.tests.slice(0, 100).map((loc, i) => <li key={i}><Location revision={manifest.revision} location={loc}/> {loc[2] && <>in <code>{loc[2]}</code></>} {loc[3] && <pre><code>{loc[3]}</code></pre>}</li>)}</ul>
      {data.tests.length > 100 && <p>Showing first 100.</p>}
      <h3>Same-named definitions ({data.definitions.length})</h3>
      <p>Same names may be unrelated overloads or types. “Different” means normalized body text differs, not necessarily behavior; identical text can behave differently in context.</p>
      <ul>{data.definitions.slice(0, 100).map((loc, i) => <li key={i}><Location revision={manifest.revision} location={loc}/> — {loc[2] === item.hash ? 'same body text' : 'different body text'}</li>)}</ul>
      {data.definitions.length > 100 && <p>Showing first 100.</p>}
    </>}
  </section>;
}
export default function CodeReference() {
  const base = useBaseUrl('/generated/');
  const [manifest, setManifest] = useState(null);
  const [group, setGroup] = useState('');
  const [items, setItems] = useState([]);
  const [query, setQuery] = useState('');
  const [selected, setSelected] = useState(null);
  const [error, setError] = useState('');
  useEffect(() => { getJson(base + 'manifest.json').then(setManifest).catch(e => setError(e.message)); }, [base]);
  useEffect(() => {
    let active = true;
    setItems([]); setSelected(null);
    if (group) getJson(`${base}groups/${group}.json`).then(data => {if (active) setItems(data);}).catch(e => {if (active) setError(e.message);});
    return () => {active = false;};
  }, [group, base]);
  const matches = items.filter(x => (x.name + ' ' + x.path).toLowerCase().includes(query.toLowerCase()));
  return <Layout title="Generated code reference" description="Source definitions and potential test references"><main className="container margin-vert--lg">
    <h1>Generated code reference</h1>
    <p>Browse syntax-extracted definitions, source links, possible test calls and same-name body comparisons. <a href={useBaseUrl('/reference/generated-reference')}>Methodology and limitations</a>.</p>
    {error && <p role="alert">{error}</p>}
    {manifest && <>
      <p>Revision <code>{manifest.revision.slice(0, 12)}</code> · {manifest.counts.files.toLocaleString()} files · {manifest.counts.functions.toLocaleString()} definitions · {manifest.counts.test_calls.toLocaleString()} potential test calls</p>
      <label>Source group <select value={group} onChange={e => {setGroup(e.target.value); setError('');}}><option value="">Choose a group</option>{manifest.groups.map(g => <option key={g.key} value={g.key}>{g.name} ({g.count})</option>)}</select></label>
      {group && <><p><label>Filter by name or path <input value={query} onChange={e => setQuery(e.target.value)} /></label></p>
        <p>{matches.length.toLocaleString()} matches; showing first 200. Refine the filter to find more.</p>
        <ul>{matches.slice(0, 200).map((x, i) => <li key={i}><button type="button" onClick={() => setSelected(x)}>{x.name}</button> <small>{x.path}:{x.line}</small></li>)}</ul></>}
      {selected && <Detail item={selected} manifest={manifest} base={base}/>}
    </>}
  </main></Layout>;
}
