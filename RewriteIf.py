import ast
from ast import NodeTransformer




class RewriteIf(NodeTransformer):
    def visit_If(self, node):
        unparsted_if_node = ast.unparse(node.test)
        print("visited if node. Test is: "+ unparsted_if_node)
        self._add_logs_to_if_node(node)
        result = self.generic_visit(node)
        print('finish visit if node')
        return result

    def _add_logs_to_if_node(self, if_node):
        log_string = self.__get_string_from_if_condition(if_node.test)
        body_result = self.__add_log_to_body(if_node.body, log_string)
        if_node.body.append(body_result)
        orelse_result = self.__add_log_to_orelse(if_node.orelse  , log_string)
        if_node.orelse.append(orelse_result)

    def __add_log_to_body(self, body_node, condition_string):
        if body_node:
            result = self.__generate_log_line('body_part '+condition_string)
        else:
            raise NotImplementedError
        return result

    def __add_log_to_orelse(self, orelse_node, condition_string):
        if orelse_node:
            result = self.__generate_log_line('oresle part '+condition_string)
        else:
            result = []
        return result

    def __generate_log_line(self, condition_string):
        func_name = ast.Name(id='log_a_line', ctx=ast.Load())
        args = [ast.Str(s=condition_string)]
        call = ast.Call(func=func_name, args=args, keywords=[])
        result = ast.Expr(value=call)
        return result

    def __get_string_from_if_condition(self, if_condition):
        nodes = [node for node in ast.walk(if_condition)]
        ids = []
        result = ''
        for node in nodes:
            unparsed_node = ast.unparse(node)
            if isinstance(node, ast.Name):
                ids.append(node.id)
            #print(unparsed_node)
        if not ids:
            raise NotImplementedError
        for variable in ids:
            result += ' '+ variable + ' is:' + '{' + variable +'}'
        return result