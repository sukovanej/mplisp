import unittest
import mplisp.evaluator as evaluator


class TestDefine(unittest.TestCase):

    def test_define_list_length_implementation(self):
        """test string"""
        input1 = """
        (def list-len
            (lambda (l)
                (if (== l `()) 0
                    (apply + (map (lambda (x) 1) l)))))
        
        (list-len `(1 2 3 4))
        """

        output1 = list(evaluator.evaluate(input1))
        self.assertEqual(output1, [None, 4])

