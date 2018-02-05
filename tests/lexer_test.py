import unittest
import mplisp.lexer as lexer


class TestLexer(unittest.TestCase):

    def test_string(self):
        """test string"""
        input1 = "(def a 'str')"
        input2 = "(def a \"str\")"

        output1 = list(lexer.lexer(input1))
        output2 = list(lexer.lexer(input2))

        output_expected_1 = ['(', 'def', 'a', '\'str\'', ')']
        output_expected_2 = ['(', 'def', 'a', '\"str\"', ')']

        self.assertEqual(output1, output_expected_1)
        self.assertEqual(output2, output_expected_2)
