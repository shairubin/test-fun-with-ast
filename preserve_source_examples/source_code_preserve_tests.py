import ast
import subprocess
from difflib import Differ

from fun_with_ast.manipulate_node.get_node_from_input import GetNodeFromInput
from fun_with_ast.source_matchers.matcher_resolver import GetDynamicMatcher
from fun_with_ast.source_matchers.reset_match import ResetMatch
from common_utils import CommonUtils, bcolors



def match_original_program(test_program='./test_programs/fib.py', run_program=True):
    utils = CommonUtils()
    python_program_as_string = utils.read_file_as_string(test_program)
    print('RUNNING TEST ON ORIGINAL PROGRAM: '+test_program)
    if run_program:
        _perform_sanity(test_program)
    # read whole file to a string
    print(bcolors.WARNING + f"AST test for {test_program}\n" , bcolors.ENDC)
#    print(bcolors.WARNING + python_program_as_string, bcolors.ENDC)
    unparsed_program = ast.unparse(ast.parse(python_program_as_string))
    print(bcolors.FAIL + f"\nAST test for {test_program}\nAST UNPARSED PROGRAM:\n" , bcolors.ENDC)
#    print(bcolors.FAIL + unparsed_program , bcolors.ENDC)
    orig_node = GetNodeFromInput(python_program_as_string, 0, get_module=True)
    orig_node_matcher = GetDynamicMatcher(orig_node)
    try:
        orig_node_matcher.do_match(python_program_as_string)
    except Exception as e:
        raise e
    fun_with_ast_source = orig_node_matcher.GetSource()
    ast.parse(fun_with_ast_source)
    print(bcolors.OKBLUE + f"\nAST test for {test_program}\nFUN WITH AST PROGRAM:\n", bcolors.ENDC)
#    print(bcolors.OKBLUE  + fun_with_ast_source, bcolors.ENDC)
    if not fun_with_ast_source == python_program_as_string:
        _assert_diff(python_program_as_string, fun_with_ast_source, stop_on_diff=True)
    _assert_diff(python_program_as_string, unparsed_program, stop_on_diff=False)
    location_of_error  = len(fun_with_ast_source) // 2
    _verify_we_catch_changes_in_code(fun_with_ast_source, location_of_error, python_program_as_string)
    _verify_reset(orig_node)


def _verify_we_catch_changes_in_code(fun_with_ast_source, location_of_error, python_program_as_string):
    new_char = 'X'
    code_with_error = fun_with_ast_source
    code_with_error_list = list(code_with_error)
    code_with_error_list[location_of_error] = new_char
    code_with_error = ''.join(code_with_error_list)
    if code_with_error == python_program_as_string:
        raise ValueError('new code is same as original code')


def _assert_diff(original_source, new_code, stop_on_diff=True):
    differ = Differ()
    lines1 = original_source.split('\n')
    lines2 = new_code.split('\n')
    diff_lines = []
    for line in differ.compare(lines1, lines2):
        if line.startswith('+'):
            print(bcolors.FAIL + line, bcolors.ENDC)
            if stop_on_diff:
                raise ValueError('diff lines: line added')
        elif line.startswith('-'):
            print(bcolors.OKBLUE + line, bcolors.ENDC)
            if stop_on_diff:
                raise ValueError('diff lines: line removed')
        elif line.startswith(' '):
            pass
        else:
            print(bcolors.OKCYAN + line, bcolors.ENDC)
            if stop_on_diff:
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


def _verify_reset(module_node):
    if not isinstance(module_node, ast.Module):
        raise ValueError('original node must be a module node')
    resetter = ResetMatch(module_node)
    resetter.reset_match()


def _run_on_example_programs(test_programs):
    for index, p in enumerate(test_programs):
        print('================================================')
        print('TEST NUMBER: ' + str(index + 1) + ' START FOR: ' + p[0])
        print('================================================')
        match_original_program(test_program=p[0], run_program=p[1])
        print('TEST NUMBER: ' + str(index + 1) + ' END FOR: ' + p[0])


RUN_TEST_PROGRAMS = True
RUN_WIP_PROGRAMS = False


if __name__ == "__main__":
    test_programs = [
                    ('./test_programs/fib.py', True),
                     ('./test_programs/prime.py', True),
                     ('./test_programs/modified_fib.py', True),
                     ('./test_programs/portfolio.py', False),
                     ('./test_programs/vqgan_arch_modified.py', False),
                     ('./test_programs/exceptions3.py', False),
                     ('./test_programs/exceptions.py', False),
                     ('./test_programs/modelling_modified2.py', False),
                     ('./test_programs/modelling_modified3.py', False),
                     ('./test_programs/modelling_modified4.py', False),
                     ('./test_programs/modelling_modified5.py', False),
                     ('./test_programs/modelling_modified6.py', False),
                     ('./test_programs/modelling_modified7.py', False),
                     ('./test_programs/modelling_modified8.py', False),
                     ('./test_programs/sentence_modified.py', False),
                     ('./test_programs/sentence.py', False),
                     ('./test_programs/unbalanced_parentheses.py', False),
                     ('./test_programs/unbalanced_parentheses2.py', False),
                     ('./test_programs/unbalanced_parentheses_orig.py', False),
                     ('./test_programs/_utils_internal2.py', False),
                     ('./test_programs/_utils_internal_orig.py', False),
                     ('./test_programs/native1.py', False),
                     ('./test_programs/native_orig.py', False),
                    ('./test_programs/torch_sources1.py', False),
                    ('./test_programs/torch_sources.py', False),
                    ('./test_programs/export_pytorch_labels.py', False),
                    ('./test_programs/pipe_with_ddp_test.py', False),
                    ('./test_programs/build_bundled1.py', False),
                    ('./test_programs/build_bundled.py', False),
                    ('./test_programs/pytorch_classes.py', False),
                    ('./test_programs/get_python_cmake_flags.py', False),
                    ('./test_programs/onnx_backend_test1.py', False),
                    ('./test_programs/onnx_backend_test.py', False),
                    ('./test_programs/return_types.py', False),
                    ('./test_programs/pytorch_utils1.py', False),
                    ('./test_programs/pytorch_utils.py', False),
                    ('./test_programs/pytorch_init.py', False),
                    ('./test_programs/pytorch_string_with_quotes.py', False),
                    ('./test_programs/pytorch_string_with_quotes1.py', False),
                    ('./test_programs/_lowrank.py', False),
                    ('./test_programs/init_with_import.py', False),
                    ('./test_programs/_hook_iterator.py', False),
                    ('./test_programs/vmap.py', False),
                    ('./test_programs/source.py', False),
                    ('./test_programs/comment_on_pr.py', False),
                    ('./test_programs/compare-fastrnn-results.py', False),
                    ('./test_programs/bench.py', False),
                    ('./test_programs/hierarchical_model_averager.py', False),
                    ('./test_programs/pytorch_build_definitions.py', False),
                    ('./test_programs/generate-xnnpack-wrappers.py', False),
                    ('./test_programs/_custom_ops.py', False),
                    ('./test_programs/_view_with_dim_change.py', False),
                    ('./test_programs/cond.py', False),
                    ('./test_programs/inductor_utils.py', False),
                    ('./test_programs/test_dlpack.py', False),
                    ('./test_programs/annotations.py', False),
                    ('./test_programs/heap.py', False),
                    ('./test_programs/the_game.py', False),
                    ('./test_programs/decomposition.py', False),
                    ('./test_programs/ensure_clipped_test.py', False),
                    ('./test_programs/context.py', False),

    ]
    wip_programs = [
                    ('/home/shai/test_fun_with_ast/work_in_progress/context1.py', False),
                    #('/home/shai/make-developers-brighter/e2e_tests/test_files/TheGame/the_game.py', False),
                    ]
    if RUN_TEST_PROGRAMS:
        _run_on_example_programs(test_programs)
    if RUN_WIP_PROGRAMS:
        _run_on_example_programs(wip_programs)
