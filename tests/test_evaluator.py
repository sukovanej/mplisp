import unittest
import mplisp.evaluator as evaluator


class TestEvaluator(unittest.TestCase):

    def test_string(self):
        """test string"""
        input1 = '\'str\''
        input2 = '\"str\"'
        input3 = '(def s \'ahoj\')\n(== s \'ahoj\')'
        input4 = '(def s \'ahoj\')\ns'

        output1 = list(evaluator.evaluate(input1))
        output2 = list(evaluator.evaluate(input2))
        output3 = list(evaluator.evaluate(input3))
        output4 = list(evaluator.evaluate(input4))

        self.assertEqual(output1, ['str'])
        self.assertEqual(output2, ['str'])
        self.assertEqual(output3, [None, True])
        self.assertEqual(output4, [None, 'ahoj'])
