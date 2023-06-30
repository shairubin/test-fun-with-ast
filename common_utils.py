import ast
from typing import Union

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class CommonUtils:

    def compare_ast(self, node1: Union[ast.expr, list[ast.expr]], node2: Union[ast.expr, list[ast.expr]]) -> bool:
        if type(node1) is not type(node2):
            return False

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
