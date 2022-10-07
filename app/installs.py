import sys
import subprocess

packages = ['discord', 'requests', 'pywebio']

# implement pip as a subprocess:
for i in packages:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', i])

# process output with an API in the subprocess module:
reqs = subprocess.check_output([sys.executable, '-m', 'pip',
'freeze'])
installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

for i in installed_packages:
    print(f"{i} has been installed.")