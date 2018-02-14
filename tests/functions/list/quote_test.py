import unittest
import mplisp.evaluator as evaluator


class TestQuote(unittest.TestCase):

    def simple_test(self):
        input1 = """
        `(1 2 3)
        """

        output1 = list(evaluator.evaluate(input1))

        print(output1)

        self.assertEqual(output1[0], [2, 4, 6])
