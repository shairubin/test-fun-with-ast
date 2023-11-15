#!/usr/bin/env python3

from __future__ import print_function

WRAPPER_SRC_NAMES = {

    # add additoonal:
    "ALL_AVX512F_MICROKERNEL_SRCS": "defined(__i386__) || defined(__i686__) || defined(__x86_64__)",

    "PROD_SCALAR_MICROKERNEL_SRCS": "defined(__arm__)",

}


