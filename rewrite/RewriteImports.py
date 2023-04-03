import ast
from ast import NodeTransformer

import source_match
from tests.create_node_test import GetNodeFromInput


class RewriteImports(NodeTransformer):

    def visit_Module(self, node) :
        if self.__is_logging_missing(node):
            self.__add_logging_import(node)
        return node
    def __add_logging_import(self, node):
        import_logging = GetNodeFromInput("import logging")
        source_match.GetSource(import_logging, 'import logging\n')
        node.body.insert(0, import_logging)

    def __is_logging_missing(self, node):
        for node in node.body:
            if isinstance(node, ast.Import) :
                for import_instance in node.names:
                    if import_instance.name == 'logging':
                        return False
        return True
