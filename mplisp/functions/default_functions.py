from typing import List
import evaluator
from structures import tree

from functions.arithmetic import basic
from functions.special_forms import define
from functions.special_forms import lambda_expression
from functions.special_forms import control_statemets

def get_functions():
    return {
        "+": basic.plus,
        "-": basic.minus,
        "*": basic.multiply,
        "/": basic.divide,
        "and?": control_statemets.and_statement,
        "or?": control_statemets.or_statement,
        "eq?": control_statemets.equals_statement,
        "if": control_statemets.if_statement,
        ">": control_statemets.greater_statement,
        "<": control_statemets.smaller_statement,
        "sqrt": basic.sqrt,
        "def": define.define,
        "lambda": lambda_expression.lambda_expression,
        "import": import_module
    }

def import_module(args: List, node):
    import inspect

    module_name = args[0].value
    functions = inspect.getmembers('typing', inspect.isfunction)
    __import__(module_name)