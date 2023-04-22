from rewrite.RewriteIf import RewriteIf, IfRewrtiteAction
from rewrite.RewriteImports import RewriteImports
import ast
from fun_with_ast import source_match


class TestImportRewrite:

    def test_simple_if_rewrite(self):
        python_code = "if True:\n    a = 1"
        module_node = self.__rewrite_if(python_code, IfRewrtiteAction.LOG_IF_BODY)
        l2_source=module_node.body[0].body[2].matcher.GetSource()
        l1_source=module_node.body[0].body[1].matcher.GetSource()
        l0_source=module_node.body[0].body[0].matcher.GetSource()
        FunWithAst_code = module_node.body[0].matcher.GetSource()

        #        FunWithAst_code = module_node.matcher.GetSource()
        assert python_code == FunWithAst_code

    def __rewrite_if(self, python_code, action):
        module_node = ast.parse(python_code)
        source_match.GetSource(module_node, python_code)
        rewrite_if = RewriteIf(action)
        rewrite_if.visit(module_node)
        rewrite_if_fixed = ast.fix_missing_locations(module_node)
        return module_node
