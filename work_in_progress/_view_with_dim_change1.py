def forward(
    ctx,  # pyre-ignore[2]: Parameter must be annotated.
    self: DT,
) -> DT:
    ctx.previous_placement = self.placements
