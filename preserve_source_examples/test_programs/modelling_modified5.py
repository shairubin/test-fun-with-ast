
def dot_product_attention_weights():
    attn_weights -= jax.nn.logsumexp(attn_weights, axis=-1, keepdims=True)