from fun_with_ast.manipulate_node.create_node import GetNodeFromInput
from fun_with_ast.manipulate_node.if_manipulator import ManipulateIfNode, IfManipulatorConfig
from fun_with_ast.source_matchers.matcher_resolver import GetDynamicMatcher

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



def if_body_rewrite(example_number, original_if_source, source_to_add, body_index, location_in_body_index):
    print(bcolors.UNDERLINE + bcolors.FAIL+'\n' + "Example number " + str(example_number)  + bcolors.ENDC)
    print(bcolors.OKBLUE  + "Original Code:\n" + original_if_source  + bcolors.ENDC)
    if_node = GetNodeFromInput(original_if_source)
    if_node_matcher = GetDynamicMatcher(if_node)
    if_node_matcher.Match(original_if_source)
    node_to_add = GetNodeFromInput(source_to_add)
    if_manipulator = ManipulateIfNode(if_node)
    if_manipulator.add_nodes([node_to_add], IfManipulatorConfig(body_index, location_in_body_index))
    new_code = if_node_matcher.GetSource()
    print(bcolors.OKCYAN + '\n' + "Modified Code:\n" + new_code + bcolors.ENDC)

if __name__ == "__main__":
    inputs = [("if True:\n    a = 1", "logger.info(\'Log for If body\')", 0, 0),
              ("if True:\n    a = 1", "logger.info(\'Log for If body\')", 0, 1),
              ("if True: # comment  \n     a = 1", "logger.info(\'Log for If body\')", 0, 1),
              #("if True: # comment  \n     a = 1\n#another comment", "logger.info(\'Log for If body\')", 0, 1)
              ("if True:\n     a = 1\nelse:\n    a=2", "logger.info(\'Log for If else\')", 1, 1),
              ("if True:\n     a = 1\nelse:\n    a=2", "logger.info(\'Log for If else 2\')", 1, 0),
              #("if a and (not c and not b):\n     a = 1\nelse:\n    a=2", "logger.info(\'Log for If else 2\')", 1, 0)
              ]
    for index, input in enumerate(inputs):
        if_body_rewrite(index, input[0], input[1], input[2], input[3])