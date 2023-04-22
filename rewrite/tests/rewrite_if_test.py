import difflib
from pprint import pprint

from rewrite.RewriteIf import RewriteIf, IfRewrtiteConfig
from rewrite.RewriteImports import RewriteImports
import ast
from fun_with_ast import source_match


class TestImportRewrite:

    def test_simple_if_rewrite(self):
        python_code = "if True:\n    a = 1"
        module_node = self.__rewrite_if(python_code, IfRewrtiteConfig('test string'))
        FunWithAst_code = module_node.body[0].matcher.GetSource()
        lines_original_python = set(python_code.splitlines())
        lines_fun_with_ast = set(FunWithAst_code.splitlines())
        diff_lines = lines_fun_with_ast - lines_original_python
        assert(len(diff_lines)) ==1
        assert diff_lines.pop() == '    logger.info(\'test string\')'

    def __rewrite_if(self, python_code, config):
        module_node = ast.parse(python_code)
        source_match.GetSource(module_node, python_code)
        rewrite_if = RewriteIf(config)
        rewrite_if.visit(module_node)
        return module_node
