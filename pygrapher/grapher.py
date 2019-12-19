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
    fit_model = optimize.curve_fit(choosed_equation.function, x_array, y_origin)

    for item in fit_model[0]:
        var_ls.append(item)

    for ys in fit_model[1]:
        y_fitted.append(ys)

    return var_ls


def draw_fitted(choosed_equation, var_ls, point_range, label = None, color = 'rand', legend = None, show_scattter = False):
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

    if show_scattter:
        print('\n')
        df = {'Parameterss':choosed_equation.var,'Values':var_ls}
        df = pd.DataFrame(df)
        print(df)

def show_scatter(x_array, y_origin, color = 'rand', size = 20):
        if color == 'rand':
            color = np.random.rand(3,)
        plt.scatter(x_array[:], y_origin[:], size, color)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        