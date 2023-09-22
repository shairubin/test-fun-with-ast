

class FlaxBartEncoderLayerCollection(nn.Module):
    config: DalleBartConfig
    dtype: jnp.dtype = jnp.float32  # the dtype of the computation
    """
    Edits:
    - use custom FlaxBartEncoderLayer
    - allow Gradient Checkpointing (nn.remat)
    """

    @nn.compact
    def __call__(
        self,
        hidden_states,
        attention_mask,
        deterministic: bool = True,
        output_attentions: bool = False,
        output_hidden_states: bool = False,
        return_dict: bool = True,
    ):

        if self.config.use_scan:
            raise NotImplementedError
        else:
            for i in range(n_layers):
                if output_hidden_states:
                    all_hidden_states += (hidden_states,)
                # final layernorm on the output of the last layer
                # or every 6 layers for Swin v2
                add_norm = self.config.ln_positions == "postln" or (
                    self.config.ln_positions == "swinv2"
                    and ((i + 1) % 6 == 0)
                    and (i != n_layers - 1)
                )
                # we don't need to scale the norm for the last layer
                use_scale = i != n_layers - 1
                layer_outputs = layer(
                    self.config,
                    dtype=self.dtype,
                    add_norm=add_norm,
                    use_scale=use_scale,
                    name=f"FlaxBartEncoderLayer_{i}",
                )(
                    hidden_states,
                    attention_mask,
                    output_attentions,
                    deterministic,
                )
                hidden_states = layer_outputs[0]
                if output_attentions:
                    all_self_attns += (layer_outputs[1],)


