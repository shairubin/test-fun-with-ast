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
    def __init__(self, source_node_metadata: NodeMetadata):
        self.node = source_node_metadata.ast_node
        self.node_parent = source_node_metadata.parent
        self.node_metadata = source_node_metadata
        self.source_suffix = ' # ' + STRUDEL_LOG_UNIQUE_IDENTIFIER + '\n'
        self.manipulator = None
    def add_source_to_node(self):
        node_to_add, source_to_add = self._get_node_to_inject()
        self.node.node_matcher.GetSource() # TODO need to put in debug
        self.manipulator.add_nodes(node_to_add.body)
        new_code = self.node.node_matcher.GetSource()
        self.node_metadata.code_after_log_injection = new_code
        self.node_metadata.added_code = source_to_add
        return new_code

    def _get_node_to_inject(self):
        source_to_add = self._get_source_code_to_add(self.node)
        try:
            ast.parse(source_to_add) #TODO debug
        except Exception as e:
            raise Exception(f'Error in parsing source_to_add: {e}')
        node_to_add = GetNodeFromInput(source_to_add, get_module=True)
        matcher = GetDynamicMatcher(node_to_add)
        matcher.do_match(source_to_add)
        return node_to_add, source_to_add

#    def _get_source_code_to_add(self):
#        raise NotImplementedError('abstract method')

    def _get_source_code_to_add(self, node):
        raw_source = self._get_raw_source_to_add(node) # must be implemented by subclass
        lines = raw_source
        source_to_add = ''
        for index, line in enumerate(lines):
            source_to_add += line + self.source_suffix.removesuffix('\n') + f'_{index}' + '\n'
        return source_to_add



    def _access_placement_service(self, node_dict):
        try:
            templates_uri = f'http://{TEMPLATES_URI}/templates/get_placements'
            if_json = json.dumps(node_dict)
        except Exception as e:
            if str(e) == 'Object of type ellipsis is not JSON serializable':
                node_dict = self._replace_ellipsis(node_dict)
                if_json = json.dumps(node_dict)
            else:
                raise e
        try:
            headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
            response = requests.post(templates_uri, json=if_json, headers=headers)
        except Exception as e:
            raise e
        if response.status_code != 200:
            raise Exception(f'Error in getting placements: {response.text}')
        return response
    #
    def _fill_if_template(self, node, root_type):
        if_dict = ast_to_dict(node)
        if_dict['context']["root_node"] = root_type
        if_dict["_id"] = str(uuid.uuid4())
        if_dict["language"] = sys.version
        return if_dict

    def _replace_ellipsis(self, node_dict, back=False):
        if back:
            search = 'Ellipsis'
            replace = Ellipsis
        else:
            search = Ellipsis
            replace = 'Ellipsis'
        if not isinstance(node_dict, list) and not isinstance(node_dict, dict):
            if node_dict == search:
                return replace
            else:
                return node_dict
        for key, value in node_dict.items():
            if isinstance(value, dict):
                node_dict[key] = self._replace_ellipsis(value)
            elif isinstance(value, list):
                if value:
                    node_dict[key] = [self._replace_ellipsis(x) for x in value]
                else:
                    node_dict[key] = [self._replace_ellipsis(x) for x in value]
            else:
                node_dict[key] = self._replace_ellipsis(value)
        return node_dict


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
