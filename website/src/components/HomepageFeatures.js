import React from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import styles from './HomepageFeatures.module.css';

const FeatureList = [
  {
    title: 'The Engine Core',
    svg: (
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" className={styles.featureIcon}>
        <path d="M12 2L3 7v10l9 5 9-5V7l-9-5z" strokeLinejoin="round" />
        <path d="M3 7l9 5 9-5M12 12v10" strokeLinejoin="round" />
      </svg>
    ),
    description: (
      <>
        The <code>App</code>, <code>Base</code> and <code>Network</code> projects implement the
        Roblox engine: the Instance tree, DataModel, Lua 5.1 scripting, physics and replication.
      </>
    ),
    links: [
      { label: 'Architecture overview →', href: '/docs/architecture/' },
      { label: 'App module →', href: '/docs/modules/app' },
    ],
  },
  {
    title: 'Studio & Clients',
    svg: (
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" className={styles.featureIcon}>
        <rect x="2" y="4" width="20" height="14" rx="2" />
        <path d="M8 21h8M12 18v3M7 9h4M7 12h7" strokeLinecap="round" />
      </svg>
    ),
    description: (
      <>
        A Qt&nbsp;4.8 based <code>RobloxStudio</code> IDE, plus native clients for Windows, Xbox,
        iOS and Android — all documented module by module.
      </>
    ),
    links: [
      { label: 'RobloxStudio module →', href: '/docs/modules/studio' },
      { label: 'Client platforms →', href: '/docs/modules/clients' },
    ],
  },
  {
    title: 'Build System',
    svg: (
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" className={styles.featureIcon}>
        <path d="M4 17l6-6-6-6M12 19h8" strokeLinecap="round" strokeLinejoin="round" />
      </svg>
    ),
    description: (
      <>
        Visual Studio solutions, CMake for Unix/Android, bundled Boost &amp; Qt builds, custom
        MSBuild rules and property sheets — everything needed to get a compiling tree.
      </>
    ),
    links: [
      { label: 'Building on Windows →', href: '/docs/getting-started/building-windows' },
      { label: 'CMake builds →', href: '/docs/getting-started/building-cmake' },
    ],
  },
  {
    title: 'Testing & Tooling',
    svg: (
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" className={styles.featureIcon}>
        <path d="M9 3h6M10 3v5L4.5 18a2 2 0 001.8 3h11.4a2 2 0 001.8-3L14 8V3" strokeLinejoin="round" />
        <path d="M7 15h10" />
      </svg>
    ),
    description: (
      <>
        Unit test suites, the <code>RobloxTest</code> physics/API harnesses, script signing tools,
        analyzers and the security-focused GitHub Actions pipelines.
      </>
    ),
    links: [
      { label: 'Testing →', href: '/docs/modules/testing' },
      { label: 'Tooling & plugins →', href: '/docs/modules/tooling' },
    ],
  },
];

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((feature, idx) => (
            <div key={idx} className={clsx('col col--3')}>
              <div className="text--center padding--md">{feature.svg}</div>
              <div className="text--center padding-horiz--md">
                <h3>{feature.title}</h3>
                <p>{feature.description}</p>
                <p>
                  {feature.links.map((link, i) => (
                    <span key={i}>
                      <Link to={link.href}>{link.label}</Link>
                      {i < feature.links.length - 1 ? <br /> : null}
                    </span>
                  ))}
                </p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
