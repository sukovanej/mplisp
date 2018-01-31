from typing import List
from mplisp import evaluator
from mplisp.functions.special_forms.control_statemets import TRUE_STATEMENTS


def is_null(args: List, node):
    """Is value null"""
    if len(args) != 1:
        evaluator.error("1 parameters exptected, {} given".format(len(args)))

    return evaluator.evaluate_symbol(args[0].value, node) is not None


def is_bool(args: List, node):
    """Is value boolean"""
    if len(args) != 1:
        evaluator.error("1 parameters exptected, {} given".format(len(args)))

    return evaluator.evaluate_node(args[0]) in TRUE_STATEMENTS


def is_list(args: List, node):
    """Is value list"""
    if len(args) != 1:
        evaluator.error("1 parameters exptected, {} given".format(len(args)))

    return isinstance(evaluator.evaluate_node(args[0]), list)

