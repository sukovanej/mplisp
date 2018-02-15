import unittest
import mplisp.evaluator as evaluator


class TestQuote(unittest.TestCase):

    def simple_test(self):
        input1 = """(quote (1 2 3))"""
        input2 = """(quote ((1 2) (3 4)))"""
        input3 = """(quote ahoj)"""
        input4 = """(quote 1)"""

        output1 = list(evaluator.evaluate(input1))
        output2 = list(evaluator.evaluate(input2))
        output3 = list(evaluator.evaluate(input3))
        output4 = list(evaluator.evaluate(input4))

        self.assertEqual(output1[0], [1, 2, 3])
        self.assertEqual(output2[0], [[1, 2], [3, 4]])
        self.assertEqual(output3[0], 'ahoj')
        self.assertEqual(output4[0], 1)

    def quote_syntax_test(self):
        input1 = "`(1 2 3)"
        input2 = "`((1 2) (3 4))"
        input3 = "`ahoj"
        input4 = "`1"
        input5 = "`()"
        input6 = "`(() (()))"

        output1 = list(evaluator.evaluate(input1))
        output2 = list(evaluator.evaluate(input2))
        output3 = list(evaluator.evaluate(input3))
        output4 = list(evaluator.evaluate(input4))
        output5 = list(evaluator.evaluate(input5))
        output6 = list(evaluator.evaluate(input6))

        self.assertEqual(output1[0], [1, 2, 3])
        self.assertEqual(output2[0], [[1, 2], [3, 4]])
        self.assertEqual(output3[0], 'ahoj')
        self.assertEqual(output4[0], 1)
        self.assertEqual(output5[0], [])
        self.assertEqual(output6[0], [[], [[]]])
