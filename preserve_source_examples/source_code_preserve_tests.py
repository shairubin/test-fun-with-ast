import ast
import subprocess
from difflib import Differ

from fun_with_ast.manipulate_node.get_node_from_input import GetNodeFromInput
from fun_with_ast.source_matchers.matcher_resolver import GetDynamicMatcher

from common_utils import CommonUtils, bcolors

RUN_TEST_PROGRAMS = True
RUN_WIP_PROGRAMS = False



def match_original_program(test_program='./test_programs/fib.py', run_program=True):
    utils = CommonUtils()
    python_program_as_string = utils.read_file_as_string(test_program)
    print('RUNNING TEST ON ORIGINAL PROGRAM: '+test_program)
    if run_program:
        _perform_sanity(test_program)
    # read whole file to a string
    print(bcolors.WARNING + f"AST test for {test_program}\nORIGINAL PROGRAM:\n" + python_program_as_string, bcolors.ENDC)
    unparsed_program = ast.unparse(ast.parse(python_program_as_string))
    print(bcolors.FAIL + f"\nAST test for {test_program}\nAST UNPARSED PROGRAM:\n" + unparsed_program, bcolors.ENDC)
    fib_node = GetNodeFromInput(python_program_as_string, 0, get_module=True)
    fib_node_matcher = GetDynamicMatcher(fib_node)
    try:
        fib_node_matcher.do_match(python_program_as_string)
    except Exception as e:
        raise e
    fun_with_ast_source = fib_node_matcher.GetSource()
    print(bcolors.OKBLUE + f"\nAST test for {test_program}\nFUN WITH AST PROGRAM:\n" + fun_with_ast_source, bcolors.ENDC)
    if not fun_with_ast_source == python_program_as_string:
        _assert_diff(python_program_as_string, fun_with_ast_source)

def _assert_diff(original_if_source, new_code):
    differ = Differ()
    lines1 = original_if_source.split('\n')
    lines2 = new_code.split('\n')
    diff_lines = []
    for line in differ.compare(lines1, lines2):
        if line.startswith('+'):
            print(bcolors.FAIL + line, bcolors.ENDC)
            raise ValueError('diff lines: line added')
        elif line.startswith('-'):
            print(bcolors.OKBLUE + line, bcolors.ENDC)
            raise ValueError('diff lines: line removed')
        elif line.startswith(' '):
            pass
        else:
            raise ValueError('diff lines')




def _perform_sanity(test_program):
    out1 = subprocess.run(["python", test_program],
                          stdout=subprocess.PIPE)
    assert out1.returncode == 0
    out2 = subprocess.run(["python", test_program],
                          stdout=subprocess.PIPE)
    assert out2.returncode == 0
    assert out2.stdout == out1.stdout
    return out2

# TODO: issue #7 for implementing the below method
def _comparte_asts(test_program, output_program):
    utils = CommonUtils()
    original_ast = 'TBD'
    rewrite_ast = 'TBD'
    assert utils.compare_ast(original_ast, rewrite_ast)


def _run_on_example_programs(test_programs):
    for index, p in enumerate(test_programs):
        print('================================================')
        print('TEST NUMBER: ' + str(index + 1) + ' START FOR: ' + p[0])
        print('================================================')
        match_original_program(test_program=p[0], run_program=p[1])
        print('TEST NUMBER: ' + str(index + 1) + ' END FOR: ' + p[0])


if __name__ == "__main__":
    test_programs = [('./test_programs/fib.py', True),
                     ('./test_programs/prime.py', True),
                     ('./test_programs/modified_fib.py', True),
                     ('./test_programs/portfolio.py', False),
                     ('./test_programs/vqgan_arch_modified.py', False),
                     ('./test_programs/exceptions3.py', False),
                     ('./test_programs/exceptions.py', False),
                     ('./test_programs/modelling_modified2.py', False),
                     ('./test_programs/modelling_modified3.py', False),
                     ('./test_programs/modelling_modified4.py', False),

                     ]
    wip_programs = [
                    ('/home/shai/test_fun_with_ast/work_in_progress/modelling_modified4.py', False),
                    ]
    if RUN_TEST_PROGRAMS:
        _run_on_example_programs(test_programs)
    if RUN_WIP_PROGRAMS:
        _run_on_example_programs(wip_programs)
