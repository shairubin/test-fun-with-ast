import subprocess

import pytest
import logging

from tests.test_utils import TestUtils

logger = logging.getLogger()
from RewriteIf import RewriteIf
from my_main import simple_parse_example


class TestE2E():

    def test_rewriteIf_no_if1(self):
        out_stream = b''
        out1 = subprocess.run(["python", "./../test_programs/fibonacci_test.py"],
                       stdout=subprocess.PIPE)
        out2 = subprocess.run(["python", "./../test_programs/fibonacci_test.py"],
                       stdout=subprocess.PIPE)

        assert out2.stdout == out1.stdout
