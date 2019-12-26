from scipy import optimize
import matplotlib.pyplot as plt
import numpy as np
import re
import pandas as pd


def fit_draw_poly(n, x_array, y_origin, point_range, label = None, color = 'rand', legend = None, show_params = False, shown_digit = 2):
    '''
    use numpy.polyfit to fit polynominal functions
    '''
    if color == 'rand':
         # use random rgb color
        color = np.random.rand(3,)

    x_array = np.array(x_array)
    y_origin = np.array(y_origin)

    fitted_model = np.polyfit(x_array, y_origin, n)
    # put all variables in a regular list, and keep digit as setted
    var_ls = [round(item, shown_digit) for item in fitted_model]
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

    
def fit(choosed_equation, x_array, y_origin):
    '''
    Curve fitting
    '''
    var_ls = []
    x_array = np.array(x_array)
    y_origin = np.array(y_origin)
    eq = choosed_equation()
    func = eq.get_function
    fit_model = optimize.curve_fit(func, x_array, y_origin)

    for item in fit_model[0]:
        var_ls.append(item)

    return var_ls


def draw_fitted_normal(choosed_equation, var_ls, point_range, label = None, color = 'rand', legend = None, show_params = False, shown_digit = 2):
    '''
    Use matplotlib to draw diagram
    '''
    if color == 'rand':
         # use random rgb color
        color = np.random.rand(3,)
    equation_str = choosed_equation.func_str
    cutted_eq = list(filter(None, re.split(r'[abck]', equation_str)))
    # string of that equation
    eq = ''
    for i in range(len(cutted_eq)):
        eq += cutted_eq[i] + str(var_ls[i])

    print(eq)
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


                                                                                                                     