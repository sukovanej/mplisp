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
    params = evaluator.evaluate_parallel_args(args)

    if len(params) == 1:
        return -1 * params[0]

    return params[0] - functools.reduce(lambda x, y: x + y, params[1:])


def plus(args: List, _):
    """Evaluates expression (+ a b c d ...) as {a + b + c + d + ...)}"""
    params = evaluator.evaluate_parallel_args(args)
    return functools.reduce(lambda x, y: x + y, params)


def multiply(args: List, _):
    """Evaluates expression (* a b c d ...) as {a * b * c * d * ...)}"""
    params = evaluator.evaluate_parallel_args(args)
    return functools.reduce(lambda x, y: x * y, params)


def divide(args: List, _):
    """Evaluates expression (/ a b c d ...) as {a / (b / (c / (d / ...)..)}"""
    params = evaluator.evaluate_parallel_args(args)
    return functools.reduce(lambda x, y: x / y, params)


def sqrt(args: List, node):
    """Evaluates expression (sqrt a) as {sqrt(a)}"""
    if len(args) != 1:
        evaluator.error("(arithmetic.basic.sqrt) wrong number of arguments, got {}, 1 expected".format(
            str(len(args))), node)

    return math.sqrt(evaluator.evaluate_node(args[0]))


def modulo(args: List, node):
    """Evaluates expression (sqrt a) as {sqrt(a)}"""
    if len(args) != 2:
        evaluator.error("(arithmetic.basic.modulo) wrong number of arguments, got {}, 2 expected".format(
            str(len(args))), node)

    params = evaluator.evaluate_parallel_args(args)
    return params[0] % params[1]
