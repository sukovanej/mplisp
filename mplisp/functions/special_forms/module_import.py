from typing import List
import importlib
import importlib.util
import inspect


def import_module(args: List, node):
    module_name = args[0].value
    mplispstd =  module_name.replace("std", "mplispstd")

    if module_exists(mplispstd):
        module_name = mplispstd

    mod = importlib.import_module(module_name)
    print(load_module_functions(mod))

    return module_name


def load_module_functions(module):
    return inspect.getmembers(module, inspect.isfunction)


def load(module):
    modules = filter(lambda i: isinstance(i, 'module'), [getattr(module, j)\
        for j in dir(module)])

    result = []

    for mod in modules:
        if isinstance(mod, 'function'):
            result.append(mod)
        elif isinstance(mod, 'module'):
            result.extend(load(mod))
    
    return result


def module_exists(module_name):
    return importlib.util.find_spec(module_name) is not None