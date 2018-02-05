import unittest
import mplisp.evaluator as evaluator


class TestLambdaExpression(unittest.TestCase):

    def test_simple(self):
        """test string"""
        input1 = '((lambda (x) x) 1)'

        output1 = list(evaluator.evaluate(input1))

        self.assertEqual(output1, [1])
