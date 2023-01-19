import ast
from ast import NodeTransformer


class RewriteIf(NodeTransformer):
    def visit_If(self, node):
        unparsted_if_node = ast.unparse(node.test)
        print("visited if node. Test is: "+ unparsted_if_node)
        node.body.append(self._add_log_to_if_body(node, unparsted_if_node))
        result = self.generic_visit(node)
        print('finish visit if node')
        return result

    def _add_log_to_if_body(self, if_node, text):
#        return if_node.body[0]
        func_name = ast.Name(id='my_function', ctx=ast.Load())
        args = [ast.Num(n=1), ast.Str(s='my function inserted')]
        call = ast.Call(func=func_name, args=args, keywords=[])
        result = ast.Expr(value=call)
        return result