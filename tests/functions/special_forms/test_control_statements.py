import unittest
import mplisp.evaluator as evaluator


class TestControlStatements(unittest.TestCase):

    def test_python_import(self):
        """test string"""
        input1 = '(or? 1 2 3)'
        input2 = '(or? #t #f)'
        input3 = '(or? #f #f)'

        output1 = list(evaluator.evaluate(input1))
        output2 = list(evaluator.evaluate(input2))
        output3 = list(evaluator.evaluate(input3))

        self.assertEqual(output1[0], True)
        self.assertEqual(output2[0], True)
        self.assertEqual(output3[0], False)
