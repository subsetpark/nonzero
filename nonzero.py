"""
Certain types of numerical values don't understand the concept of 0, usually ordinal
Values: years, streets, storeys.
"""

class nz(int):
    def check_for_0(s):
        def f(self, other):
            method = getattr(super(), s)
            if self < 0 and method(other) >= 0:
                return type(self)(method(other) + 1)
            elif self > 0 and method(other) <= 0:
                return type(self)(method(other) - 1)
            else:
                return type(self)(method(other))
        return f

    def __new__(cls, x):
        if x == 0:
            raise ValueError("0 is not a valid value")
        else:
            return super().__new__(cls, x)

    __add__ = check_for_0('__add__')
    __sub__ = check_for_0('__sub__')