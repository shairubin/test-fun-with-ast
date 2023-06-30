import ast
import contextlib
import os
import subprocess

from fun_with_ast.manipulate_node.create_node import GetNodeFromInput
from fun_with_ast.source_matchers.matcher_resolver import GetDynamicMatcher

from common_utils import CommonUtils, bcolors


class TestE2E:

    def test_rewriteIf_no_if1(self, test_program='/home/shai/auto-logging/preserve_source_examples/test_programs/fib.py', output_program='/tmp/test.py'):
        with contextlib.suppress(FileNotFoundError):
            os.remove(output_program)
        out2 = self._perform_sanity(test_program)
        # read whole file to a string
        utils = CommonUtils()
        python_string = utils.read_file_as_string(test_program)
        print(bcolors.OKCYAN + "\noriginal program:\n" + python_string, bcolors.ENDC)
        unparsed_program = ast.unparse(ast.parse(python_string))
        print(bcolors.OKGREEN + "\nunparsed program:\n" + unparsed_program, bcolors.ENDC)
        fib_node = GetNodeFromInput(python_string)
        fib_node_matcher = GetDynamicMatcher(fib_node)
        fib_node_matcher.do_match(python_string)
        fun_with_ast_source = fib_node_matcher.GetSource()


    #        python_result = self._rewrite_tree(python_string)
#        rewrite_out = self._run_modified_program(python_result, output_program)
#        self._comparte_asts(test_program, output_program)
#        assert out2.stdout == rewrite_out.stdout

    def _run_modified_program(self, python_result, output_program):
        with open(output_program, 'w') as modified_program:
            modified_program.write(python_result)
        rewrite_out = subprocess.run(["python", output_program], stdout=subprocess.PIPE)
        return rewrite_out

    def _rewrite_tree(self, python_string):
        parsed_tree = simple_parse_example(python_string)
        simple_rewrite_import_example(parsed_tree)
        rewrite_if_tree = simple_rewrtie_if_example(parsed_tree)
        python_result = simple_unparse_example(rewrite_if_tree)
        logging.info(python_result)
        return python_result

    def _perform_sanity(self, test_program):
        out1 = subprocess.run(["python", test_program],
                              stdout=subprocess.PIPE)
        out2 = subprocess.run(["python", test_program],
                              stdout=subprocess.PIPE)
        assert out2.stdout == out1.stdout
        return out2

    def _comparte_asts(self, test_program, output_program):
        test_utils = TestUtils()
        rewrite_string = subprocess.run(["grep", "-v", "info", output_program], stdout=subprocess.PIPE)
        original_string = test_utils.read_file_as_string(test_program)
        original_ast = simple_parse_example(original_string)
        rewrite_ast = simple_parse_example(rewrite_string.stdout)
        assert test_utils.compare_ast(original_ast, rewrite_ast)

