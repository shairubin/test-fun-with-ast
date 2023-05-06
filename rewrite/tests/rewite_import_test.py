from fun_with_ast.get_source import GetSource

from rewrite.RewriteImports import RewriteImports
import ast


class TestImportRewrite:

    def test_simple_import_rewrite(self):
        python_code = "a = 1"
        module_node = self.__rewrite_imports(python_code, ['logging'])
        FunWithAst_code = module_node.matcher.GetSource()
        assert 'import logging\n'+python_code == FunWithAst_code
        assert python_code != FunWithAst_code

    def test_simple_no_logging_import_rewrite(self):
        python_code = "a = 1"
        module_node = self.__rewrite_imports(python_code, ['re', 're'])
        FunWithAst_code = module_node.matcher.GetSource()
        assert 'import re\n'+python_code == FunWithAst_code
        assert python_code != FunWithAst_code

    def test_simple_import_no_rewrite(self):
        python_code = "import logging\na = 1"
        module_node = self.__rewrite_imports(python_code, ['logging'])
        FunWithAst_code = module_node.matcher.GetSource()
        assert python_code == FunWithAst_code

    def test_simple_import_partial_no_rewrite(self):
        python_code = "import logging\na = 1"
        module_node = self.__rewrite_imports(python_code, ['logging', 're'])
        FunWithAst_code = module_node.matcher.GetSource()
        assert 'import re\n'+python_code == FunWithAst_code

    def test_import_in_non_module_scope(self):
        python_code = "for i in [1,2,3]:\n   import logging\n   a = 1\n   import re\n"
        module_node = self.__rewrite_imports(python_code, ['re', 'logging'])
        FunWithAst_code = module_node.matcher.GetSource()
        assert 'import re\nimport logging\n'+python_code == FunWithAst_code

    def test_import_not_in_start_of_module(self):
        python_code = "import logging\nfor i in [1,2,3]:\n   import logging\n   a = 1\nimport re\n"
        module_node = self.__rewrite_imports(python_code, ['re', 'logging'])
        FunWithAst_code = module_node.matcher.GetSource()
        assert 'import re\n'+python_code == FunWithAst_code

    def __rewrite_imports(self, python_code, list_of_imports):
        module_node = ast.parse(python_code)
        GetSource(module_node, python_code)
        rewrite_imports = RewriteImports(list_of_imports)
        rewrite_imports.visit(module_node)
        ast.fix_missing_locations(module_node)
        return module_node

