def exposed_in(module):
    def wrapper(fn):
        fn.__module__ = module
        return fn
    return wrapper

argnums_t = Union[int, Tuple[int, ...]]
