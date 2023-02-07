import subprocess
import logging

import pytest

logging.basicConfig(level=logging.INFO)
from my_main import simple_parse_example, simple_rewrtie_if_example, simple_unparse_example, \
    simple_rewrite_import_example


class TestE2E():
    @pytest.mark.parametrize("test_program", ['./../test_programs/fibonacci_test.py'])
    def test_rewriteIf_no_if1(self, test_program):
        out2 = self._perform_sanity(test_program)
        # read whole file to a string
        python_string = self._read_file_as_string(test_program)
        # tramsform the original program
        python_result = self._rewrite_tree(python_string)
        rewrite_out = self._run_modified_program(python_result)

        assert out2.stdout == rewrite_out.stdout

    def _run_modified_program(self, python_result):
        with open('/tmp/test.py', 'w') as modified_program:
            modified_program.write(python_result)
        rewrite_out = subprocess.run(["python", "/tmp/test.py"], stdout=subprocess.PIPE)
        return rewrite_out

    def _rewrite_tree(self, python_string):
        parsed_tree = simple_parse_example(python_string)
        simple_rewrite_import_example(parsed_tree)
        rewrite_if_tree = simple_rewrtie_if_example(parsed_tree)
        python_result = simple_unparse_example(rewrite_if_tree)
        logging.info(python_result)
        return python_result

    def _read_file_as_string(self, test_program):
        text_file = open(test_program, 'r')
        python_string = text_file.read()
        text_file.close()
        return python_string

    def _perform_sanity(self, test_program):
        out1 = subprocess.run(["python", test_program],
                              stdout=subprocess.PIPE)
        out2 = subprocess.run(["python", test_program],
                              stdout=subprocess.PIPE)
        assert out2.stdout == out1.stdout
        return out2
