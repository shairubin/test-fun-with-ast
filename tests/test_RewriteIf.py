

import pytest
import logging

from tests.test_utils import TestUtils

logger = logging.getLogger()
from RewriteIf import RewriteIf
from my_main import simple_parse_example

class TestBasicReWrite():
    @pytest.fixture
    def input_value(self):
        return "x+5"

    def test_rewriteIf_no_if(self, input_value):
        utils = TestUtils()
        logger.info(f'input value: {input_value}')
        parsed_tree = simple_parse_example(input_value)
        rewrite_tree = RewriteIf().visit(parsed_tree)
        assert  utils.compare_ast(parsed_tree, rewrite_tree) == True
