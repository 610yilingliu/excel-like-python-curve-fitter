from scipy import optimize
import matplotlib.pyplot as plt
import numpy as np
import re
import pandas as pd


def fit(choosed_equation, x_array, y_origin):
    '''
    Curve fitting
    '''
    var_ls = []
    y_fitted = []
    fit_model = optimize.curve_fit(choosed_equation.get_function, x_array, y_origin)

    for item in fit_model[0]:
        var_ls.append(item)

    # for r-squared
    for ys in fit_model[1]:
        y_fitted.append(ys)

    return var_ls, y_fitted

def fit_draw_poly(n, x_array, y_origin, point_range, label = None, color = 'rand', legend = None, show_params = False):
    '''
    use numpy.polyfit to fit polynominal functions
    '''
    if color == 'rand':
         # use random rgb color
        color = np.random.rand(3,)

    x_array = np.array(x_array)
    y_origin = np.array(y_origin)

    fitted_model = np.polyfit(x_array, y_origin, n)
    # put all variables in a regular list
    var_ls = [item for item in fitted_model]
    # reverse list, so the variables will start from k0
    var_ls = var_ls[::-1]
    # maximun n for x ** n
    poly_max = len(var_ls)
    func_str = ''

    var_name = []
    for i in range(poly_max):
        func_str += str(var_ls[i]) + ' * x^' + str(i) + ' + '
        var_name.append('k' + str(i))
    func_str = func_str[:-3]
    print(func_str)

    x = np.arange(point_range[0], point_range[1], 0.01)
    y_np = np.polyval(fitted_model, x)

    if label != None:
        plt.plot(x, y_np, color, label)
    plt.plot(x, y_np, color)

    if legend != None:
        try:
            plt.legend(loc = legend)
        except:
            raise Exception('Location not match, please read matplotlib.pyplot legend location for details.')

    if show_params:
        print('\n')
        df = {'Parameterss':var_name,'Values':var_ls}
        df = pd.DataFrame(df)
        print(df)

    



def draw_fitted_normal(choosed_equation, var_ls, point_range, label = None, color = 'rand', legend = None, show_params = False):
    '''
    Use matplotlib to draw diagram
    '''
    if color == 'rand':
         # use random rgb color
        color = np.random.rand(3,)
    equation_str = choosed_equation.func_str
    cutted_eq = list(filter(None, re.split(r'k\d+|[ab]', equation_str)))
    # string of that equation
    eq = ''
    for i in range(len(cutted_eq)):
        eq += str(var_ls[i]) + cutted_eq[i]
    x = np.arange(point_range[0], point_range[1], 0.01)
    y_np = eval(eq)

    if label != None:
        plt.plot(x, y_np, color, label)
    plt.plot(x, y_np, color)

    if legend != None:
        try:
            plt.legend(loc = legend)
        except:
            raise Exception('Location not match, please read matplotlib.pyplot legend location for details.')
    print(eq)

    if show_params:
        print('\n')
        df = {'Parameterss':choosed_equation.var,'Values':var_ls}
        df = pd.DataFrame(df)
        print(df)

def show_scatter(x_array, y_origin, color = 'rand', point_size = 20):
        if color == 'rand':
            color = np.random.rand(3,)
        plt.scatter(x_array[:], y_origin[:], point_size, color)



__all__ = ['fit', 'fit_draw_poly', 'draw_fitted_normal', 'show_scatter']                                                                                                                           