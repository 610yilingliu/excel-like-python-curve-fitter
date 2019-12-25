from pygrapher.grapher import *
from pygrapher.equations import *
import matplotlib.pyplot as plt
import numpy as np


def linear_fitter(x_array, y_origin, point_range, label = None, color = 'rand', legend = 'upper right',  show_scatter = True, point_size = 20):
    linear_func = linear()
    var_ls = fit(linear_func, x_array, y_origin)
    draw_fitted_normal(linear_func, var_ls, point_range, label, color, legend, show_scatter)
    if show_scatter:
        show_scatter(x_array, y_origin, color, point_size)

def poly_fitter(x_array, y_origin, point_range, label = None, color = 'rand', legend = 'upper right',  show_scatter = True, point_size = 20):
    fit_draw_poly

def exp_fitter(x_array, y_origin, point_range, label = None, color = 'rand', legend = 'upper right',  show_scatter = True, point_size = 20):
    exp_func = exponential()
    var_ls = fit(exp_func, x_array, y_origin)
    draw_fitted_normal(exp_func, var_ls, point_range, label, color, legend, show_scatter)
    if show_scatter:
        show_scatter(x_array, y_origin, color, point_size)

def log_fitter(x_array, y_origin, point_range, label = None, color = 'rand', legend = 'upper right',  show_scatter = True, point_size = 20):
    log_func = logarithm()
    var_ls = fit(log_func, x_array, y_origin)
    draw_fitted_normal(log_func, var_ls, point_range, label, color, legend, show_scatter)
    if show_scatter:
        show_scatter(x_array, y_origin, color, point_size)