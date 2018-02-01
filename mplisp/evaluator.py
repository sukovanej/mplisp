from mplisp import syntax
from mplisp.structures import tree
from mplisp.functions import default_functions
import concurrent.futures


def evaluate(value: str):
    syntax_tree = syntax.create_tree(value)
    syntax_tree.local_env.symbols = default_functions.get_functions()

    for node in syntax_tree.children:
        yield evaluate_node(node)


def evaluate_node(node: tree.SyntaxTreeNode):
    if not isinstance(node, tree.SyntaxTreeNode):
        return node

    if not node.children:
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

    return None


def evaluate_parallel_args(args):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        return list(executor.map(evaluate_node, args))


def error(value: str):
    """Return error message and exit"""
    print("[\033[91merror\033[0m: {}]".format(value))
    quit()
