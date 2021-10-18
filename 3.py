import os
import shutil

cwd = 'my_project/'
new_cwd = 'my_project/templates'
print(os.getcwd())

for root, dirs, files in os.walk(cwd):
    for dir in dirs:
        old_path = os.path.join(root, dir)
        if old_path.endswith('templates'):
            try:
                shutil.copytree(old_path, new_cwd)
            except FileExistsError:
                new_cwd += '1'
                shutil.copytree(old_path, new_cwd)
