import concurrent.futures

from mplisp import syntax
from mplisp.structures import tree, env
from mplisp.functions import default_functions
from mplisp.lexer import STR_SURROUND


def evaluate(value: str, local_env=None):
    """Evaluate input"""
    syntax_tree = syntax.create_tree(value)

    if local_env is None:
        local_env = env.EnvNode({})
        local_env.symbols = default_functions.get_functions()

    syntax_tree.local_env = local_env

    for node in syntax_tree.children:
        if node.value and node.value.startswith('#!'):  # shebang
            continue

        yield evaluate_node(node)


def evaluate_node(node: tree.SyntaxTreeNode):
    if not isinstance(node, tree.SyntaxTreeNode):
        return node

    if not node.children:
        result = evaluate_symbol(node.value, node)

        if result is None:
            if node.value[0] in STR_SURROUND and node.value[len(node.value) - 1] == node.value[0]:
                result = str(node.value[1:-1])
            else:
                try:
                    result = float(node.value)
                    result_int = int(result)

                    if result == result_int:
                        result = result_int
                except ValueError:
                    error("{} not found".format(node.value), node)
        elif isinstance(result, tree.SyntaxTreeNode):
            result = evaluate_node(result)
    else:
        func = evaluate_node(node.children[0])

        if callable(func):
            result = func(node.children[1:], node)
        else:
            error("{} is not callable".format(node.children[0].value), node)

    return result


def evaluate_symbol(symbol: str, node: tree.SyntaxTreeNode):
    """Evaluate symbol"""
    if node.local_env is not None and symbol in node.local_env.symbols:
        return node.local_env.symbols[symbol]
    elif node.parent is not None:
        return evaluate_symbol(symbol, node.parent)

    return None


def evaluate_parallel_args(args):
    """Evaluate args in parallel"""
    with concurrent.futures.ThreadPoolExecutor() as executor:
        return list(executor.map(evaluate_node, args))


def error(value: str, node: tree.SyntaxTreeNode):
    """Return error message and exit"""
    raise ValueError("[\033[91m error \033[0m: {} on line {}]".format(value, node.line))
