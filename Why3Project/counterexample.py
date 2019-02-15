import math
import random
from decimal import *

b = 4
max_n = 3
max_m = 3

getcontext().prec = 100

def B(n):
    return Decimal(b) ** n

def pick_x(xm,m):
    return Decimal(xm + random.random())*B(-m)

def compute_xn(x,n):
    return int(x*B(n))

def inv_real(x):
    return Decimal(1) / x

def thesis_inv(x,n,m):
    if n <= -m:
        return 0
    else:
        k = n+2*m+1
        xk = compute_xn(x,k)
        assert xk != -1 and xk != 0 and xk != 1
        if xk > 1:
            return int(math.ceil(B(k+n)/xk))
        else:
            return int(math.floor(B(k+n)/xk))

def project_inv(x,n,m):
    if n <= -m:
        return 0
    else:
        k = n+2*m+1
        xk = compute_xn(x,k)
        assert xk != -1 and xk != 0 and xk != 1
        return int(round(B(k+n)/xk, 0))

def ineq_ok(x, xn, n):
    assert Decimal(xn-1)*B(-n) < Decimal(xn+1)*B(-n)
    return Decimal(xn-1)*B(-n) < x and x < Decimal(xn+1)*B(-n)

# We take m and xm as parameters, and we pick a value for x from them, because it is simpler this way.
# (We could also take a random x as parameter and compute m and xm for this x)
def _check(m,n,xm): # abs(xm) must be strictly greater than 1
    x = pick_x(xm,m)
    inv_t_xn = thesis_inv(x,n,m)
    inv_p_xn = project_inv(x,n,m)
    inv_x = inv_real(x)
    assert ineq_ok(inv_x, inv_p_xn, n)
    res = ineq_ok(inv_x, inv_t_xn, n)
    if not res:
        print ("CE for m={m} and n={n}".format(m=m,n=n))
        print ("x={x}".format(x=x))
        print ("1/x={inv_x}".format(inv_x=inv_x))
        print ("1/xn(project)={inv_xn}".format(inv_xn=inv_p_xn))
        print ("1/xn(thesis)={inv_xn}".format(inv_xn=inv_t_xn))
        print ("")
    return res

def check(m,n):
    for i in range(2,2*b):
        if not (_check(m,n,-i) and _check(m,n,i)):
            return False
    return True

for m in range(0, max_m):
    for n in range(0, max_n):
        if not check(m,n):
            #print ("CE for m={m} and n={n}".format(m=m,n=n))
            pass

