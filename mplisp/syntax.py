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

    last_token = ('', 0)

    for token in lexer.lexer(value):
        actual_node = syntax(token, actual_node, last_token)
        last_token = token

    return main_node


def syntax(token, node: tree.SyntaxTreeNode, last_token) -> tree.SyntaxTreeNode:
    """create node"""
    if token[0] == '`':
        return node

    if last_token[0] == "`":
        node = node.append("")
        node.append("quote")

    if token[0] == '(':
        new_node = node.append("")
        new_node.line = token[1]
        return new_node
    elif token[0] == ')':
        if node.parent and node.parent.children and node.parent.children[0].value == 'quote':
            return node.parent.parent

        return node.parent

    new_node = node.append(token[0])
    new_node.line = token[1]

    return node
