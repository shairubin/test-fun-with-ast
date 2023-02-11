import ast
from itertools import zip_longest
from typing import Union


class TestUtils:

    def compare_ast(self, node1: Union[ast.expr, list[ast.expr]], node2: Union[ast.expr, list[ast.expr]]) -> bool:
        if type(node1) is not type(node2):
            return False

#        print("node1: ", node1)
#        print("node2: ", node2)
        if isinstance(node1, ast.AST):
            for k, v in vars(node1).items():
                if k in {"lineno", "end_lineno", "col_offset", "end_col_offset", "ctx"}:
                    continue
                if not self.compare_ast(v, getattr(node2, k)):
#                    print("v:    ", v)
#                    print(f'node2, k={k}: ', getattr(node2, k))
                    return False
            return True

        elif isinstance(node1, list) and isinstance(node2, list):
            return all(self.compare_ast(n1, n2) for n1, n2 in zip_longest(node1, node2))
        else:
            result = (node1 == node2)
            return result

    def read_file_as_string(self, test_program):
        text_file = open(test_program, 'r')
        python_string = text_file.read()
        text_file.close()
        return python_string
