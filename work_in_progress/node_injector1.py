import ast
import json
import sys
import uuid

import requests
from fun_with_ast.manipulate_node.get_node_from_input import GetNodeFromInput
from fun_with_ast.source_matchers.matcher_resolver import GetDynamicMatcher

from djangoproject.settings import STRUDEL_LOG_UNIQUE_IDENTIFIER, TEMPLATES_URI
from log_manager.node_metadata import NodeMetadata
from utils.strudel_utils import ast_to_dict


class NodeInjector:

#    def _get_source_code_to_add(self):
#        raise NotImplementedError('abstract method')

    def _get_source_code_to_add(self, node):
        for index, line in enumerate(lines):
            source_to_add += line + self.source_suffix.removesuffix('\n') + f'_{index}' + '\n'
        return source_to_add




    # # this is co-pilot code -- nice
    # def _replace_ellipsis(self, if_dict, back=False):
    #     if back:
    #         search = 'Ellipsis'
    #         replace = Ellipsis
    #     else:
    #         search = Ellipsis
    #         replace = 'Ellipsis'
    #     for key, value in if_dict.items():
    #         if value == search:
    #             if_dict[key] = replace
    #         elif isinstance(value, dict):
    #             if_dict[key] = self._replace_ellipsis(value)
    #         elif isinstance(value, list):
    #             if_dict[key] = [self._replace_ellipsis(x) for x in value]
    #     return if_dict
    #
