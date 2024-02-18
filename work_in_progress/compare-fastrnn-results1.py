
def construct_name(fwd_bwd, test_name):
    return f"{suite_name}[{test_name}]:{'bwd' if bwd else 'fwd'}"

