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
        if if_node.body:
            body_result = self.__get_log_nodes(if_node)
            if_node.body.insert(0,body_result)
        if if_node.orelse:
            orelse_result = self.__get_log_nodes(if_node)
            if_node.orelse.insert(0,orelse_result)

    def __get_log_nodes(self, if_node):
        result = self.__generate_log_node(if_node)
        return result

    # def __add_log_to_orelse(self, orelse_node, formated_string_node):
    #     if orelse_node:
    #         result = self.__generate_log_line(formated_string_node)
    #     else:
    #         result = []
    #     return result

    def __generate_log_node(self, if_node):
        log_func = ast.Attribute(value=ast.Name(id='logging', ctx=ast.Load()),
                                 attr='warn',
                                 ctx=ast.Load())
        JoinedStr_node = self.__get_JoinedStr_node(if_node.test)
        args = JoinedStr_node
        call = ast.Call(func=log_func, args=args, keywords=[])
        result = ast.Expr(value=call)
        return result

    def __get_JoinedStr_node(self, if_condition):
        nodes = [node for node in ast.walk(if_condition)]
        ids = []
        formated_Values=[]
        string_for_log = ''
        for node in nodes:
            unparsed_node = ast.unparse(node)
            if isinstance(node, ast.Name):
                ids.append(node.id)
        if not ids:
            raise NotImplementedError
        for variable in ids:
            string_for_log += ' '+ variable + ' is:' + '{' + variable +'}'
#            formated_value = ast.FormattedValue(value=ast.Name(id=variable, ctx=ast.Load()),
#                                                ctx=ast.Load(),
#                                                conconversion=-1 )
#            formated_Values.append(ast.Constant(value='--'))
#            formated_Values.append(formated_value)
        result_string = 'f\" '+ string_for_log + ' \"'
        result = ast.parse(result_string)
#        result = ast.Expr(value=ast.JoinedStr(values=formated_value))
        print(ast.unparse(result))
        return [result.body[0].value]