from typing import List
from mplisp import evaluator


def is_null(args: List, node):
    """Is value null"""
    if len(args) != 1:
        evaluator.error("1 parameters exptected, {} given".format(len(args)))

    return evaluator.evaluate_symbol(args[0].value, node) is None


def is_bool(args: List, _):
    """Is value boolean"""
    if len(args) != 1:
        evaluator.error("1 parameters exptected, {} given".format(len(args)))

    return isinstance(evaluator.evaluate_node(args[0]), bool)


def is_list(args: List, _):
    """Is value list"""
    if len(args) != 1:
        evaluator.error("1 parameters exptected, {} given".format(len(args)))

    return isinstance(evaluator.evaluate_node(args[0]), list)

