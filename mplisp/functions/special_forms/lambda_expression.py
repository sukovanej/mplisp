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
from mplisp.structures import env
from mplisp import evaluator


def lambda_expression(args: List, node):
    """Return lambda expression"""
    if len(args) != 2:
        evaluator.error("2 parameters expected, {} given".format(len(args)))

    return create_lambda(args, node)


def let_expression(args: List, node):
    """Return let expression"""
    with concurrent.futures.ThreadPoolExecutor() as executor:
        def set_env(x):
            (x, evaluator.evaluate_node(x.children[1]))

        for name, value in executor.map(set_env, args[0].children):
            node.local_env.symbols[name.children[0].value] = value

    return evaluator.evaluate_node(args[1])


def let_star_expression(args: List, node):
    """Return let expression"""
    for param in args[0].children:
        node.local_env.symbols[param.children[0].value] = evaluator.evaluate_node(
            param.children[1])

    return evaluator.evaluate_node(args[1])


def create_lambda(args, node):
    """Generate lambda function"""
    params = [arg.value for arg in args[0].children]

    def func(local_args: List, _):
        """Callable object"""
        new_node = copy.deepcopy(node.children[2])

        for arg, value in zip(params, local_args):
            new_node.getenv().symbols[arg] = evaluator.evaluate_node(value)

        return evaluator.evaluate_node(new_node)

    return func
