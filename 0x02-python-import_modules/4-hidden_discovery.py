#!/usr/bin/python3
import importlib

def print_module_names(module):
    names = [name for name in dir(module) if not name.startswith('__')]
    for name in sorted(names):
        print(name)

if __name__ == "__main__":
    module_name = 'hidden_4'  # Replace with the name of the module without the .py or .pyc extension
    module = importlib.import_module(module_name)
    print_module_names(module)
