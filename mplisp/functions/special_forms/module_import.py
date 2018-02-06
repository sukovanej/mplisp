"""import special form

Exmaples:
(import std.io.petr)
"""
from types import ModuleType
from typing import List
import importlib
import importlib.util
import inspect
from mplisp import evaluator


def import_module(args: List, node):
    """
    Import all functions from a module and add corresponding symbols
    to the parent environment.
    """
    module_name = evaluator.evaluate_node(args[0])

    if not isinstance(module_name, str):
        evaluator.error("1st param must be of type str")

    mplispstd = module_name.replace("std", "mplispstd")

    if module_exists(mplispstd):
        module_name = mplispstd
    elif not module_exists(module_name):
        evaluator.error("package {} not found".format(module_name))

    mod = importlib.import_module(module_name)

    functions = {name.replace("_", "-"): func for name, func in load_module_functions(mod)}
    inst = node.parent

    while inst.local_env is None:
        inst = inst.parent

    inst.local_env.symbols.update(functions)

    return mod


def python_getattr(args: List, node):
    """Call python function from mplisp"""
    if len(args) != 2:
        evaluator.error("2 parameters expected, {} given".format(len(args)))

    params = evaluator.evaluate_parallel_args(args)

    if not isinstance(params[0], ModuleType):
        params[0] = import_module(args[0:1], node)

    if not isinstance(params[1], str):
        evaluator.error("2st param must be of type str, {} given".format(type(params[1])))

    return getattr(params[0], params[1])


def load_module_functions(module):
    """Get all module functions"""
    return inspect.getmembers(module, inspect.isfunction)


def module_exists(module_name):
    """Does module exists"""
    return importlib.util.find_spec(module_name) is not None
