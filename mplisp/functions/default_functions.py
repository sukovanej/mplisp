""" mplisp basic functions
"""
from mplisp.functions.arithmetic import basic
from mplisp.functions.special_forms import define
from mplisp.functions.special_forms import lambda_expression
from mplisp.functions.special_forms import control_statemets
from mplisp.functions.special_forms import module_import
from mplisp.functions.special_forms import types
from mplisp.functions.special_forms import assert_value
from mplisp.functions.list import lists
from mplisp.functions.list import quote


def get_functions():
    """Generate basic functions"""
    return {
        "+": basic.plus,
        "-": basic.minus,
        "*": basic.multiply,
        "/": basic.divide,
        "%": basic.modulo,
        "sqrt": basic.sqrt,

        "#t": True,
        "#f": False,

        "if": control_statemets.if_statement,
        "and?": control_statemets.and_statement,
        "or?": control_statemets.or_statement,
        "not?": control_statemets.not_statement,
        "==": control_statemets.equals_statement,
        "!=": control_statemets.not_equals_statement,
        ">": control_statemets.greater_statement,
        "<": control_statemets.smaller_statement,

        "null?": types.is_null,
        "bool?": types.is_bool,
        "list?": types.is_list,

        "->bool?": types.to_bool,
        "->int": types.to_int,

        "def": define.define,
        "lambda": lambda_expression.lambda_expression,
        "let": lambda_expression.let_expression,
        "let*": lambda_expression.let_star_expression,

        "import": module_import.import_module,
        "get-attribute": module_import.python_getattr,

        "list": lists.create_list,
        "map": lists.map_list,
        "filter": lists.filter_list,
        "range": lists.gen_list,
        "list-ref": lists.list_ref,
        "apply": lists.list_apply,
        "length": lists.list_length,
        "slice": lists.slice_list,
        "car": lists.car_list,
        "cdr": lists.cdr_list,
        "quote": quote.quote,

        "enumerate": lists.enumerate_list,

        "assert!": assert_value.assert_value,
        "assert-equal!": assert_value.assert_equal
    }
