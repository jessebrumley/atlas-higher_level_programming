#!/usr/bin/python3
import importlib

def discover_names(module_name):
   module = importlib.import_module(module_name)
   for name in dir(module):
       if not name.startswith("__"):
           print(name)

if __name__ == "__main__":
   module_name = 'hidden_4'
   discover_names(module_name)
