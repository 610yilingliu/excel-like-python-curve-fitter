from numpy import exp, log

# linear equation
class linear():
    def __init__(self, x, k0, k1):
        self.func_str = 'k0 + k1 * x'
        self.var = ['k0','k1']

    def get_funcstr(self):
        return self.func_str

    def get_function(self):
        return eval(self.func_str)

    def get_vars(self):
        return self.var

# ploynominal
class poly():
    def __init__(self, x, n):
        func = ''
        var = []
        for i in range(n + 1):
            func += ('k'+str(i)) + ' * '+ 'x ** ' + str(i) + ' + '
            var.append('k'+str(i))
        func = func[:-3]
            
        self.func_str = func
        self.var = var

    def get_funcstr(self):
        return self.func_str
        
    def get_function(self):
        return eval(self.func_str)

    def get_vars(self):
        return self.var    

# exponential
class exponential():
    def __init__(self, x, b, a = 'e'):
        if a == 'e':
            self.func_str = 'b + exp(x)'
            self.var = ['b']
        else:
            self.func_str = 'b + a ** x'
            self.var = ['b', 'a']

    def get_funcstr(self):
        return self.func_str
        
    def get_function(self):
        return eval(self.func_str)

    def get_vars(self):
        return self.var  


# x = log(a)N
class logarithm():
    def __init__(self, x, a, b):
        self.func_str = 'b + log(x, a)'
        self.var = ['b', 'a']

    def get_funcstr(self):
        return self.func_str
        
    def get_function(self):
        return eval(self.func_str)

    def get_vars(self):
        return self.var