def get_sharding_prop_cache_info():
    return (
        DTensor._propagator.propagate_op_sharding.cache_info()  # type:ignore[attr-defined
    )
