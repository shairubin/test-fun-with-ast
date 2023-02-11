import contextlib
import os
import subprocess

import pytest

from test_utils import TestUtils

class TestE2EASTUtils:

    @pytest.mark.parametrize("test_program, output_program", [('./../test_programs/fibonacci_test.py', '/tmp/test.py')])
    def test_rewriteIf_no_if1(self, test_program, output_program):
        with contextlib.suppress(FileNotFoundError):
            os.remove(output_program)
        test_utils = TestUtils()
        python_code = test_utils.read_file_as_string(test_program)
        print(python_code)
        import ast
        module_node = ast.parse(python_code)
        import source_match
        source_match.GetSource(module_node, python_code)
        assert python_code == module_node.matcher.GetSource()
