import ast
import logging

from RewriteImports import RewriteImports

logging.basicConfig(level=logging.INFO)
from RewriteConstant import RewriteConstant
from RewriteIf import RewriteIf

def simple_if_block(x):
    if x == 5:
        logging.info(f'the value of x is: {x}')
    else:
        pass
    simple_if = """
import logging
if x == 5 or y != 7 and z == 6: 
    logging.info(f'body if {x}, {y}')
else:         
    logging('body else')
"""
    return simple_if

def simple_rewrtie_example(parsed_tree):
    rewrite_tree = RewriteConstant().visit(parsed_tree)
    return rewrite_tree

def simple_rewrtie_if_example(parsed_tree):
    rewrite_tree = RewriteIf().visit(parsed_tree)
    rewrite_tree_recalcutate_positions = ast.fix_missing_locations(rewrite_tree)
    return rewrite_tree_recalcutate_positions

def simple_unparse_example(parsed_tree):
    unparsed_tree=ast.unparse(parsed_tree)
    logging.info(f"** the unparsed tree: \n{unparsed_tree}")
    print(unparsed_tree)
    return unparsed_tree

def simple_rewrite_import_example(parsed_tree):
    rewrite_tree = RewriteImports().visit(parsed_tree)
    rewrite_tree_recalcutate_positions = ast.fix_missing_locations(rewrite_tree)
    return rewrite_tree_recalcutate_positions

def simple_parse_example(python_prog: str):
    parsed_tree= ast.parse(python_prog)
    parsed_tree_dump= ast.dump(parsed_tree, include_attributes=False, indent=5)
    logging.info(f"simple_parse_example: the parsed tree: {parsed_tree_dump}")
    return parsed_tree

if __name__ == "__main__":
#    parsed_tree = simple_parse_example('x   +=   5')
#    unparsed_tree = simple_unparse_example(parsed_tree)
#    rewrite_tree =   simple_rewrtie_example(parsed_tree)
#    simple_unparse_example(rewrite_tree)
    simple_if = simple_if_block(7)
    print(simple_if)
    parsed_tree = simple_parse_example(simple_if)
    rewrite_if_tree = simple_rewrtie_if_example(parsed_tree)
    simple_parse_example(rewrite_if_tree)
    simple_unparse_example(rewrite_if_tree)