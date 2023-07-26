import scipy.misc
import time as t

def f(x):                           
    return (5*x + 8) / (1-(x**2))
start = t.time()
for i in range (10):
    result = scipy.misc.derivative(f, 8, dx=1e-6)
konec = t.time()

print(konec - start)
