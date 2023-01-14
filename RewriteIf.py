import ast
from _ast import Constant
from ast import NodeTransformer
from random import  randrange


class RewriteIf(NodeTransformer):
    def visit_If(self, node):
        print("visited if node")
        node.body.append(node.body[0])
        result = ast.NodeVisitor.generic_visit(self, node)
        print('finish visit if node')
        return result

