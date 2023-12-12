import inspect
import torch


def skip_init(module_cls, *args, **kwargs):
    if 'device' not in inspect.signature(module_cls).parameters:
        raise RuntimeError('Module must support a \'device\' arg to skip initialization')
