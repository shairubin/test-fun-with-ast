import ast
import subprocess

from fun_with_ast.manipulate_node.get_node_from_input import GetNodeFromInput
from fun_with_ast.source_matchers.matcher_resolver import GetDynamicMatcher

from common_utils import CommonUtils, bcolors




def match_original_program(test_program='./test_programs/fib.py'):
    _perform_sanity(test_program)
    # read whole file to a string
    utils = CommonUtils()
    python_program_as_string = utils.read_file_as_string(test_program)
    print(bcolors.WARNING + f"AST test for {test_program}\nORIGINAL PROGRAM:\n" + python_program_as_string, bcolors.ENDC)
    unparsed_program = ast.unparse(ast.parse(python_program_as_string))
    print(bcolors.FAIL + f"\nAST test for {test_program}\nAST UNPARSED PROGRAM:\n" + unparsed_program, bcolors.ENDC)
    fib_node = GetNodeFromInput(python_program_as_string, 0, get_module=True)
    fib_node_matcher = GetDynamicMatcher(fib_node)
    fib_node_matcher.do_match(python_program_as_string)
    fun_with_ast_source = fib_node_matcher.GetSource()
    print(bcolors.OKBLUE + f"\nAST test for {test_program}\nFUN WITH AST PROGRAM:\n" + fun_with_ast_source, bcolors.ENDC)
    assert fun_with_ast_source == python_program_as_string



def _perform_sanity(test_program):
    out1 = subprocess.run(["python", test_program],
                          stdout=subprocess.PIPE)
    out2 = subprocess.run(["python", test_program],
                          stdout=subprocess.PIPE)
    assert out2.stdout == out1.stdout
    return out2

def _comparte_asts(test_program, output_program):
    utils = CommonUtils()
    rewrite_string = subprocess.run(["grep", "-v", "info", output_program], stdout=subprocess.PIPE)
    original_string = utils.read_file_as_string(test_program)
    original_ast = 'TBD'
    rewrite_ast = 'TBD'
    assert utils.compare_ast(original_ast, rewrite_ast)



if __name__ == "__main__":
    test_programs = ['./test_programs/fib.py',
                     './test_programs/prime.py'
                     ]
    wip_programs = ['./work_in_progress/modified_fib.py',
                    './work_in_progress/prime_wip.py',
                    ]
    for p in test_programs:
        match_original_program(test_program=p)
    #for p in wip_programs:
    #    match_original_program(test_program=p)