# mod 3 will load a mode from other directory

from ..submod1 import mod1

def f31():
    print 'call f1() from mod3.py'    
    mod1.f1()

f31()
