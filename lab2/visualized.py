


def x_():
    return 0


def f_(x=None):
    return lambda: 1 + x()


def interpret(f):
    # the natural value of a function
    return f(f_)(x_)()

def predicate(f):
    # the bool value of a function
    if f(f_)(x_)() == 0:
        return False
    else:
        return True
# INC := λn.λf.λx.f (n f x)
INC = lambda n: lambda a: lambda b: a(n(a)(b))
# PLUS  := λm.λn.m SUCC n
ADD=lambda a: lambda b: a(INC)(b)
#  MULT  := λm.λn.λf.m (n f)
MUL = lambda a: lambda b: lambda c: a(b(c))


PRED = lambda n: lambda f: lambda x: n(lambda g: lambda h: h(g(f)))(lambda u: x)(lambda u: u)
#  0 := λf.λx.x
zero = lambda f: lambda x: x
#  1 := λf.λx.f x
One = lambda f: lambda x: f(x)
# 2 := λf.λx.f (f x)
TWO   = lambda a: lambda b: a(a(b))
#  3 := λf.λx.f (f (f x))
THREE = lambda a: lambda b: a(a(a(b)))
FOUR  = INC(THREE)
FIVE  = ADD(TWO)(THREE)
SIX   = MUL(TWO)(THREE)
SEVEN = INC(SIX)
EIGHT = MUL(FOUR)(TWO)






MULT_ = lambda m: lambda n: lambda f:m(n(f))
def MULT(n,m):

    
    print(f'λm.λn.λf. m (n f)')
    a=MULT_(m)(n)
    b=interpret(m)
    print(f'λn.λf. n ({b} f)')
    c=interpret(n)
    print(f'λf. {c} ({b} f)')
    d=interpret(a)
    print(f'{b}*{c}={d}')
    return a


T = lambda f: lambda x: f(f)(x)
G = lambda g: lambda n: n(lambda u: MULT(n,g(g)(PRED(n))))(One)
FACT = T(G)
FACT(SIX)

