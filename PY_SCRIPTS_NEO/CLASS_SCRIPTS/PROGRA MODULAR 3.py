import math

def t(x):
    res = (6 * x**2)
    return res

def g(x):
    res =(4 * x) + 5 - t(x)
    return res

def h(x):
    res = math.sqrt(2*x)
    return res

def k(x):
    res = (x**3) - (15 * x)
    return res

def f(x):
    res = (g(x) * h(x))/(k(x) * t(x))
    return res

if __name__ == "__main__":
    x = 1
    y = f(x)
    print(y)