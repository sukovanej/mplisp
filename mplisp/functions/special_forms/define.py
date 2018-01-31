from typing import List
from mplisp import evaluator


def define(args: List, node):
    if len(args) != 2:
        evaluator.error("2 parameters exptected, {} given".format(
            len(args)
        ))
    else:
        if args[0].value in node.parent.local_env.symbols:
            evaluator.error("{} already defined".format(args[0].value))

        node.parent.local_env.symbols[args[0].value] = evaluator.evaluate_node(
            args[1])

        return None
