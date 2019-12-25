# in command line: python -m unittest test.test_equations

import unittest

from pygrapher.equations import *
from scipy import optimize

class TestEquations(unittest.TestCase):
    longMessage = True

    def test_linear(self):
        lin = linear()
        print(type(lin.get_function))
        self.assertEqual(lin.get_funcstr(), 'k0 + k1 * x', 'Linear String Has Problem')
        self.assertEqual(lin.get_vars(), ['k0', 'k1'], 'Linear Vars Has Problem')
        model = optimize.curve_fit(lin.get_function, [0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5])
        print(model)
        
    # def test_poly(self):
    #     pol = poly(2)
    #     funcstr = pol.get_funcstr()
    #     get_var = pol.get_vars()
    #     self.assertEqual(funcstr, 'k0 * x ** 0 + k1 * x ** 1 + k2 * x ** 2', msg = 'Poly String Has Problem')
    #     self.assertEqual(get_var, ['k0', 'k1', 'k2'], msg = 'Ploy Vars Has Problem')

    def test_exponential(self):
        exe = exponential()
        ex2 = exponential(2)
        self.assertEqual(exe.get_funcstr(), 'b + exp(x)',  msg = 'Exp String for e Has Problem')
        self.assertEqual(ex2.get_vars(), ['b', 'a'], msg = 'Exp String for Others Has Problem')

    def test_logarithm(self):
        lo = logarithm()
        self.assertEqual(lo.get_funcstr(), 'b + log(x, a)', msg = 'Log String Has Problem')
