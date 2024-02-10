
def _process_batched_inputs(
    in_dims: in_dims_t, args: Tuple, func: Callable
) -> Tuple[int, List[Any], List[Any], TreeSpec]:
    if flat_in_dims is None:
        raise ValueError(
            f'vmap({_get_name(func)}, in_dims={in_dims}, ...)(<inputs>): '
            f'in_dims is not compatible with the structure of `inputs`. '
            f'in_dims has structure {tree_flatten(in_dims)[1]} but inputs '
            f'has structure {args_spec}.')

