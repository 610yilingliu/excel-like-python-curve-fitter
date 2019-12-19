from grapher import fit, draw, show_scatter
from equations import linear_func, poly_func, exp_func, log_func
import matplotlib.pyplot as plt


def linear_fitter(x_array, y_origin, point_range, label = None, color = 'rand', legend = 'upper right',  show_scatter = True, point_size = 20):
    var_ls = fit(linear_func, x_array, y_origin)
    draw(linear_func, var_ls, point_range, label, color, legend, show_scatter)
    if show_scatter:
        show_scatter(x_array, y_origin, color, point_size)

def poly_fitter(x_array, y_origin, point_range, label = None, color = 'rand', legend = 'upper right',  show_scatter = True, point_size = 20):
    var_ls = fit(poly_func, x_array, y_origin)
    draw(poly_func, var_ls, point_range, label, color, legend, show_scatter)
    if show_scatter:
        show_scatter(x_array, y_origin, color, point_size)

def exp_fitter(x_array, y_origin, point_range, label = None, color = 'rand', legend = 'upper right',  show_scatter = True, point_size = 20):
    var_ls = fit(exp_func, x_array, y_origin)
    draw(exp_func, var_ls, point_range, label, color, legend, show_scatter)
    if show_scatter:
        show_scatter(x_array, y_origin, color, point_size)

def log_fitter(x_array, y_origin, point_range, label = None, color = 'rand', legend = 'upper right',  show_scatter = True, point_size = 20):
    var_ls = fit(log_func, x_array, y_origin)
    draw(log_func, var_ls, point_range, label, color, legend, show_scatter)
    if show_scatter:
        show_scatter(x_array, y_origin, color, point_size)