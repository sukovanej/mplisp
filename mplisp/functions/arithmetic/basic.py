from typing import List
import functools
import math
from mplisp import evaluator


def minus(args: List, node):
    args = [evaluator.evaluate_node(arg) for arg in args]

    if len(args) == 1:
        return -1 * args[0]
    else:
        return args[0] - functools.reduce(lambda x, y: x + y, args[1:], 0)


def plus(args: List, _):
    args = [evaluator.evaluate_node(arg) for arg in args]
    return functools.reduce(lambda x, y: x + y, args, 0)


def multiply(args: List, _):
    args = [evaluator.evaluate_node(arg) for arg in args]
    return functools.reduce(lambda x, y: x * y, args, 1)


def divide(args: List, _):
    args = [evaluator.evaluate_node(arg) for arg in args]
    return functools.reduce(lambda x, y: x / y, args[1:], args[0])


def sqrt(args: List, _):
    if len(args) == 1:
        return math.sqrt(evaluator.evaluate_node(args[0]))
    else:
        return "[error: wrong number of arguments, got " + str(len(args)) + ", 1 expected"
