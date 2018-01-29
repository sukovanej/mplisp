from typing import List
import functools
from mplisp import evaluator


TRUE_STATEMENTS = [False, 0]


def and_statement(args: List, _):
    for arg in args:
        if evaluator.evaluate_node(arg) in TRUE_STATEMENTS:
            return False

    return True


def or_statement(args: List, _):
    for arg in args:
        if evaluator.evaluate_node(arg) not in TRUE_STATEMENTS:
            return True

    return False


def smaller_statement(args: List, _):
    return evaluator.evaluate_node(args[0]) < evaluator.evaluate_node(args[1])


def greater_statement(args: List, _):
    return evaluator.evaluate_node(args[0]) > evaluator.evaluate_node(args[1])


def equals_statement(args: List, node):
    return evaluator.evaluate_node(args[0]) == evaluator.evaluate_node(args[1])


def if_statement(args: List, _):
    if len(args) != 3:
        return "[error: wrong number of arguments, 3 expected]"
    else:
        condition = evaluator.evaluate_node(args[0])

        if condition:
            return evaluator.evaluate_node(args[1])
        else:
            return evaluator.evaluate_node(args[2])