import ast

from ChangeConstant import RewriteConstant


def simple_rewrtie_example(parsed_tree):
    rewrite_tree = RewriteConstant().visit(parsed_tree)
    return rewrite_tree

def simple_unparse_example(parsed_tree):
    unparsed_tree=ast.unparse(parsed_tree)
    print("** the unparsed tree: \n", unparsed_tree)
    return unparsed_tree

def simple_parse_example(python_prog):
    parsed_tree= ast.parse(python_prog)
    parsed_tree_dump= ast.dump(parsed_tree, include_attributes=False, indent=5)
    print("** the parsed tree: \n", parsed_tree_dump)
    return parsed_tree

if __name__ == "__main__":
    parsed_tree = simple_parse_example('x   +=   5')
    unparsed_tree = simple_unparse_example(parsed_tree)
    rewrite_tree =   simple_rewrtie_example(parsed_tree)
    simple_unparse_example(rewrite_tree)
