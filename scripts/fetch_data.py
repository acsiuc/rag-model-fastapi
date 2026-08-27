import subprocess
from pathlib import Path

root_path = Path(__file__).parent.parent
documentation_path = root_path / Path('data/docs/en/docs')
code_documentation_path = root_path / Path('data/docs_src')

if documentation_path.is_dir() and code_documentation_path.is_dir():
    print("The repository has already been cloned and fetched.")
else:

    subprocess.run(['git', 'clone', '--depth', '1', '--filter=blob:none', '--sparse', 'https://github.com/fastapi/fastapi.git', 
                    str(root_path / 'data')], check = True)
    subprocess.run(['git', 'sparse-checkout', 'set', 'docs/en/docs', 'docs_src'], cwd = root_path / Path('data'), check = True)