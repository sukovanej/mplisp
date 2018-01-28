from functions.arithmetic import basic
from functions.special_forms import define
from functions.special_forms import lambda_expression

def get_functions():
    return {
        "+": basic.plus,
        "-": basic.minus,
        "*": basic.multiply,
        "/": basic.divide,
        "sqrt": basic.sqrt,
        "def": define.define,
        "lambda": lambda_expression.lambda_expression,
    }
