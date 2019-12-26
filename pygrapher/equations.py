from numpy import exp, log

# linear equation
class linear:

    func = 'x * k + b'

    def get_funcstr(self):
        return self.func

    def get_function(self, x, k ,b):
        return eval(self.func)

    @staticmethod
    def get_vars():
        return ['k','b']


# exponential (e based)
class e_exponential:

    func = 'exp(x) + b'
    
    def get_funcstr(self):
        return self.func
    
    def get_function(self, x, b):
        return eval(self.func)

    @staticmethod
    def get_vars():
        return ['b']

# exponential (other based)
class exponential:

    func = 'exp(x) + b'

    def get_funcstr(self):
        return self.func
    
    def get_function(self, x, a, b):
        return eval(self.func)

    @staticmethod
    def get_var():
        return['a', 'b']

class e_exponential_with_param:

    func = 'exp(x) * k + b'

    def get_funcstr(self):
        return self.func
    
    def get_function(self, x, k, b):
        return eval(self.func)

    @staticmethod
    def get_vars():
        return ['k', 'b']

class exponential_with_param:
    
    func = ' k * a ** x + b'
    def get_funcstr(self):
        return self.func
    
    def get_function(self, x, k, a, b):
        return eval(self.func)

    @staticmethod
    def get_vars():
        return['k', 'a', 'b']

# x = log(a)N
class logarithm:
    func = 'log(x, a) + b'

    def get_funcstr(self):
        return self.func
        
    def get_function(self, x, a, b):
        return eval(self.func)

    @staticmethod
    def get_vars():
        return ['a', 'b']

class logarithm_with_param:
    func = ' b + k * log(x, a)'

    def get_funcstr(self):
        return self.func
    
    def get_function(self, x, k, a, b):
        return eval(self.func)

    @staticmethod
    def get_vars():
        return ['k', 'a', 'b']