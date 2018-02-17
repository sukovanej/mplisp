import unittest
import mplisp.syntax as syntax


class TestSyntax(unittest.TestCase):

    def test_string(self):
        """test string"""
        input1 = '(def a \'str\')'
        input2 = '(def a \"str\")'
        input3 = '\'str\''

        output1 = syntax.create_tree(input1)
        output2 = syntax.create_tree(input2)
        output3 = syntax.create_tree(input3)

        self.assertEqual(output1.children[0].children[2].value, '\'str\'')
        self.assertEqual(output2.children[0].children[2].value, '\"str\"')
        self.assertEqual(output3.children[0].value, '\'str\'')

    def test_quote(self):
        input1 = '`ahoj'
        input2 = '`1'
        input3 = '`(1 2)'
        input4 = '`((1 2) 1)'

        output1 = syntax.create_tree(input1)
        output2 = syntax.create_tree(input2)
        output3 = syntax.create_tree(input3)
        output4 = syntax.create_tree(input4)

        self.assertEqual(output1.children[0].children[0].value, 'quote')
        self.assertEqual(output2.children[0].children[0].value, 'quote')
        self.assertEqual(output3.children[0].children[0].value, 'quote')
        self.assertEqual(output4.children[0].children[0].value, 'quote')

        self.assertEqual(output1.children[0].children[1].value, 'ahoj')
        self.assertEqual(output2.children[0].children[1].value, '1')

        self.assertEqual(output3.children[0].children[1].children[0].value, '1')
        self.assertEqual(output3.children[0].children[1].children[1].value, '2')

        self.assertEqual(output4.children[0].children[1].children[0].children[0].value, '1')
        self.assertEqual(output4.children[0].children[1].children[0].children[1].value, '2')
        self.assertEqual(output4.children[0].children[1].children[1].value, '1')

    def test_quote_advanced(self):
        input1 = "(== l `(1 2) 1 2)"

        output1 = syntax.create_tree(input1)

        self.assertEqual(output1.children[0].children[2].children[0].value, 'quote')
        self.assertEqual(output1.children[0].children[0].value, '==')
        self.assertEqual(output1.children[0].children[1].value, 'l')
        self.assertEqual(output1.children[0].children[3].value, '1')
        self.assertEqual(output1.children[0].children[4].value, '2')
