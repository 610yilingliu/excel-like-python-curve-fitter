from numpy import exp, log

# linear equation
class linear(object):

    func = 'k0 + k1 * x'

    # just for myself to study, we don't really need static method here
    @staticmethod
    def get_funcstr():
        return linear.func

    def get_function(self, x, k0, k1):
        return eval(self.func)

    @staticmethod
    def get_vars():
        return ['k0','k1']

# # ploynominal
# class poly():
#     def __init__(self,n):
#         func = ''
#         var = []
#         for i in range(n + 1):
#             func += ('k'+str(i)) + ' * '+ 'x ** ' + str(i) + ' + '
#             var.append('k'+str(i))
#         func = func[:-3]
            
#         self.func_str = func
#         self.var = var
#         siglist = var.copy()
#         siglist.insert(0, 'x')
#         self.siglist = tuple(siglist)

#     def get_sig(self):
#         tup = self.siglist
#         def make_sig(*names):
#             parms = [Parameter(name, Parameter.POSITIONAL_OR_KEYWORD)
#                     for name in names]
#             return Signature(parms)
#         return make_sig(*tup)

#     def get_function(self):
#         return eval(self.func_str)

#     def get_funcstr(self):
#         return self.func_str

#     def get_vars(self):
#         return self.var    


# exponential
class exponential(object):
    def __init__(self, a = 'e'):
        if a == 'e':
            self.func_str = 'c + b * exp(x)'
            self.var = ['b', 'c']
        else:
            self.func_str = 'c + b * a ** x'
            self.var = ['b', 'c', 'a']

    def get_funcstr(self,a):
        if a == 'e':
            func_str = 'b + exp(x)'
        func_str = 'b + a ** x'
        return func_str
    
    def get_function(self, a, b):
        return eval(self.func_str)
    
    def get_e_function(self, b)

    def get_vars(self):
        return self.var  


# x = log(a)N
class logarithm():
    def __init__(self):
        self.func_str = 'b + log(x, a)'
        self.var = ['b', 'a']

    def get_funcstr(self):
        return self.func_str
        
    def get_function(self, x, b, a):
        return eval(self.func_str)

    def get_vars(self):
        return self.var


__all__ = ['linear', 'exponential', 'logarithm']