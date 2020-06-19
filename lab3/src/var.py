#!/usr/bin/env python3


# Reference: John Harrison,

# Introduction to Functional Programming, 1997,

# https://www.cl.cam.ac.uk/teaching/Lectures/funprog-jrh-1996/all.pdf

#

# Var, Const, Comb, Abst -- 2.3.1 Lambda terms

# free and bound -- 2.3.2 Free and bound variables

# sub -- 2.3.3 Substitution

# beta -- 2.3.4 Conversions

class Var(object):

    def __init__(self, v):
        assert isinstance(v, str)

        self.v = v

    def __str__(self):
        return self.v

    def free(self):
        return {self.v}

    def bound(self):
        return set()

    def sub(self, v, exp):
        if self.v == v:
            return exp

        return self


class Const(object):

    def __init__(self, c):
        assert isinstance(c, str)

        self.c = c

    def __str__(self):
        return self.c

    def free(self):
        return set()

    def bound(self):
        return set()

    def sub(self, v, exp):
        return self


class Comb(object):

    def __init__(self, s, t):

        self.s = s

        self.t = t

    def __str__(self):

        return "( {} {} )".format(self.s, self.t)

    def free(self):

        return self.s.free() | self.t.free()

    def bound(self):

        return self.s.bound() | self.t.bound()

    def sub(self, v, exp):

        return Comb(self.s.sub(v, exp), self.t.sub(v, exp))

    def beta(self):

        if isinstance(self.s, Comb):
            return Comb(self.s.beta(), self.t)

        if isinstance(self.s, Abst):
            return self.s.s.sub(self.s.x, self.t)

        if isinstance(self.t, Abst) or isinstance(self.t, Comb):
            return Comb(self.s, self.t.beta())

        return self


class Abst(object):

    def __init__(self, x, s):
        self.x = x

        self.s = s

    def __str__(self):
        return "\\{} -> {}".format(self.x, self.s)

    def free(self):
        return self.s.free() - {self.x}

    def bound(self):
        return {self.x} | self.s.bound()

    def sub(self, v, exp):
        if v == self.x:
            return self

        return Abst(self.x, self.s.sub(v, exp))

    def beta(self):
        return Abst(self.x, self.s.beta())


zero = Abst('f', Abst('x', Var('x')))
one = Abst('f', Abst('x', Comb(Var('f'), Var('x'))))
two = Abst('f', Abst('x', Comb(Var('f'), Comb(Var('f'), Var('x')))))
three = Abst('f', Abst('x', Comb(Var('f'),Comb(Var('f'), Comb(Var('f'), Var('x'))))))
four = Abst('f', Abst('x', Comb(Var('f'),Comb(Var('f'),Comb(Var('f'), Comb(Var('f'), Var('x')))))))
five = Abst('f', Abst('x', Comb(Var('f'),Comb(Var('f'),Comb(Var('f'),Comb(Var('f'), Comb(Var('f'), Var('x'))))))))
TRUE = Abst('u', Abst('v', Var('u')))
FALSE = Abst('u', Abst('v', Var('v')))


def sum(m, n):
    return Abst('f', Abst('x', Comb(Comb(m, Var('f')), Comb(Comb(n, Var('f')), Var('x')))))


def succ(n):
    return Abst('f', Abst('x', Comb(Var('f'), Comb(Comb(n, Var('f')), Var('x')))))


def mult(m, n):
    return Abst('f', Comb(m, Comb(n, Var('f'))))


def pred(n):
    return Abst('f', Abst('x', Comb(Comb(Comb(n, Abst('g', Abst('h', Comb(Var('h'), Comb(Var('g'), Var('f')))))), Abst('u', Var('x'))),Abst('u', Var('u')))))


def fact(n):
    T = Abst('f', Abst('x', Comb(Comb(Var('f'), Var('f')), Var('x'))))
    G = Abst('g', Abst('n', Comb(Comb(n, Abst('g', mult(n, Comb(Comb(Var('g'), Var('g')), pred(n))))), one)))
    return Comb(T,G)


if __name__ == '__main__':

    x = fact(pred(five))
    print(x)

    for _ in range(100):
        x = x.beta()
        print(x)

