from typing import List
import functools
import evaluator
from structures import tree


def lambda_expression(args: List, node):
    if len(args) != 2:
        return "[error: wrong number of arguments]"
    else:
        params = [arg.value for arg in args[0].children]
        eval_node = args[1]

        def func(local_args, local_node): 
            new_node = tree.SyntaxTreeNode("", eval_node.children, node)

            for child in eval_node.children:
                child.parent = new_node

            for i, arg in enumerate(params):
                new_node.local_env.symbols[arg] = evaluator.evaluate_node(
                    local_args[i])

            return evaluator.evaluate_node(new_node)

        return func