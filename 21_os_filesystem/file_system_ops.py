import os
import shutil
import glob

current_dir = os.getcwd()
print(f"Current directory: {current_dir}")

files = os.listdir('.')
print(f"Files in current directory: {files}")

for file in files:
    if os.path.isfile(file):
        print(f"File: {file}")
    elif os.path.isdir(file):
        print(f"Directory: {file}")

os.makedirs('temp_folder/subfolder', exist_ok=True)

with open('temp_folder/test.txt', 'w') as f:
    f.write("Test file content")

shutil.copy('temp_folder/test.txt', 'temp_folder/test_copy.txt')

python_files = glob.glob('*.py')
print(f"Python files: {python_files}")

for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.py'):
            print(os.path.join(root, file))

if os.path.exists('temp_folder'):
    shutil.rmtree('temp_folder')
