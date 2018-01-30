from typing import List
import copy
from mplisp import evaluator


def lambda_expression(args: List, node):
    if len(args) != 2:
        return "[error: wrong number of arguments, 2 expected]"

    params = [arg.value for arg in args[0].children]
    return create_lambda(params, node.children[2])


def create_lambda(params, body):
    """Generate lambda function"""

    def func(local_args: List, _):
        new_node = copy.deepcopy(body)

        for i, arg in enumerate(params):
            new_node.local_env.symbols[arg] = evaluator.evaluate_node(
                local_args[i])

        return evaluator.evaluate_node(new_node)

    return func
