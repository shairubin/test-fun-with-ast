
import pytest
from fun_with_ast import source_match
from test_utils import TestUtils


@pytest.fixture(scope="module",
#                params=['./../test_programs/find_largest_number.py', './../test_programs/simple_print.py'])
                params=[
                        './test_programs/simple_module.py',
                        './test_programs/simple_module2.py', \
                        './test_programs/simple_module3.py', \
                        './test_programs/simple_module_assignment.py', \
                        './test_programs/match_comment_eol.py', \
                        './test_programs/simple_module.py'
                        ])
def test_program(request):
    yield request.param


class TestE2EASTUtils:

    def test_simple_ast_utils(self, test_program):
        test_utils = TestUtils()
        python_code = test_utils.read_file_as_string(test_program)
        import ast
        module_node = ast.parse(python_code)
        source_match.GetSource(module_node, python_code)
        FunWithAst_code = module_node.matcher.GetSource()
        assert python_code == FunWithAst_code
