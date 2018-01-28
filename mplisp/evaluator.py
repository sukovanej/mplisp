import syntax
from structures import tree
from functions import default_functions


def evaluate(value: str):
    syntax_tree = syntax.create_tree(value)
    syntax_tree.local_env.symbols = default_functions.get_functions()

    for node in syntax_tree.children:
        yield evaluate_node(node)


def evaluate_node(node: tree.SyntaxTreeNode):
    if len(node.children) == 0:
        result = evaluate_symbol(node.value, node.parent)

        if result is None:
            try:
                result = float(node.value)
                result_int = int(result)

                if result == result_int:
                    result = result_int

            except ValueError:
                result = None
        elif isinstance(result, tree.SyntaxTreeNode):
            result = evaluate_node(result)
    else:
        func = evaluate_node(node.children[0])

        if callable(func):
            result = func(node.children[1:], node)
        else:
            print("[error: '" + node.children[0].value + "' is not callable]")
            quit()

    return result


def evaluate_symbol(symbol: str, node: tree.SyntaxTreeNode):
    if symbol in node.local_env.symbols:
        return node.local_env.symbols[symbol]
    elif node.parent is not None:
        return evaluate_symbol(symbol, node.parent)
    else:
        return None


def test():
    inputs = [
        "(+ (+ 1 1) 2 3)",
        "1",
        "(+ 1 2)",
        "(- 1 2)",
        "(* 2 3 4)",
        "(/ 4 (+ 1 1))",
        "(- 5)"
    ]

    expected_outputs = [
        7,
        1,
        3,
        -1,
        24,
        2,
        -5
    ]

    outputs = list(evaluate('\n'.join(inputs)))

    assert expected_outputs == outputs

    print(list(evaluate("""
        (def pyth 
            (lambda (a b)
                (sqrt (+ (* a a) (* b b)))))
        (pyth 9 12)
    """)))


if __name__ == "__main__":
    test()
