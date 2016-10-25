#!/usr/bin/env python3

import sys

class Operator(object):

    _map = dict()

    def __repr__(self):
        return "{}.get({})".format(type(self).__name__, self.name)

    def __cmp__(self, other):
        if self.order > other.order:
            return 1
        elif self.order < other.order:
            return -1
        else:
            return 0

    def __init__(self, name, func=None, order=0):
        if name in self._map:
            raise ValueError("Operator {} already defined.".format(name))
        else:
            self._map[name] = self
            self.name = name
            if func != None:
                self.do = func
            else:
                raise ValueError("No function specified for new operator {}".format(name))
            self.order = order

    @classmethod
    def get(cls, name):
        return cls._map[name]

    @classmethod
    def exist(cls, name):
        return name in cls._map

Operator("+", lambda x, y: x + y, 10)
Operator("-", lambda x, y: x - y, 10)
Operator("*", lambda x, y: x * y, 20)
Operator("/", lambda x, y: x / y, 20)
Operator("^", lambda x, y: x ** y, 30)


if __name__ == "__main__":
    try:
        out_stack = []
        while True:
            in_string = input()
            if Operator.exist(in_string):
                if len(out_stack) >= 2:
                    b, a = out_stack.pop(), out_stack.pop()
                    out_stack.append(Operator.get(in_string).do(a, b))
                    print(out_stack[-1])
                else:
                    print("Not enough numbers on stack to complete operation")
                    print(out_stack)
            elif in_string.isnumeric():
                out_stack.append(int(in_string))
            elif in_string == "p":
                if out_stack:
                    print(out_stack[-1])
            elif in_string == "q":
                raise KeyboardInterrupt
            elif in_string == "f":
                print(out_stack)
            else:
                raise print("Undefined input")
    except KeyboardInterrupt:
        sys.exit(0)
    except EOFError:
        if out_stack:
            print(out_stack[-1])
        sys.exit(0)
