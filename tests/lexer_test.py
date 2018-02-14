import unittest
import mplisp.lexer as lexer


class TestLexer(unittest.TestCase):

    def test_string(self):
        """test string"""
        input1 = '(def a \'str\')'
        input2 = '(def a \"str\")'
        input3 = '\'str\''
        input4 = '`()'

        output1 = list(lexer.lexer(input1))
        output2 = list(lexer.lexer(input2))
        output3 = list(lexer.lexer(input3))
        output4 = list(lexer.lexer(input4))

        output_expected_1 = [('(', 1), ('def', 1), ('a', 1), ('\'str\'', 1), (')', 1)]
        output_expected_2 = [('(', 1), ('def', 1), ('a', 1), ('\"str\"', 1), (')', 1)]
        output_expected_3 = [('\'str\'', 1)]
        output_expected_4 = [('(', 1), ('quote', 1), (')', 1)]

        self.assertEqual(output1, output_expected_1)
        self.assertEqual(output2, output_expected_2)
        self.assertEqual(output3, output_expected_3)
        self.assertEqual(output4, output_expected_4)
