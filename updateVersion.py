# update the version with the latest git commit
import subprocess
git_commit = subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD'], text=True)
new_version = '1.0-' + git_commit.strip()
print('Building with new version number', new_version)
with open('_version.py', 'w') as f:
    f.write('version = "' + new_version + '"')