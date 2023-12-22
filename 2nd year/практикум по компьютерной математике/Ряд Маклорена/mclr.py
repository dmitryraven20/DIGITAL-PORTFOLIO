pi = 3.14
n = 1

def fact(x):
    if x == 0:
        return 1

    return fact(x-1) * x

def exp(x, n):
    d = 0
    for i in range(n):
        t = (x**i) / fact(i)
        d = d + t
    return d

def sinx(x,n):
    d = 0
    for i in range(n):
        t = (((-1)**i) / (fact(2*i)+1)) * (x**((2*i)+1))
        d = d + t
    return d

def cosx(x,n):
    d = 0
    for i in range(n):
        t = (((-1)**i) / (fact(2*i))) * (x**(2*i))
        d = d + t
    return d

def arcsinx(x,n):
    d = 0
    for i in range(n):
        t = ((fact(2*i) / (4**i)*(fact(i)**2)*((2*i)+1))) * (x**((2*i)+1))
        d = d + t
    return d

def arccosx(x,n):
    d = 0
    for i in range(n):
        t = ((fact(2*i) / (4**i)*(fact(i)**2)*((2*i)+1))) * (x**((2*i)+1))
        d = d + t
    d = (pi/2) - d
    return d
