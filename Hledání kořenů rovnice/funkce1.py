import sympy as sp
import time as t

#uzavřená metoda
x = sp.symbols('x')
funkce = (x - 2)*(x**2 + 3*x + 1)

# Rovnice kvadratického polynomu
start = t.time()
reseni = sp.solve(funkce, x)
konec = t.time()
print(f"čas: {konec-start},{reseni}")

#otevřená metoda
def polynomial_function(x):
    return (x - 2)*(x**2 + 3*x + 1)

def numerical_derivative(func, x, epsilon=1e-6):
    return (func(x + epsilon) - func(x)) / epsilon

def newton_method_efficient(initial_guess, tolerance, max_iterations):
    x_n = initial_guess
    for _ in range(max_iterations):
        f_xn = polynomial_function(x_n)
        f_prime_xn = numerical_derivative(polynomial_function, x_n)
        
        x_n1 = x_n - f_xn / f_prime_xn
        
        if abs(x_n1 - x_n) < tolerance:
            return x_n1
        x_n = x_n1
    return None

initial_guess = 0.0
tolerance = 1e-6
max_iterations = 100

start = t.time()

for i in range(100):
    root = newton_method_efficient(initial_guess, tolerance, max_iterations)

konec = t.time()
print(f"čas: {konec-start},{root}")
