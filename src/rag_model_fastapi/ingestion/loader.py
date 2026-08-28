import re
from pathlib import Path

from rag_model_fastapi.paths import (
    code_documentation_path,
    data_path,
    documentation_path,
    root_path,
)


def resolve_code_markers(text):

    """Replace {* path.py *} markers with the actual code from docs_src."""

    pattern = r'\{\*\s*(.+?\.py)(?:\s+hl\[.*?\])?\s*\*\}'

    def replace_one(match):
        raw_path = match.group(1)
        cleaned_path = 'docs_src/' + raw_path.split('docs_src/')[-1]
        full_path = data_path / cleaned_path

        code = full_path.read_text()
        return  f"```python\n{code}\n```"

    return re.sub(pattern, replace_one, text)

def strip_anchor_ids(text):

    pattern = r'\{\s*#.+?\s*\}'

    return re.sub(pattern, '', text)

def strip_note_blocks(text):

    pattern = r'///[^\n]*\n(.*?)///'

    return re.sub(pattern, r'\1', text, flags=re.DOTALL)