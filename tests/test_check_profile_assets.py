"""Casos sintéticos para as verificações do README público."""
import tempfile
import unittest
from pathlib import Path

from scripts.check_profile_assets import check_profile

PNG_1PX = (b'\x89PNG\r\n\x1a\n' + b'\x00\x00\x00\rIHDR' +
           b'\x00\x00\x00\x01\x00\x00\x00\x01' + b'\x08\x02\x00\x00\x00')


class ProfileValidationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / 'assets').mkdir()

    def tearDown(self):
        self.tmp.cleanup()

    def test_local_images_and_anchor_pass(self):
        (self.root / 'assets' / 'hero.png').write_bytes(PNG_1PX)
        (self.root / 'README.md').write_text(
            '![Capa](assets/hero.png?size=large)\n[Seção](#secao)\n', encoding='utf-8')
        self.assertEqual(check_profile(self.root), [])

    def test_missing_file_is_reported(self):
        (self.root / 'README.md').write_text('![Capa](assets/inexistente.png)', encoding='utf-8')
        self.assertTrue(any('inexistente' in e for e in check_profile(self.root)))

    def test_html_image_requires_alt(self):
        (self.root / 'assets' / 'hero.png').write_bytes(PNG_1PX)
        (self.root / 'README.md').write_text('<img src="assets/hero.png">', encoding='utf-8')
        self.assertTrue(any('texto alternativo' in e for e in check_profile(self.root)))

    def test_svg_invalid_is_reported(self):
        (self.root / 'assets' / 'broken.svg').write_text('<svg>', encoding='utf-8')
        (self.root / 'README.md').write_text('# Olá', encoding='utf-8')
        self.assertTrue(any('SVG inválido' in e for e in check_profile(self.root)))

    def test_fenced_code_not_interpreted_as_reference(self):
        (self.root / 'README.md').write_text('```md\n![X](missing.png)\n```\n', encoding='utf-8')
        self.assertEqual(check_profile(self.root), [])

    def test_reference_must_stay_inside_repository(self):
        (self.root / 'README.md').write_text('[Arquivo](../outside.txt)', encoding='utf-8')
        self.assertTrue(any('fora do repositório' in e for e in check_profile(self.root)))


if __name__ == '__main__':
    unittest.main()
