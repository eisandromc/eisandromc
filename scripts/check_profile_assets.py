#!/usr/bin/env python3
"""Verifica caminhos locais, acessibilidade básica de imagens e arquivos gráficos.

Não testa URLs externas, renderização Markdown, performance nem código de projetos.
"""
from __future__ import annotations

import re
import struct
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

MARKDOWN_LINK = re.compile(r'(!?)\[([^\]\n]*)\]\(([^)\n]+)\)')
FENCE = re.compile(r'^\s*(```|~~~)')
PNG_SIGNATURE = b'\x89PNG\r\n\x1a\n'


class ImageCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.images: list[tuple[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() == 'img':
            props = dict(attrs)
            self.images.append((props.get('src') or '', props.get('alt') or ''))


def local_path(root: Path, raw: str) -> tuple[Path | None, str | None]:
    """Resolve referência local; ignora links externos e fragmentos internos."""
    value = raw.strip().strip('<>')
    if not value or value.startswith('#'):
        return None, None
    value = value.split()[0]  # Desconsidera o título opcional em Markdown.
    parts = urlsplit(value)
    if parts.scheme or parts.netloc or value.startswith('//'):
        return None, None
    if parts.path.startswith('/'):
        return None, f'Caminho absoluto não portável: {value}'
    path = (root / unquote(parts.path)).resolve()
    if not path.is_relative_to(root.resolve()):
        return None, f'Caminho fora do repositório: {value}'
    return path, None


def check_profile(root: Path) -> list[str]:
    errors: list[str] = []
    readme = root / 'README.md'
    if not readme.is_file():
        return ['README.md ausente']

    # Não analisar trechos de código fenced como se fossem links do documento.
    content: list[str] = []
    in_fence = False
    fence_kind = ''
    for line in readme.read_text(encoding='utf-8').splitlines():
        mark = FENCE.match(line)
        if mark:
            if not in_fence:
                in_fence, fence_kind = True, mark.group(1)[:3]
            elif mark.group(1)[:3] == fence_kind:
                in_fence = False
            continue
        if not in_fence:
            content.append(line)
    text = '\n'.join(content)
    html = ImageCollector()
    html.feed(text)

    references: list[tuple[str, bool, str]] = []
    for src, alt in html.images:
        references.append((src, True, alt))
    for m in MARKDOWN_LINK.finditer(text):
        references.append((m.group(3), m.group(1) == '!', m.group(2)))

    for ref, image, alt in references:
        if image and not alt.strip():
            errors.append(f'Imagem sem texto alternativo: {ref}')
        path, reason = local_path(root, ref)
        if reason:
            errors.append(reason)
        elif path and not path.is_file():
            errors.append(f'Referência local inexistente: {ref}')

    images = root / 'assets'
    if images.exists():
        for svg in images.rglob('*.svg'):
            try:
                ET.parse(svg)
            except ET.ParseError as exc:
                errors.append(f'SVG inválido ({svg.relative_to(root)}): {exc}')
        for png in images.rglob('*.png'):
            with png.open('rb') as stream:
                header = stream.read(24)
            if len(header) < 24 or not header.startswith(PNG_SIGNATURE) or header[12:16] != b'IHDR':
                errors.append(f'PNG inválido: {png.relative_to(root)}')
            else:
                width, height = struct.unpack('>II', header[16:24])
                if not width or not height:
                    errors.append(f'Dimensões PNG inválidas: {png.relative_to(root)}')
    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors = check_profile(root)
    if errors:
        for error in errors:
            print(f'ERRO: {error}', file=sys.stderr)
        return 1
    print('OK: referências locais, alt de imagens e SVG/PNG verificados.')
    print('Limites: links externos e renderização oficial do GitHub não foram testados.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
