from typing import List
from mplisp import evaluator
from mplisp.functions.special_forms.control_statemets import FALSE_STATEMENTS


def is_null(args: List, node):
    """Is value null"""
    if len(args) != 1:
        evaluator.error("(special_forms.types.is_null) 1 parameters expected, {} given".format(len(args)), node)

    return evaluator.evaluate_symbol(args[0].value, node) is None


def is_bool(args: List, node):
    """Is value boolean"""
    if len(args) != 1:
        evaluator.error("(special_forms.types.is_bool) 1 parameters expected, {} given".format(len(args)), node)

    return isinstance(evaluator.evaluate_node(args[0]), bool)


def is_list(args: List, node):
    """Is value list"""
    if len(args) != 1:
        evaluator.error("(special_forms.types.is_list) 1 parameters expected, {} given".format(len(args)), node)

    return isinstance(evaluator.evaluate_node(args[0]), list)


def to_bool(args: List, node):
    """Convert expression to its boolean value"""
    if len(args) != 1:
        evaluator.error("(special_forms.types.to_bool) 1 parameter expected, {} given".format(len(args)), node)

    value = evaluator.evaluate_node(args[0])
    return value not in FALSE_STATEMENTS


def to_int(args: List, node):
    """Convert expression to its boolean value"""
    if len(args) != 1:
        evaluator.error("(special_forms.types.to_int) 1 parameter expected, {} given".format(len(args)), node)

    value = evaluator.evaluate_node(args[0])
    return int(value)
