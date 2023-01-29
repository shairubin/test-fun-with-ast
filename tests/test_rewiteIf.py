import ast
import logging

import pytest

from RewriteIf import RewriteIf
from tests.test_utils import TestUtils


class TestRewtiteIf():
    simple_if_1 = """
if x == 5 or (y != 7 and z == 6): 
    print(simple_if_1) 
"""
    simple_if_1_logged = """
if x == 5 or (y != 7 and z == 6):
    logging.warn(f'  x is:{x} y is:{y} z is:{z} ')
    print(simple_if_1)
"""

    @pytest.mark.parametrize("prog_in, prog_out", [(simple_if_1, simple_if_1_logged)])
    def test_rewriteIf_no_if1(self, prog_in, prog_out):
        utils = TestUtils()
        parsed_tree_in = ast.parse(prog_in)
        parsed_tree_out = ast.parse(prog_out)
        logged_tree = RewriteIf().visit(parsed_tree_in)
        logging.info(f'{ast.unparse(parsed_tree_in)}')
        assert prog_out.strip() == ast.unparse(logged_tree).strip()
        assert utils.compare_ast(parsed_tree_in, parsed_tree_out) == True
