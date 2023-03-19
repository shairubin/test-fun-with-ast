import contextlib
import os
import subprocess

import pytest

from test_utils import TestUtils


@pytest.fixture(scope="module",
#                params=['./../test_programs/find_largest_number.py', './../test_programs/simple_print.py'])
                params=['./../test_programs/simple_module.py', './../test_programs/simple_module2.py'])
def test_program(request):
    yield request.param


class TestE2EASTUtils:

    def test_simple_ast_utils(self, test_program):
        test_utils = TestUtils()
        python_code = test_utils.read_file_as_string(test_program)
        import ast
        module_node = ast.parse(python_code)
        import source_match
        source_match.GetSource(module_node, python_code)
        FunWithAst_code = module_node.matcher.GetSource()
        assert python_code == FunWithAst_code
        print('source from matcher')
        print(module_node.matcher.GetSource())
