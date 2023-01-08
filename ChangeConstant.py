from _ast import Constant
from ast import NodeTransformer
from typing import Any



class RewriteConstant(NodeTransformer):
    def visit_Constant(self, node):
        return Constant(value=6)