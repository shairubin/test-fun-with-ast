import ast
from ast import NodeTransformer
import logging
from dataclasses import dataclass

from fun_with_ast import source_match
from fun_with_ast.create_node import GetNodeFromInput
from fun_with_ast.get_source import GetSource

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)

@dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False)
class IfRewrtiteConfig():
    _body_fix_log: str = 'Log for If body'
    _else_fix_log: str = 'Log for If else'
    _body_condition_log: bool = False
    _else_condition_log: bool = False

    def __post_init__(self):
        if self._body_condition_log:
            self._body_fix_log = ''

    @property
    def body_fixed_log(self):
        return self._body_fix_log

    @property
    def body_condition_log(self):
        return self._body_condition_log

class RewriteIf(NodeTransformer):
    def __init__(self, if_config):
        super(NodeTransformer, self).__init__()
        self._if_config = if_config


    def visit_If(self, node):
        self._add_logs_to_if_node(node)
        result = self.generic_visit(node)
        return result

    def _add_logs_to_if_node(self, if_node):
        if if_node.body:
            body_result = self.__get_log_nodes(if_node)
            if_node.body.insert(0,body_result)
        if if_node.orelse:
            orelse_result = self.__get_log_nodes(if_node)
            if_node.orelse.insert(0,orelse_result)

    def __get_log_nodes(self, if_node):
        result = self.__generate_log_node(if_node)
        return result


    def __generate_log_node(self, if_node):
        if self._if_config.body_fixed_log:
            return self.__generate_fixed_log_node_for_body(if_node)
        elif self._if_config.body_condition_log:
            return self.__generate_condition_log_node_for_body(if_node)
        else:
            raise NotImplementedError

    def __get_ident(self, if_node):
        if if_node.__getattribute__('orelse'):
            raise NotImplementedError
        body = if_node.body
        ident = self.__find_ident(body)
        return ident

    def __find_ident(self, body):
        ident = 0
        for stmt in body:
            stmt_ident = stmt.col_offset
            if stmt_ident > ident and ident == 0:
                ident = stmt_ident
            elif stmt_ident > ident and ident != 0:
                raise ValueError('illegal ident')
        return ident

    def __generate_fixed_log_node_for_body(self, if_node):
        ident = ' '*self.__get_ident(if_node)
        log_line = f'logger.info(\'{self._if_config.body_fixed_log}\')\n'
        log_node = GetNodeFromInput(log_line)
        GetSource(log_node, ident+log_line)
        return log_node

    def __generate_condition_log_node_for_body(self, if_node):
        formatted_string = self.__get_log_formated_string(if_node.test)
        ident = ' '*self.__get_ident(if_node)
        log_line = f'logger.info(\'Condition in body log is: {formatted_string}\')\n'
        log_node = GetNodeFromInput(log_line)
        GetSource(log_node, ident+log_line)
        return log_node

        return  formatted_string

    def __get_log_formated_string(self, if_condition):
        if isinstance(if_condition, ast.Compare):
            return self.__handle_compare(if_condition)
        elif isinstance(if_condition, ast.BoolOp):
            return self.__handle_boolop(if_condition)
        elif isinstance(if_condition, ast.Call):
            return self.__handle_call(if_condition)
        elif isinstance(if_condition, ast.Name):
            return ''+ f'{if_condition.id}' + ''
        elif isinstance(if_condition, ast.Constant):
            return str(if_condition.value)
        else:
            raise NotImplementedError

    def __get_JoinedStr_node(self, formated_string):
        result_string = 'f\" ' + formated_string + ' \"'
        result = ast.parse(result_string)
        logger.info(ast.unparse(result))
        return [result.body[0].value]

    def __handle_compare(self, compare_node):
        if len(compare_node.ops) == 1:
            left =  self.__get_log_formated_string(compare_node.left)
        else:
            raise NotImplementedError
        if len(compare_node.comparators) == 1:
            comperators =  self.__get_log_formated_string(compare_node.comparators[0])
        else:
            raise NotImplementedError
        op_str = self.__ops_to_string(compare_node.ops[0])
        result =  left + op_str + comperators
        return result
    def __handle_call(self, call_node):
        args = ''
        for arg in call_node.args:
            args+= " "+self.__get_log_formated_string(arg)
        result =  "called " + call_node.func.id + " with args: "+args
        return result

    def __handle_boolop(self, boolop_node):
        if len(boolop_node.values) == 2:
            left =  self.__get_log_formated_string(boolop_node.values[0])
            right = self.__get_log_formated_string(boolop_node.values[1])
        else:
            raise NotImplementedError
        result =  left + " BoolOp " + right
        return result

    def __ops_to_string(self, ast_op):
        if isinstance(ast_op, ast.Eq):
            return '='
        elif isinstance(ast_op, ast.NotEq):
            return '!='
        elif isinstance(ast_op, ast.GtE):
            return '>='
        else:
            raise NotImplementedError


