import ast
from ast import NodeTransformer


class RewriteImports(NodeTransformer):

    def visit_Module(self, node) :
        if self.__is_logging_missing(node):
            self.__add_logging_import(node)
        return node
    def __add_logging_import(self, node):
        raise NotImplementedError

    def __is_logging_missing(self, node):
        for node in node.body:
            if isinstance(node, ast.Import) :
                for import_instance in node.names:
                    if import_instance.name == 'logging':
                        return False
        return True