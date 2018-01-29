from typing import List
import copy
import functools
import evaluator
from structures import tree


def lambda_expression(args: List, node):
    if len(args) != 2:
        return "[error: wrong number of arguments, 2 expected]"
    else:
        params = [arg.value for arg in args[0].children]
        eval_node = args[1]

        def func(local_args: List, local_node): 
            new_node = copy.deepcopy(node.children[2])

            for i, arg in enumerate(params):
                new_node.local_env.symbols[arg] = evaluator.evaluate_node(
                    local_args[i])

            return evaluator.evaluate_node(new_node)

        return func