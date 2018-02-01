""" Lambda, let, let*

Examples:
(let
    (
        (a 6))
    (* a 1))
"""
from typing import List
import copy
import concurrent.futures
from mplisp import evaluator


def lambda_expression(args: List, node):
    """Return lambda expression"""
    if len(args) != 2:
        evaluator.error("2 parameters exptected, {} given".format(
            len(args)
        ))

    params = [arg.value for arg in args[0].children]
    return create_lambda(params, node.children[2])


def let_expression(args: List, node):
    """Return let expression"""
    for param in args[0].children:
        node.local_env.symbols[param.children[0].value] = evaluator.evaluate_node(
            param.children[1])

    return evaluator.evaluate_node(args[1])


def let_star_expression(args: List, node):
    """Return let expression"""
    for param in args[0].children:
        node.local_env.symbols[param.children[0].value] = evaluator.evaluate_node(
            param.children[1])

    return evaluator.evaluate_node(args[1])


def create_lambda(params, body):
    """Generate lambda function"""

    def func(local_args: List, _):
        """Callable object"""
        new_node = copy.deepcopy(body)

        with concurrent.futures.ThreadPoolExecutor() as executor:
            for arg, value in zip(params, executor.map(evaluator.evaluate_node,
                    local_args)):
                new_node.local_env.symbols.update({arg: value})

        return evaluator.evaluate_node(new_node)

    return func
