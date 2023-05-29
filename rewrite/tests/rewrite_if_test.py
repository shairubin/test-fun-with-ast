import ast

import pytest
from fun_with_ast.get_source import GetSource
from fun_with_ast.manipulate_node.create_node import GetNodeFromInput
from fun_with_ast.manipulate_node.if_manipulator import ManipulateIfNode, IfManipulatorConfig
from fun_with_ast.source_matchers.matcher_resolver import GetDynamicMatcher

from rewrite.RewriteIf import RewriteIf, IfRewrtiteConfig


@pytest.fixture(
                params=[
                        ["if True:\n    a = 1", "logger.info(\'Log for If body\')"],
                        ["if a:\n    a = 1", "    logger.info(\'Log for If body\')"],
                        ["if a:\n    a = 1\n    return False", "    logger.info(\'Log for If body\')"]
                        ])
def test_fixed_body_params(request):
    yield request.param

@pytest.fixture(
                params=[
                        ["if True:\n    a = 1", "    logger.info('Condition in body log is: True')"],
                        ["if a==2:\n    a = 1", "    logger.info('Condition in body log is: a=2')"],
                ])
def test_condition_body_params(request):
    yield request.param

class TestImportRewrite:

    def test_fixed_if_rewrite(self, test_fixed_body_params):
        original_if_source = test_fixed_body_params[0]
        if_node = GetNodeFromInput(original_if_source)
        if_node_matcher = GetDynamicMatcher(if_node)
        if_node_matcher.Match(original_if_source)
        node_to_add = GetNodeFromInput(test_fixed_body_params[1])
        if_manipulator = ManipulateIfNode(if_node)
        if_manipulator.add_nodes([node_to_add], IfManipulatorConfig(body_index=0, location_in_body_index=0))
        new_code = if_node_matcher.GetSource()
        print(new_code)
    def test_condition_if_rewrite(self, test_condition_body_params):
        python_code = test_condition_body_params[0]
        module_node = self.__rewrite_if(python_code, IfRewrtiteConfig(_body_condition_log=True))
        expected_string = test_condition_body_params[1]
        self._verify_rewrite(expected_string, module_node, python_code)


    def test_simple_if_else_rewrite(self):
        python_code = "if True:\n    a = 1\nelse:\n    a = 2"
        module_node = self.__rewrite_if(python_code, IfRewrtiteConfig())
        self._verify_rewrite('    logger.info(\'test string\')', module_node, python_code)

    def _rewrite_if(self, python_code, config):
        module_node = ast.parse(python_code)
        GetSource(module_node, python_code)
        rewrite_if = RewriteIf(config)
        rewrite_if.visit(module_node)
        return module_node

    def _verify_rewrite(self, expected_string, module_node, python_code):
        FunWithAst_code = module_node.body[0].matcher.GetSource()
        lines_original_python = set(python_code.splitlines())
        lines_fun_with_ast = set(FunWithAst_code.splitlines())
        diff_lines = lines_fun_with_ast - lines_original_python
        assert (len(diff_lines)) == 1
        assert diff_lines.pop() == expected_string
