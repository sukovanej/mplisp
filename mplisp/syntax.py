from structures import tree
import lexer

'''
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
'''


def create_tree(value: str) -> tree.SyntaxTreeNode:
    main_node = tree.SyntaxTreeNode("", [], None)
    actual_node = main_node

    for token in lexer.lexer(value):
        actual_node = syntax(token, actual_node)

    return main_node


def syntax(token, node: tree.SyntaxTreeNode) -> tree.SyntaxTreeNode:
    if token == '(':
        return node.append("")
    elif token == ')':
        return node.parent
    else:
        node.append(token)
        return node


def test():
    print(create_tree("1"))


if __name__ == "__main__":
    test()
