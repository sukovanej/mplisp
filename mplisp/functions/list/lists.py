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
        evaluator.error("At least 2 parameters expected, {} given.".format(len(args)))

    function = evaluator.evaluate_node(args[0])

    if not callable(function):
        evaluator.error("map function is not callable")

    arg_list = evaluator.evaluate_node(args[1])

    return list(map(lambda x: function([x], node), arg_list))
