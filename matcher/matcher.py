from collections import defaultdict
from inspect import signature

__author__ = 'johannes'


class Match:
    functions = defaultdict(list)

    def __init__(self, f):
        self.name = f.__module__ + "." + f.__name__
        Match.functions[self.name].append(f)

    def __call__(self, *args, **kwargs):
        for func in Match.functions[self.name]:
            kw = dict(kwargs)
            params = signature(func).parameters
            kw.update(dict(zip(list(params), args)))
            for ann in func.__annotations__:
                if func.__annotations__[ann] != kw[ann]:
                    break
            else:
                return func(*args, **kwargs)
        else:
            raise TypeError("No match found for {func} with args={args} and kwargs={kwargs}".format(func=self.name,
                                                                                                    args=args,
                                                                                                    kwargs=kwargs))
