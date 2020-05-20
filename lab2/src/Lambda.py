
# interpreting and visualize
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

POW = lambda a: lambda b: b(a)
#  PRED  := λn.λf.λx.n (λg.λh.h (g f)) (λu.x) (λu.u)
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
# true = λx. λy. x
C_True = lambda u: lambda v: u
# false = λx. λy. y
C_False = lambda u: lambda v: v
# let BoolAnd = lambda x y . x y FALSE 
OR  = lambda a: lambda b: a(C_True)(b)
# let BoolOr = lambda x y. x TRUE y 
AND = lambda a: lambda b: a(b)(C_False)
# let BoolNot = lambda x . x FALSE TRUE 
NOT = lambda a: a(C_False)(C_True)

# iszero n = n (λb. false) true
ISZERO = lambda n: n(lambda x: C_False)(C_True)

T = lambda f: lambda x: f(f)(x)
G = lambda g: lambda n: n(lambda u: MUL(n)(g(g)(PRED(n))))(One)
FACT = T(G)

# Factorial n = n * factorial(n-1)
# F=λx.F(PREDX)


# Y=λf.( λx.f(xx))( λx.f(xx))
# YF = F(F(F(F(…)))
# T=λf. λx.ffx
# G=λg.λn.n(λu.MULn(gg(PREDn)))1
# 	G=λg.( λh. λn.n(λu.MULn(h(PREDn)))1)(g g)
# 	=λg.F(gg)
# TG=(λf. λx.ffx)( λg.F(gg))
# =λx.( λg.F(gg))( λg.F(gg))x
# =(λg.F(gg))( λg.F(gg))
# =(λf.( λg.f(gg))( λf.f(gg))F
# =YF

