import pytest

from rewrite.RewriteImports import RewriteImports
import ast
import source_match


class TestImportRewrite:

    def test_simple_import(self):
        python_code = "a = 1"
        module_node = ast.parse(python_code)
        source_match.GetSource(module_node, python_code)
        RewriteImports().visit(module_node)
        ast.fix_missing_locations(module_node)
        FunWithAst_code = module_node.matcher.GetSource()
        assert 'import logging\n'+python_code == FunWithAst_code
