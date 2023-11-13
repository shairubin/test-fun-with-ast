#!/usr/bin/env python3

from __future__ import print_function
import collections
import os
import sys
import logging

def update_sources(xnnpack_path, cmakefile = "XNNPACK/CMakeLists.txt"):
    sources = collections.defaultdict(list)
    while i < len(lines):
            line = lines[i]


            if line.startswith("SET") and line.split('(')[1].strip(' \t\n\r') in set(WRAPPER_SRC_NAMES.keys()) | set(SRC_NAMES):
                name = line.split('(')[1].strip(' \t\n\r')
            else:
                i += 1
    return sources
