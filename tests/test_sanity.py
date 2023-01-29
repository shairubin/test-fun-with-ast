

import pytest
import logging

from tests.test_utils import TestUtils

logger = logging.getLogger()
from RewriteIf import RewriteIf
from my_main import simple_parse_example



class TestBasicSanity():
    input1 = "x+5"
    input2 = "x+6"
    input3 = """ 
def datetime_cast_date_sql(self, sql, params, tzname): 
    sql, params = self._convert_sql_to_tz(sql, params, tzname) 
    return f"DATE({sql})", params
"""
    @pytest.fixture
    def input_value1(self):
        return TestBasicSanity.input1


    @pytest.fixture
    def input_value2(self):
        return TestBasicSanity.input2

    @pytest.fixture
    def input_value3(self):
        return TestBasicSanity.input3

    @pytest.mark.parametrize("input", [input1 , input2, input3])
    def test_rewriteIf_no_if1(self, input):
        self._parse_rewrite_compare(input)

    def _parse_rewrite_compare(self, input_value1):
        utils = TestUtils()
        logger.info(f'input value: {input_value1}')
        parsed_tree = simple_parse_example(input_value1)
        rewrite_tree = RewriteIf().visit(parsed_tree)
        assert utils.compare_ast(parsed_tree, rewrite_tree) == True

    @pytest.mark.parametrize("tree1, tree2", [(input1, input2) , (input1,input3), (input2, input3)])
    def test_rewriteIf_no_if_two_trees(self, tree1, tree2):
        utils = TestUtils()
        logger.info(f'input value: {tree1}, {tree2}')
        parsed_tree1 = simple_parse_example(tree1)
        parsed_tree2 = simple_parse_example(tree2)
        assert  utils.compare_ast(parsed_tree1, parsed_tree2) == False
        assert  utils.compare_ast(parsed_tree1, parsed_tree1) == True
        assert  utils.compare_ast(parsed_tree2, parsed_tree2) == True

        rewrite_tree1 = RewriteIf().visit(parsed_tree1)
        rewrite_tree2 = RewriteIf().visit(parsed_tree2)
        assert  utils.compare_ast(parsed_tree1, rewrite_tree1) == True
        assert  utils.compare_ast(parsed_tree2, rewrite_tree2) == True
        assert  utils.compare_ast(parsed_tree2, rewrite_tree1) == False
