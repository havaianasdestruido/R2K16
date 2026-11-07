import json
from pathlib import Path
import subprocess
import tempfile
import unittest

from generate_reference import generate


class ReferenceTest(unittest.TestCase):
    def test_definitions_test_calls_variants_and_stale_cleanup(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            subprocess.run(['git', 'init', '-q', str(root)], check=True)
            subprocess.run(['git', '-C', str(root), 'config', 'user.email', 'test@example.com'], check=True)
            subprocess.run(['git', '-C', str(root), 'config', 'user.name', 'Test'], check=True)
            (root / 'src').mkdir()
            (root / 'tests').mkdir()
            (root / 'src/a.py').write_text('def calculate(x):\n    return helper(x)\n')
            (root / 'src/b.py').write_text('def calculate(x):\n    return x + 1\n')
            (root / 'tests/test_a.py').write_text('def test_calculate():\n    assert calculate(1) == 2\n')
            (root / 'ignored.py').write_text('def hidden():\n    pass\n')
            subprocess.run(['git', '-C', str(root), 'add', 'src', 'tests'], check=True)
            subprocess.run(['git', '-C', str(root), 'commit', '-qm', 'fixture'], check=True)
            out = root / 'output'
            generate(root, out)
            manifest = json.loads((out / 'manifest.json').read_text())
            self.assertEqual(manifest['counts']['functions'], 3)
            import hashlib
            key = hashlib.sha256(b'calculate').hexdigest()[:2]
            match = json.loads((out / 'names' / (key + '.json')).read_text())['calculate']
            self.assertEqual(len(match['definitions']), 2)
            self.assertNotEqual(match['definitions'][0][2], match['definitions'][1][2])
            self.assertEqual(match['tests'], [['tests/test_a.py', 2, 'test_calculate', 'assert calculate(1) == 2']])
            group = next(x for x in manifest['groups'] if x['name'] == 'src')
            defs = json.loads((out / 'groups' / (group['key'] + '.json')).read_text())
            self.assertIn('helper', defs[0]['calls'])
            (out / 'groups/stale.json').write_text('{}')
            generate(root, out)
            self.assertFalse((out / 'groups/stale.json').exists())

if __name__ == '__main__':
    unittest.main()
