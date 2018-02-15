import unittest
import mplisp.evaluator as evaluator


class TestModuleImport(unittest.TestCase):

    def test_python_import(self):
        import sys
        """test string"""
        input1 = '(import "sys")'

        output1 = list(evaluator.evaluate(input1))

        self.assertEqual(type(output1[0]), type(sys))

    def test_python_apply(self):
        """test string"""
        input1 = '''
        (get-attribute "sys" "argv")
        '''

        output1 = list(evaluator.evaluate(input1))

        self.assertTrue(isinstance(output1[0], list))

    def test_import_mplisp(self):
        """test mplisp import"""
        input1 = '''
        (import "scripts/testlib")
        (nice-string "test")
        '''

        output1 = list(evaluator.evaluate(input1))
        self.assertEqual(output1[1], ">> test <<")

    def test_import_python_function(self):
        """test mplisp import"""
        input1 = '''
        (def os-mod (import "os"))
        ((get-attribute os-mod "getcwd"))
        '''

        output1 = list(evaluator.evaluate(input1))
        self.assertTrue("mplisp/tests" in output1[1])
