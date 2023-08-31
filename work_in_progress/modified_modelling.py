

def norm(type, *args, **kwargs):
    if type == "rmsnorm":
        return RMSNorm(*args, **kwargs)
    elif type == "layernorm":
        return nn.LayerNorm(*args, **kwargs)
    else:
        raise ValueError(f"Unknown norm type {type}")


def dot_product_attention_weights(
    query: Any,
    key: Any,
    bias: Optional[Any] = None,
    mask: Optional[Any] = None,
    embed_pos: Optional[Any] = None,
    broadcast_dropout: bool = True,
    dropout_rng: Optional[PRNGKey] = None,
    dropout_rate: float = 0.0,
    deterministic: bool = False,
    dtype: Any = jnp.float32,
    precision: PrecisionLike = None,
    sinkhorn_iters: int = 1,
    is_encoder: bool = False,
    tau=None,
):
    """
    Computes dot-product attention weights given query and key.
    mask is included into the bias.

    Adapted from flax.linen.attention.dot_product_attention_weights"
    """

    pass