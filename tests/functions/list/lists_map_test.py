import unittest
import mplisp.evaluator as evaluator


class TestListMap(unittest.TestCase):

    def map_test(self):
        input1 = """
        (map (lambda (x) (* 2 x)) (list 1 2 3))
        """

        output1 = list(evaluator.evaluate(input1))

        self.assertEqual(output1[0], [2, 4, 6])

    def map_test_2(self):
        input1 = """
        (import "sys")
        (def a (list 1 2 3 4))
        (map (lambda (x) (* 2 x)) a)
        """

        output1 = list(evaluator.evaluate(input1))
        self.assertEqual(output1[2], [2, 4, 6, 8])
