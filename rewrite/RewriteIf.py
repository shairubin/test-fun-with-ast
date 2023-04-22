import ast
from ast import NodeTransformer
import logging

from fun_with_ast import source_match
from fun_with_ast.create_node import GetNodeFromInput
from fun_with_ast.dynamic_matcher import GetDynamicMatcher

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)
from enum import auto, Flag


class IfRewrtiteAction(Flag):
    LOG_IF_BODY = auto()

class RewriteIf(NodeTransformer):
    def __init__(self, if_action):
        super(NodeTransformer, self).__init__()
        self._if_action = if_action

    def visit_If(self, node):
#        unparsted_if_node = ast.unparse(node.test)
#        logging.info("visited if node. Test is: "+ unparsted_if_node)
        self._add_logs_to_if_node(node)
        result = self.generic_visit(node)
#        logging.info("finish if node. Test is: "+ unparsted_if_node)
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
        formated_string  = self.__get_log_formated_string(if_node.test)
        join_Str_string = 'f\" ' + formated_string + ' \"'
        log_node = GetNodeFromInput('logger.info(\'test string\')\n')
        #matcher = GetDynamicMatcher(log_node)
        #matcher.Match('logger.info(\'test string\')')
        source = source_match.GetSource(log_node, 'logger.info(\'test string\')\n')

#        log_func = ast.Attribute(value=ast.Name(id='logging', ctx=ast.Load()),
#                                 attr='info',
#                                 ctx=ast.Load())
        #JoinedStr_node = self.__get_JoinedStr_node(formatted_string)
#        args = JoinedStr_node
#        call = ast.Call(func=log_func, args=args, keywords=[])
#        result = ast.Expr(value=call)
        return log_node

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
