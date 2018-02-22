"""Script that outputs information about the current versions of python"""
from platform import python_version
import os
import sys
import json
import yaml

data = ['version', 'name (alias) or virtual environment', 'python executable location',
        'pip location', 'PYTHONPATH', 'installed packages', 'site-packages location']

site_packages = next(p for p in sys.path if 'site-packages' in p)

output = [python_version(), os.popen('pyenv version-name').read().strip(), sys.executable,
          os.popen('which pip').read().strip(), sys.exec_prefix,
          os.popen('pip freeze').read().strip().split('\n'),
          site_packages]

structured_output = dict(zip(data, output))

with open('data.json', 'w') as outfile:
    outfile.write(json.dumps(structured_output, indent=4,
                             sort_keys=True, separators=(',', ': '), ensure_ascii=False))
    outfile.close()

with open('data.yaml', 'w') as outfile:
    outfile.write(yaml.dump(structured_output, allow_unicode=True))
outfile.close()
