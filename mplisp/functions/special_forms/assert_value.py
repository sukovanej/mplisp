from typing import List
from mplisp import evaluator
from mplisp.functions.special_forms.control_statemets import FALSE_STATEMENTS


def assert_value(args: List, node):
    """First argument must be True"""
    if len(args) != 1:
        evaluator.error("1 parameter expected, {} given".format(len(args)))

    value = evaluator.evaluate_node(args[0])

    if value in FALSE_STATEMENTS:
        evaluator.error("Assertion failed: {}".format(node))

    return None


def assert_equal(args: List, node):
    """First argument must equals to the second one"""
    if len(args) != 2:
        evaluator.error("2 parameter expected, {} given".format(len(args)))

    values = evaluator.evaluate_parallel_args(args)

    if values[0] != values[1]:
        evaluator.error("Assertion failed: {} != {} \n {}".format(values[0], values[1], node))

    return None
