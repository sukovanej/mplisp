from typing import List
from . import env

class SyntaxTreeNode(object):
    def __init__(self, value: str, children: List, 
                 parent, local_env: env.EnvNode = None):
        self.value = value
        self.children = children
        self.parent = parent

        if local_env is None:
            self.local_env = env.EnvNode({})
        else:
            self.local_env = local_env

    def append(self, value):
        node = SyntaxTreeNode(value, [], self)
        self.children.append(node)

        return node

    def __repr__(self, tab = ' '):
        result = "(" + self.value + ")" + '\n'

        for ch in self.children:
            result += tab + " -> " + ch.__repr__(tab + ' ')

        return result