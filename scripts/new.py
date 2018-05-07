#!/usr/bin/env python
import os
import sys

# TODO: Consider http://python-packaging.readthedocs.io/en/latest/command-line-scripts.html#the-scripts-keyword-argument
# for packaging.

# Ensure running in root directory
working_dir = os.getcwd()
print(working_dir)
if(working_dir.endswith('lib')):
    print("Run script from project root.")
    quit()

# Ensure arguments
if(len(sys.argv) == 1):
    print(
        "Must provide filename prefaced with three digits w/o extension (e.g. 005_halting_problem)")
    quit()

# Create files
file_name = sys.argv[1]

if(file_name.endswith('.py')):
    file_name = file_name[0:-3]  # Handle with or without extension

with open(f'{working_dir}/src/{file_name}.py', 'w') as file:
    file.write('')  # blank is fine for now

# TODO: Use templating? https://docs.python.org/3.4/library/string.html#template-strings
# This is fine for now.
test_lines = [
    'import importlib\n',
    f'solution = importlib.import_module(\'src.{file_name}\')'
]

with open(f'{working_dir}/tests/test_{file_name}.py', 'w') as file:
    file.write(test_lines[0])
    file.write(test_lines[1])
