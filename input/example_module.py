# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 18:54:35 2015

@author: Georg
"""

def bisection(f, a, b, eps):
    fa = f(a)
    if fa*f(b) > 0:
        return None, 0
    
    i =  0   # iteration counter
    liste = []   # List to store intervals in
    while (b-a) > eps:
        i += 1
        m = (a + b)/2.0
        fm = f(m)
        if fa*fm <= 0:
            b = m   # root is in the left half of [a,b]
        else:
            a = m   # root is in the right half of [a,b]
            fa = fm
        print 'Iteration %d: interval=[%g, %g]' % (i, a, b)
        liste.append([i, a, b])
    return m, i, liste

def test_bisection():
    def f(x):
        return 2*x - 3   # simple linear equation with one root x=1.5
    
    x, i, liste = bisection(f, a=0, b=10, eps=1E-5)
    success = abs(x - 1.5) < 1E-5   # test within eps tolerance
    msg = "found x=%g != 1.5 " % x
    assert success, msg

def get_input():
    """Get f, a, b, eps from the command line."""
    import sys
    from scitools.StringFunction import StringFunction
    try:
        f = StringFunction(sys.argv[1])
        a = float(sys.argv[2])
        b = float(sys.argv[3])
        eps = float(sys.argv[4])
    except IndexError:
        print "Usage %s: f a b eps" % sys.argv[0]
        sys.exit(1)
    return f, a, b, eps

def calc_vals(f, a, b):
    x = [((b-a)/1000.0)*x + a for x in range(1000)]
    y = [f(k) for k in x]
    return x, y

if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        test_bisection()
    else:
        f, a, b, eps = get_input()
        x, i, liste = bisection(f, a, b, eps)
        print 'Found root x=%g in %d iterations' % (x, i)
        
__all__ = ['bisection', 'test_bisection', 'get_input', 'calc_vals']