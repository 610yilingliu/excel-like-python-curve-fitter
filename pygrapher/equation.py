from numpy import exp, log

def linear(x, k0, k1):
    return k0 + k1 * x

def exponential(x, a, b, c):
    return c + b * a ** x

def e_exponential(x, c, b):
    return c + b * exp(x)

def logarithm(x, c, b, a):
    b + c * log(x, a)

print(str(logarithm))

__all__ = ['linear', 'exponential', 'logarithm']