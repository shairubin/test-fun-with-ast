import ast
from ast import NodeTransformer

from fun_with_ast import source_match
from fun_with_ast.create_node import GetNodeFromInput


class RewriteImports(NodeTransformer):
    def __init__(self, imports):
        super(NodeTransformer, self).__init__()
        self._imports = sorted(set(imports), key=str)

    def visit_Module(self, node, *args):
        exising_imports = self.__get_existing_imports(node)
        for imp in self._imports:
            if imp not in exising_imports:
                self.__add_import(node, imp)
        return node
    def __add_import(self, node, _import):
        import_node = GetNodeFromInput(f'import {_import}')
        source_match.GetSource(import_node, f'import {_import}\n')
        node.body.insert(0, import_node)

    def __get_existing_imports(self, node):
        existing_imports = set()
        for node in node.body:
            if isinstance(node, ast.Import):
                for import_instance in node.names:
                    existing_imports.add(import_instance.name)
            else:
                break
        return existing_imports
