"""import special form

Exmaples:
(import std.io.petr)
"""
from types import ModuleType
from typing import List
import os
import importlib
import importlib.util
import inspect
from mplisp import evaluator
from mplisp.structures import env


def import_module(args: List, node):
    """
    Import all functions from a module and add corresponding symbols
    to the parent environment.
    """
    module_name = evaluator.evaluate_node(args[0])

    if not isinstance(module_name, str):
        evaluator.error("(special_forms.module_import.import) 1st param must be of type str", node)

    local_path = module_name + ".mplisp"
    absolute_path = os.path.join("/usr/lib/mplisp", local_path)
    path = ''

    if os.path.isfile(local_path):
        path = local_path
    elif os.path.isfile(absolute_path):
        path = absolute_path

    if path:
        with open(local_path) as file_object:
            list(evaluator.evaluate(file_object.read(), node.getenv()))
            return None

    mplispstd = module_name.replace("std", "mplispstd")

    if module_exists(mplispstd):
        module_name = mplispstd
    elif not module_exists(module_name):
        evaluator.error("(special_forms.module_import.import) package {} not found".format(module_name), node)

    mod = importlib.import_module(module_name)
    return mod


def python_getattr(args: List, node):
    """Call python function from mplisp"""
    if len(args) != 2:
        evaluator.error("(special_forms.module_import.get_attribute) 2 parameters expected, {} given".format(len(args)), node)

    params = evaluator.evaluate_parallel_args(args)

    if not isinstance(params[0], ModuleType):
        params[0] = import_module(args[0:1], node)

    if not isinstance(params[1], str):
        evaluator.error("(special_forms.module_import.get_attribute) 2st param must be of type str, {} given".format(type(params[1])), node)

    attr = getattr(params[0], params[1])

    if callable(attr):
        return function_caller(attr)

    return attr


def function_caller(func_obj):
    def func(local_args: List, _):
        """Callable object"""
        params = evaluator.evaluate_parallel_args(local_args)

        return func_obj(*params)

    return func


def load_module_functions(module):
    """Get all module functions"""
    return inspect.getmembers(module, inspect.isfunction)


def module_exists(module_name):
    """Does module exists"""
    return importlib.util.find_spec(module_name) is not None
