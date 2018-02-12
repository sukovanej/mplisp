import unittest
import mplisp.evaluator as evaluator


class TestLambdaExpression(unittest.TestCase):

    def test_simple(self):
        """test string"""
        input1 = '((lambda (x) x) 1)'
        input2 = '((lambda (x) (+ x 1)) 1)'
        input3 = '(((lambda (x) x) +) 1 2)'

        output1 = list(evaluator.evaluate(input1))
        output2 = list(evaluator.evaluate(input2))
        output3 = list(evaluator.evaluate(input3))

        self.assertEqual(output1, [1])
        self.assertEqual(output2, [2])
        self.assertEqual(output3, [3])

    def test_factorial(self):
        input1 = """
        (def fact 
            (lambda (x)
                (if (> x 1)
                    (* x (fact (- x 1)))
                    1)))
        (fact 1)
        (fact 2)
        (fact 3)
        (fact 4)
        (fact 5)
        """

        output1 = list(evaluator.evaluate(input1))

        self.assertEqual(output1, [None, 1, 2, 6, 24, 120])

    def test_generator(self):
        input1 = """
        (def fc 
            (lambda (a)
                (lambda (x) (+ x a))))
                
        ((fc 1) 1)
        ((fc 2) 1)
        ((fc 1) 2)
        
        (def +2 (fc 2))
        (def +1 (fc 1))
        
        (+1 1)
        (+1 -2)
        (+2 -2)
        (+2 1)
        (+2 2)
        """

        output1 = list(evaluator.evaluate(input1))

        self.assertEqual(output1, [None, 2, 3, 3, None, None, 2, -1, 0, 3, 4])

    def test_generator_2(self):
        input1 = """
        (lambda (a) (lambda (x) (+ x a)))
        """

        output1 = list(evaluator.evaluate(input1))
