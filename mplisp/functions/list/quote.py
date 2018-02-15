""" Lists
"""
from typing import List
from mplisp.structures import tree
import mplisp.evaluator


def quote(args: List, node):
    """Create list"""
    if len(args) != 1:
        mplisp.evaluator.error("(lists.quote.quote) 1 parameter expected, {} given.".format(len(args)), node)

    return _syntax_tree_to_list(args[0])


def _evaluate_value(value):
    result = mplisp.evaluator.evaluate_value_symbol(value)

    if result is None:
        result = value

    return result


def _syntax_tree_to_list(node: tree.SyntaxTreeNode):
    if node.value:
        return _evaluate_value(node.value)

    result = []
    for node in node.children:
        if not node.value:
            result.append(_syntax_tree_to_list(node))
        else:
            result.append(_evaluate_value(node.value))

    return result
