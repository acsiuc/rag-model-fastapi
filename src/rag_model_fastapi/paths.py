from pathlib import Path

root_path = Path(__file__).parents[2]
data_path = root_path / Path('data')
documentation_path = data_path / Path('docs/en/docs')
code_documentation_path = data_path / Path('docs_src')
eval_path = root_path / Path('evaluation') / Path('evaluation.json')