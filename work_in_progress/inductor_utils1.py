
def check_model_cuda(
    rtol=None,
):

    if rtol is not None:
        rtol = max(2e-3, rtol)
