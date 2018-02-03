from mplisp.structures import tree
from mplisp import lexer

"""
(mil 1 2)
""
    -> mil
    -> 1
    -> 2

((2 3) petr)
""
    -> ""
        -> 2
        -> 3
    -> petr
"""


def create_tree(value: str) -> tree.SyntaxTreeNode:
    """create the whole tree"""
    main_node = tree.SyntaxTreeNode("", [], None)
    actual_node = main_node

    for token in lexer.lexer(value):
        actual_node = syntax(token, actual_node)

    return main_node


def syntax(token: str, node: tree.SyntaxTreeNode) -> tree.SyntaxTreeNode:
    """create node"""
    if token == '(':
        return node.append("")
    elif token == ')':
        return node.parent

    node.append(token)
    return node
