from Multiple import *
import numpy as np
class Foo:
    @multimethod(int, int)
    def add(a, b, *args):
        return a + b

    @multimethod(float, float)
    def add(a, b, *args):
        return a + b

    @multimethod(int, float)
    def add(a, b, *args):
        return a + b

    @multimethod(object, object)
    def add(a, b, *args):
        return str(a) + str(b)

    @multimethod(int, str)
    def add(a, b, *args):
        return str(a) + b
    @multimethod(str, int)
    def Str_Mult(a, b, *args):
        return a *b
    @multimethod(str, int)
    def add(a, b, *args):
        return a + str(b)
    @multimethod(str, float)
    def add(a, b, *args):
        return a + str(b)
    @multimethod(np.ndarray,np.ndarray)
    def add(a, b, *args):
        return a + b
    @multimethod(np.ndarray,int)
    def MAtrixIntMult(a, b, *args):
        return a * b
    @multimethod(np.ndarray,np.ndarray)
    def MatrixMult(a, b, *args):
        return np.dot(a, b) 

    @multimethod()
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

    @multimethod(str)
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
    @multimethod(float, int)
    def add(a, b, *args):
        return a + b


class Foo2(Foo1):
    @multimethod(int, int, int)
    def add(a, b, *args):
        return a + b + args[0]



