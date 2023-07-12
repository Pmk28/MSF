from scipy import integrate
import time as t

def Scipy(a,b):
    start = t.time()
    vysledek1 = integrate.quad(lambda x: x**2, a, b)
    print(vysledek1)
    konec = t.time()
    return konec - start

vysledek = Scipy(0,1)
print(f"Čas: {vysledek}")
