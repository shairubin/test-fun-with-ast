
# Convenience aliases for common composite types that we need
# to talk about in PyTorch

_TensorOrTensorsOrGradEdge = Union[
    torch.Tensor, Sequence[torch.Tensor],
    "torch.autograd.graph.GradientEdge",
    Sequence["torch.autograd.graph.GradientEdge"]]
