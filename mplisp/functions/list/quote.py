""" Lists
"""
from typing import List
from mplisp.structures import tree
import mplisp.evaluator


def quote(args: List, _):
    """Create list"""
    return _syntax_tree_to_list(args)


def _syntax_tree_to_list(node_array: List[tree.SyntaxTreeNode]):
    if len(node_array) == 1 and not node_array[0].children:
        value = mplisp.evaluator.evaluate_value_symbol(node_array[0].value)
        if value is None:
            value = node_array[0].value

        return value

    result = []
    for node in node_array:
        if node.children:
            result.append(_syntax_tree_to_list(node.children))
        else:
            value = mplisp.evaluator.evaluate_value_symbol(node.value)
            if value is None:
                value = node.value

            result.append(value)

    return result
