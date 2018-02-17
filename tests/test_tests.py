import unittest

from mplisp import evaluator


class TestSyntax(unittest.TestCase):

    def test_string(self):
        """test string"""
        input1 = """
        (def a \'str\')
        (assert-equal! a 'str')
        """

        output1 = evaluator.evaluate(input1, None, True)
        output2 = evaluator.evaluate(input1, None, False)

        self.assertEqual(list(output1), [None, None])
        self.assertEqual(list(output2), [None])
