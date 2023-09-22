
def generate(
            self,
            input_ids: jnp.ndarray,
            attention_mask: Optional[jnp.ndarray] = None,
            max_length: Optional[int] = None,
            pad_token_id: Optional[int] = None,
            bos_token_id: Optional[int] = None,
            eos_token_id: Optional[int] = None,
            decoder_start_token_id: Optional[int] = None,
            do_sample: Optional[bool] = None,
            prng_key: Optional[jnp.ndarray] = None,
            top_k: Optional[int] = None,
            top_p: Optional[float] = None,
            temperature: Optional[float] = None,
            num_beams: Optional[int] = None,
            no_repeat_ngram_size: Optional[int] = None,
            min_length: Optional[int] = None,
            forced_bos_token_id: Optional[int] = None,
            forced_eos_token_id: Optional[int] = None,
            length_penalty: Optional[float] = None,
            early_stopping: Optional[bool] = None,
            trace: bool = True,
            params: Optional[Dict[str, jnp.ndarray]] = None,
            condition_scale: Optional[float] = 1.0,
            input_ids_uncond: Optional[jnp.ndarray] = None,
            attention_mask_uncond: Optional[jnp.ndarray] = None,
            **model_kwargs,
    ):

        if self.config.is_encoder_decoder:
            # add encoder_outputs to model_kwargs
            if model_kwargs.get("encoder_outputs") is None:
                model_kwargs_input = dict(model_kwargs)
                model_kwargs = self._prepare_encoder_decoder_kwargs_for_generation(
                    input_ids,
                    params,
                    {"attention_mask": attention_mask, **model_kwargs_input},
                )
                if condition_scale != 1.0:
                    assert (
                            input_ids_uncond is not None
                    ), "`input_ids_uncond` has to be defined for super conditioning."
                    assert (
                            do_sample is True
                    ), "`do_sample` has to be True for super conditioning."
                    assert (
                            num_beams == 1
                    ), "`num_beams` has to be 1 for super conditioning."
                    model_kwargs_uncond = (
                        self._prepare_encoder_decoder_kwargs_for_generation(
                            input_ids_uncond,
                            params,
                            {
                                "attention_mask": attention_mask_uncond,
                                **model_kwargs_input,
                            },
                        )
                    )
                else:
                    model_kwargs_uncond = None
            # prepare decoder_input_ids for generation
            input_ids = (
                    jnp.ones((input_ids.shape[0], 1), dtype="i4") * decoder_start_token_id
            )

