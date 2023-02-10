from _ast import Constant
from ast import NodeTransformer
from random import  randrange


class RewriteConstant(NodeTransformer):
    def visit_Constant(self, node):
        new_value = self._get_new_value(6)
        return Constant(value=new_value)

    def _get_new_value(self, old_value):
        return randrange(old_value+10,old_value+20)