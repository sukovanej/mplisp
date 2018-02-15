""" Lists
"""
from typing import List
from mplisp import evaluator


def create_list(args: List, _):
    """Create list"""
    return evaluator.evaluate_parallel_args(args)


def cdr_list(args: List, _):
    """Create list"""

    if len(args) != 1:
        evaluator.error("1 parameter expected, {} given.".format(len(args)), node)

    param = evaluator.evaluate_node(args[0])

    if not isinstance(param, list):
        evaluator.error("1st parameter must be of type list", node)

    return param[1:]


def car_list(args: List, _):
    """Create list"""

    if len(args) != 1:
        evaluator.error("1 parameter expected, {} given.".format(len(args)), node)

    param = evaluator.evaluate_node(args[0])

    if not isinstance(param, list):
        evaluator.error("1st parameter must be of type list", node)

    return param[0]


def slice_list(args: List, node):
    """slice of list"""
    if len(args) < 2:
        evaluator.error("at least 2 parameters expected, {} given.".format(len(args)), node)

    param = evaluator.evaluate_node(args[0])

    if not isinstance(param, list) and not isinstance(param, str):
        evaluator.error("1st parameter must be of type list or str", node)

    params = evaluator.evaluate_parallel_args(args[1:])

    if not isinstance(params[0], int):
        evaluator.error("1st parameter must be of type int", node)

    if len(args) == 2:
        return param[params[0]:]

    if not isinstance(params[1], int):
        evaluator.error("2st parameter must be of type int", node)

    return param[params[0]:params[1]]


def map_list(args: List, node):
    """Map list"""
    if len(args) != 2:
        evaluator.error("2 parameters expected, {} given.".format(len(args)), node)

    function_object = evaluator.evaluate_node(args[0])

    if not callable(function_object):
        evaluator.error("map function is not callable", node)

    arg_list = evaluator.evaluate_node(args[1])

    return list(map(lambda x: function_object([x], node), arg_list))


def gen_list(args: List, node):
    """get range(*params)"""
    params = evaluator.evaluate_parallel_args(args)

    return list(range(*params))


def list_ref(args: List, _):
    """Check whether the first argument is list and the second one is int.
    Return element on that position"""
    if len(args) != 2:
        evaluator.error("2 parameters expected, {} given.".format(len(args)), node)

    params = evaluator.evaluate_parallel_args(args)

    if not isinstance(params[0], list):
        evaluator.error("1st parameter must be of type list", node)

    if not isinstance(params[1], int):
        evaluator.error("2st parameter must be of type list", node)

    if params[1] < 0 or params[1] >= len(params[0]):
        evaluator.error("index {} is out of range".format(params[1]), node)

    return params[0][params[1]]


def list_apply(args: List, node):
    """Evaluate function on params given by list"""
    if len(args) != 2:
        evaluator.error("2 parameters expected, {} given.".format(len(args)), node)

    function_object = evaluator.evaluate_node(args[0])

    if not callable(function_object):
        evaluator.error("apply function is not callable", node)

    arg_list = evaluator.evaluate_node(args[1])

    if not isinstance(arg_list, list):
        evaluator.error("apply function is not callable", node)

    return function_object(arg_list, node)


def list_length(args: List, node):
    """Return list length"""
    value = evaluator.evaluate_node(args[0])

    if not isinstance(value, list):
        evaluator.error("1st argument must be list", node)

    return len(value)


def enumerate_list(args: List, node):
    """Python enumerate equiv."""
    value = evaluator.evaluate_node(args[0])

    if not isinstance(value, list):
        evaluator.error("1st argument must be list", node)

    return list(enumerate(value))


def filter_list(args: List, node):
    """Filter list"""
    if len(args) != 2:
        evaluator.error("2 parameters expected, {} given.".format(len(args)), node)

    function_object = evaluator.evaluate_node(args[0])

    if not callable(function_object):
        evaluator.error("1st parameter is not callable", node)

    arg_list = evaluator.evaluate_node(args[1])

    return list(filter(lambda x: function_object([x], node), arg_list))

