""" Lists
"""
from typing import List
from mplisp.structures import tree


def quote(args: List, _):
    """Create list"""
    return _syntax_tree_to_list(args)


def _syntax_tree_to_list(node_array: List[tree.SyntaxTreeNode]):
    result = []

    for node in node_array:
        if node.children:
            result.append(_syntax_tree_to_list(node.children))
        else:
            result.append(node.value)

    return result
