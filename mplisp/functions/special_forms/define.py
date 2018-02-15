from typing import List
from mplisp import evaluator


def define(args: List, node):
    """create new name->symbol connection"""
    if len(args) != 2:
        evaluator.error("(special_forms.define.def) 2 parameters expected, {} given".format(len(args)), node)

    if args[0].value in node.parent.getenv().symbols:
        evaluator.error("(special_forms.define.def) {} already defined".format(args[0].value), node)

    node.parent.getenv().symbols[args[0].value] = evaluator.evaluate_node(
        args[1])

    return None
