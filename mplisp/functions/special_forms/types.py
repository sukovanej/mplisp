from typing import List
from mplisp import evaluator
from mplisp.functions.special_forms.control_statemets import FALSE_STATEMENTS


def is_null(args: List, node):
    """Is value null"""
    if len(args) != 1:
        evaluator.error("1 parameters expected, {} given".format(len(args)))

    return evaluator.evaluate_symbol(args[0].value, node) is None


def is_bool(args: List, _):
    """Is value boolean"""
    if len(args) != 1:
        evaluator.error("1 parameters expected, {} given".format(len(args)))

    return isinstance(evaluator.evaluate_node(args[0]), bool)


def is_list(args: List, _):
    """Is value list"""
    if len(args) != 1:
        evaluator.error("1 parameters expected, {} given".format(len(args)))

    return isinstance(evaluator.evaluate_node(args[0]), list)


def to_bool(args: List, _):
    """Convert expression to its boolean value"""
    if len(args) != 1:
        evaluator.error("1 parameter expected, {} given".format(len(args)))

    value = evaluator.evaluate_node(args[0])
    return value not in FALSE_STATEMENTS


def to_int(args: List, _):
    """Convert expression to its boolean value"""
    if len(args) != 1:
        evaluator.error("1 parameter expected, {} given".format(len(args)))

    value = evaluator.evaluate_node(args[0])
    return int(value)
