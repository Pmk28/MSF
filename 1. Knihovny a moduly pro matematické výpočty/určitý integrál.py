from scipy import integrate
import time as t

def f(x):
    return x**2

def Scipy(a,b):
    start = t.time()
    for i in range(100):
        vysledek = integrate.quad(lambda x: x**2, a, b)
    konec = t.time()
    
    return (konec - start,vysledek)

vysledek = Scipy(0,1)
print(f"Scipy: {vysledek[0]}")


a = 0
b = 1
n = 100000000 #počet subintervalů

s = (b-a)/n #šířka každého intervalu
integral=0
start = t.time()
for i in range(n):
    x = a + i*s  # Aktuální hodnota x pro daný subinterval
    integral += f(x)

aproximace = integral * s
konec = t.time()
print(f"Bez Scipy:{konec - start}")
