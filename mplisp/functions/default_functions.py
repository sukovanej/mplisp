from mplisp.functions.arithmetic import basic
from mplisp.functions.special_forms import define
from mplisp.functions.special_forms import lambda_expression
from mplisp.functions.special_forms import control_statemets
from mplisp.functions.special_forms import module_import


def get_functions():
    return {
        "+": basic.plus,
        "-": basic.minus,
        "*": basic.multiply,
        "/": basic.divide,
        "sqrt": basic.sqrt,

        "if": control_statemets.if_statement,
        "and?": control_statemets.and_statement,
        "or?": control_statemets.or_statement,
        "==": control_statemets.equals_statement,
        ">": control_statemets.greater_statement,
        "<": control_statemets.smaller_statement,

        "def": define.define,
        "lambda": lambda_expression.lambda_expression,
        "import": module_import.import_module
    }
