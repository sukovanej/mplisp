""" Basic arithmetic operations

Examples:
(+ 1 2)
(- 5 (+ 1 2) 1)
(* 1 2 3 4 5)
"""
from typing import List
import functools
import math
from mplisp import evaluator


def minus(args: List, _):
    """Evaluates expression (- a b c d ...) as {a - (b + c + d + ...)}"""
    args = [evaluator.evaluate_node(arg) for arg in args]

    if len(args) == 1:
        return -1 * args[0]

    return args[0] - functools.reduce(lambda x, y: x + y, args)


def plus(args: List, _):
    """Evaluates expression (+ a b c d ...) as {a + b + c + d + ...)}"""
    args = [evaluator.evaluate_node(arg) for arg in args]
    return functools.reduce(lambda x, y: x + y, args)


def multiply(args: List, _):
    """Evaluates expression (* a b c d ...) as {a * b * c * d * ...)}"""
    args = [evaluator.evaluate_node(arg) for arg in args]
    return functools.reduce(lambda x, y: x * y, args)


def divide(args: List, _):
    """Evaluates expression (/ a b c d ...) as {a / (b / (c / (d / ...)..)}"""
    args = [evaluator.evaluate_node(arg) for arg in args]
    return functools.reduce(lambda x, y: x / y, args)


def sqrt(args: List, _):
    """Evaluates expression (sqrt a) as {sqrt(a)}"""
    if len(args) != 1:
        evaluator.error("wrong number of arguments, got {}, 1 expected".format(
            str(len(args))))

    return math.sqrt(evaluator.evaluate_node(args[0]))

def modulo(args: List, _):
    """Evaluates expression (sqrt a) as {sqrt(a)}"""
    if len(args) != 2:
        evaluator.error("wrong number of arguments, got {}, 2 expected".format(
            str(len(args))))

    params = [evaluator.evaluate_node(arg) for arg in args]
    return params[0] % params[1]
