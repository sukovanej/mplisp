from typing import List
from . import env


class SyntaxTreeNode(object):
    def __init__(self, value: str, children: List,
                 parent, local_env: env.EnvNode = None):
        self.value = value
        self.children = children
        self.parent = parent
        self.local_env = local_env
        self.line = 0

    def append(self, value):
        node = SyntaxTreeNode(value, [], self)
        self.children.append(node)

        return node

    def getenv(self):
        obj = self

        while obj.local_env is None:
            obj = obj.parent

        return obj.local_env

    def __repr__(self, tab=' '):
        result = "(" + self.value + ")" + '\n'

        for child in self.children:
            result += tab + " -> " + child.__repr__(tab + ' ')

        return result
