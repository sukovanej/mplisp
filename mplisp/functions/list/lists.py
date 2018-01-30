""" Lists
"""
from typing import List
from mplisp import evaluator


def create_list(args: List, _):
    """Create list"""
    return [evaluator.evaluate_node(arg) for arg in args]


def map_list(args: List, node):
    """Map list"""
    if len(args) != 2:
        evaluator.error("2 parameters expected, {} given.".format(len(args)))

    function = evaluator.evaluate_node(args[0])

    if not callable(function):
        evaluator.error("map function is not callable")

    arg_list = evaluator.evaluate_node(args[1])

    return list(map(lambda x: function([x], node), arg_list))


def gen_list(args: List, _):
    """get range(*params)"""
    params = [evaluator.evaluate_node(arg) for arg in args]

    return list(range(*params))


def list_ref(args: List, _):
    if len(args) != 2:
        evaluator.error("2 parameters expected, {} given.".format(len(args)))

    params = [evaluator.evaluate_node(arg) for arg in args]

    if not isinstance(params[0], list):
        evaluator.error("1st parameter must be of type list")

    if not isinstance(params[1], int):
        evaluator.error("1st parameter must be of type list")

    if params[1] < 0 or params[1] >= len(params[0]):
        evaluator.error("index {} is out of range".format(params[1]))

    return params[0][params[1]]