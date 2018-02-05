import unittest
import mplisp.lexer as lexer


class TestLexer(unittest.TestCase):

    def test_string(self):
        """test string"""
        input1 = "(def a 'str')"
        input2 = "(def a \"str\")"

        output1 = lexer.lexer(input1)
        output2 = lexer.lexer(input2)

        print(list(output1))
        print(list(output2))
