#!/usr/bin/env python3
import argparse
def collect_license(current):
            try:
                ident = identify_license(license_file)
            except ValueError:
                raise ValueError('could not identify license file '
                                 f'for {root}') from None
