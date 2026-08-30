import re

from rag_model_fastapi.paths import data_path


def resolve_code_markers(text):

    """Replace {* path.py *} markers with the actual code from docs_src."""

    pattern = r'\{\*\s*(.+?\.py).*?\*\}'

    def replace_one(match):
        raw_path = match.group(1)
        cleaned_path = 'docs_src/' + raw_path.split('docs_src/')[-1]
        full_path = data_path / cleaned_path

        try:
            code = full_path.read_text()
            return  f"```python\n{code}\n```"
        except FileNotFoundError:
            return match.group(0)

        

    return re.sub(pattern, replace_one, text)

def strip_anchor_ids(text):

    pattern = r'\{\s*#.+?\s*\}'

    return re.sub(pattern, '', text)

def strip_note_blocks(text):

    pattern = r'///[^\n]*\n(.*?)///'

    return re.sub(pattern, r'\1', text, flags=re.DOTALL)

def load_file(path):

    with open(path, 'r') as f:
        markdown_file = f.read()
        file_without_anchors = strip_anchor_ids(markdown_file)
        file_without_note_blocks = strip_note_blocks(file_without_anchors)
        clean_file_with_code = resolve_code_markers(file_without_note_blocks)

    return {'path': path, 'text': clean_file_with_code}



def load_all_files(path):
    list_of_paths_text = []
    for file in path.rglob('*.md'):
        path_text_dict = load_file(file)
        list_of_paths_text.append(path_text_dict)

    return list_of_paths_text

