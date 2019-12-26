# in command line: python -m unittest test.test_grapher
import unittest

from pygrapher.grapher import *
from pygrapher.equations import linear

class TestGrapher(unittest.TestCase):
    longMessage = True

    def test_fit(self):
        test_eq = linear
        x_array = [0, 1, 2]
        y_array = [0, 1, 2]
        print(fit(test_eq, x_array, y_array))

    def test_draw_fitted_normal(self):
        test_eq = linear
        x_array = [0, 1, 2]
        y_array = [0, 1, 2]


if __name__ == "__main__":
    TestGrapher().test_fit()