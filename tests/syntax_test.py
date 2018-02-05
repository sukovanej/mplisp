import unittest
import mplisp.syntax as syntax


class TestSyntax(unittest.TestCase):

    def test_string(self):
        """test string"""
        input1 = '(def a \'str\')'
        input2 = '(def a \"str\")'

        output1 = syntax.create_tree(input1)
        output2 = syntax.create_tree(input2)

        self.assertEqual(output1.children[0].children[2].value, '\'str\'')
        self.assertEqual(output2.children[0].children[2].value, '\"str\"')
