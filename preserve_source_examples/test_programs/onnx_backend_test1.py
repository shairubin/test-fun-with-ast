# @package onnx
# Module caffe2.python.onnx.tests.onnx_backend_test






import os
import unittest

import onnx.backend.test

import caffe2.python.onnx.backend as c2
from caffe2.python import core

core.SetEnginePref({}, {})

# This is a pytest magic variable to load extra plugins
pytest_plugins = 'onnx.backend.test.report',

backend_test = onnx.backend.test.BackendTest(c2, __name__)

backend_test.exclude(r'(test_hardsigmoid'  # Does not support Hardsigmoid.
                     '|test_hardmax'  # Does not support Hardmax.
                     '|test_.*FLOAT16.*'  # Does not support Cast on Float16.
                     '|test_depthtospace.*'  # Does not support DepthToSpace.
                     '|test_reduce_l1.*'  # Does not support ReduceL1.
                     ')')
