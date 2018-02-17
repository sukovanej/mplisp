import unittest

from mplisp.structures import tree
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

    def test_quote_advanced_2(self):
        input1 = "(== l `(1 2) 1 2)"
        input2 = "(`() `(1 2) (`()))"
        input3 = "(`())"
        input4 = "(`(() ()))"
        input5 = "`ahoj"
        input6 = "(`ahoj)"

        output1 = syntax.create_tree(input1)
        output2 = syntax.create_tree(input2)
        output3 = syntax.create_tree(input3)
        output4 = syntax.create_tree(input4)
        output5 = syntax.create_tree(input5)
        output6 = syntax.create_tree(input6)

        self.assertEqual(self.list_repr(output1)[0], ["==", "l", ["quote", ["1", "2"]], "1", "2"])
        self.assertEqual(self.list_repr(output2)[0], [["quote", []], ["quote", ["1", "2"]], [["quote", []]]])
        self.assertEqual(self.list_repr(output3)[0], [["quote", []]])
        self.assertEqual(self.list_repr(output4)[0], [["quote", [[], []]]])
        self.assertEqual(self.list_repr(output5)[0], ["quote", "ahoj"])
        self.assertEqual(self.list_repr(output6)[0], [["quote", "ahoj"]])

    def list_repr(self, node: tree.SyntaxTreeNode):
        if node.value:
            return node.value

        result = []
        for node in node.children:
            result.append(self.list_repr(node))

        return result
