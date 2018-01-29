from typing import List
import functools
import evaluator


def define(args: List, node):
    if len(args) != 2:
        return "[error: wrong number of arguments]"
    else:
        if args[0].value in node.parent.local_env.symbols:
            return "[error: " + args[0].value + " already defined]"

        node.parent.local_env.symbols[args[0].value] = evaluator.evaluate_node(
            args[1])

        return None