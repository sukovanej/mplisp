"""import special form

Exmaples:
(import std.io.petr)
"""
from typing import List
import importlib
import importlib.util
import inspect


def import_module(args: List, node):
    """
    Import all functions from a module and add corresponding symbols
    to the parent enviroment.
    """
    module_name = args[0].value
    mplispstd = module_name.replace("std", "mplispstd")

    if module_exists(mplispstd):
        module_name = mplispstd

    mod = importlib.import_module(module_name)
    functions = load_module_functions(mod)
    node.parent.local_env.symbols.update(functions)

    return None


def load_module_functions(module):
    """Get all module functions"""
    return inspect.getmembers(module, inspect.isfunction)


def module_exists(module_name):
    """Does module exists"""
    return importlib.util.find_spec(module_name) is not None
