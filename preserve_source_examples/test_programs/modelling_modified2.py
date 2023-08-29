

# subln gain
subln_gain = {
    "encoder": lambda config: math.sqrt(
        1.0
        / 3.0
        * math.log(3 * config.decoder_layers)
        * math.log(2 * config.encoder_layers)
    ),
    "decoder": lambda config: math.sqrt(math.log(3 * config.decoder_layers))
}


