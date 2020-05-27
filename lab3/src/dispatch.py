from Multiple import *

overload = multimethod


class Foo:
    @overload(int, int)
    def add(n, m, *args):
        return n + m

    @overload(float, float)
    def add(n, m, *args):
        return n + m

    @overload(int, float)
    def add(n, m, *args):
        return n + m

    @overload(object, object)
    def add(n, m, *args):
        return str(n) + str(m)

    @overload(int, str)
    def add(n, m, *args):
        return str(n) + m

    @overload(str, int)
    def add(n, m, *args):
        return n + str(m)

    @overload()
    def add(*args):
        k = 0
        for i in range(len(args)):
            if args[i] == None:
                continue
            if isinstance(args[i], str) or isinstance(k, str):
                if (i == 0):
                    k = ''
                k = str(k) + str(args[i])
            else:
                k = k + args[i]
        return k

    @overload(str)
    def add(*args):
        k = 0
        for i in range(len(args)):
            if args[i] == None:
                continue
            if isinstance(args[i], str) or isinstance(k, str):
                if (i == 0):
                    k = ''
                k = str(k) + str(args[i])
            else:
                k = k + args[i]
        return k


class Foo1(Foo):
    @overload(float, int)
    def add(n, m, *args):
        return n + m


class Foo2(Foo1):
    @overload(int, int, int)
    def add(n, m, *args):
        return n + m + args[0]
