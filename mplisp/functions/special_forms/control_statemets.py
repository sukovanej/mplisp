from typing import List
from mplisp import evaluator


FALSE_STATEMENTS = [False, 0]


def and_statement(args: List, _):
    """Evaluate (and? a b c ...) as {a && b && c && ...}"""
    for arg in args:
        if evaluator.evaluate_node(arg) in FALSE_STATEMENTS:
            return False

    return True


def or_statement(args: List, _):
    """Evaluate (or? a b c ...) as {a || b || c || ...}"""
    for arg in args:
        if evaluator.evaluate_node(arg) not in FALSE_STATEMENTS:
            return True

    return False


def smaller_statement(args: List, node):
    """Evaluate (< a b) as {a < b}"""
    if len(args) != 2:
        evaluator.error("(special_forms.control_statements.smaller) 2 parameters expected, {} given".format(len(args)), node)

    return evaluator.evaluate_node(args[0]) < evaluator.evaluate_node(args[1])


def not_statement(args: List, node):
    """Evaluate (< a b) as {a < b}"""
    if len(args) != 1:
        evaluator.error("(special_forms.control_statements.not) 1 parameter expected, {} given".format(len(args)), node)

    return evaluator.evaluate_node(args[0]) in FALSE_STATEMENTS


def greater_statement(args: List, node):
    """Evaluate (> a b) as {a > b}"""
    if len(args) != 2:
        evaluator.error("(special_forms.control_statements.greater) 2 parameters expected, {} given".format(len(args)), node)

    return evaluator.evaluate_node(args[0]) > evaluator.evaluate_node(args[1])


def not_equals_statement(args: List, node):
    """Evaluate (!= a b) as {a != b}"""
    if len(args) != 2:
        evaluator.error("(special_forms.control_statements.not_equals) 2 parameters expected, {} given".format(len(args)), node)

    return evaluator.evaluate_node(args[0]) != evaluator.evaluate_node(args[1])


def equals_statement(args: List, node):
    """Evaluate (== a b) as {a == b}"""
    if len(args) != 2:
        evaluator.error("(special_forms.control_statements.equals) 2 parameters expected, {} given".format(len(args)), node)

    return evaluator.evaluate_node(args[0]) == evaluator.evaluate_node(args[1])


def if_statement(args: List, node):
    """Evaluate (if cond a b) as {(cond) ? a : b}"""
    if len(args) != 3:
        evaluator.error("(special_forms.control_statements.if) 3 parameters expected, {} given".format(len(args)), node)

    condition = evaluator.evaluate_node(args[0])

    if condition:
        return evaluator.evaluate_node(args[1])

    return evaluator.evaluate_node(args[2])
