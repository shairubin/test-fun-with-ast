from _ast import Constant
from ast import NodeTransformer
from random import  randrange


class RewriteIf(NodeTransformer):
    def visit_If(self, node):
        raise
