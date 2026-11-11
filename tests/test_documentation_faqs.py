"""Checks that page-specific FAQs survive codebase documentation regeneration."""
import json
from pathlib import Path
import tempfile
import unittest

from scripts.docgen.markdown_generator import MarkdownGenerator

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / 'website' / 'docs'


class DocumentationFAQTests(unittest.TestCase):
    def test_every_page_has_a_faq_and_example(self):
        for page in DOCS.rglob('*.md'):
            with self.subTest(page=page):
                text = page.read_text(encoding='utf-8')
                self.assertIn('## FAQ\n', text)
                faq = text.split('## FAQ\n', 1)[1].split('\n## ', 1)[0]
                self.assertIn('### ', faq)
                self.assertIn('```bash\n', faq)

    def test_generated_faqs_are_inserted_in_custom_output(self):
        faqs = json.loads((ROOT / 'scripts/docgen/page_faqs.json').read_text(encoding='utf-8'))
        pages = {p.name for p in (DOCS / 'codebase').glob('*.md')}
        self.assertEqual(set(faqs), pages)
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            for name in faqs:
                (output / name).write_text('# Title\n\nIntro.\n\n## Reference\n', encoding='utf-8')
            MarkdownGenerator(output_dir=directory)._add_page_faqs()
            for name, faq in faqs.items():
                with self.subTest(page=name):
                    self.assertIn(faq, (output / name).read_text(encoding='utf-8'))
                    self.assertIn(faq, (DOCS / 'codebase' / name).read_text(encoding='utf-8'))


if __name__ == '__main__':
    unittest.main()
