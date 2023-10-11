import importlib
import pkgutil
import random as real_random
import sys


installed_modules = pkgutil.iter_modules()

rand_mod_name = real_random.choice(list(installed_modules))

rand_mod = importlib.import_module(rand_mod_name.name)

print(f"Importing {rand_mod.__name__} as random")

if hasattr(rand_mod, '__all__'):
    submodules = rand_mod.__all__
else:
    submodules = list(vars(rand_mod).keys())


for submod in submodules:
    exec(f"{submod} = rand_mod.{submod}")