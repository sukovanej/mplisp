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
    functions = load_module_functions(mod)
    node.parent.local_env.symbols.update(functions)

    return None


def load_module_functions(module):
    return inspect.getmembers(module, inspect.isfunction)


def module_exists(module_name):
    return importlib.util.find_spec(module_name) is not None