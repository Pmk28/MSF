import time
import numpy as np

vektor = 100000

def Soucet():
    start = time.time()
    v1 = range(vektor)
    v2 = range(vektor)
    v3 = [v1[i] + v2[i] for i in range(len(v1)) ]
    konec = time.time()
    return konec - start

def SoucetNumPy():
    start1 = time.time()
    v1 = np.arange(vektor)
    v2 = np.arange(vektor)
    v3 = v1 + v2
    konec1 = time.time()
    return konec1 - start1


f1 = Soucet()
f2 = SoucetNumPy()
if f1 > f2:
    porovnani = "rychlejsi"
elif f1 < f2:
    porovnani = "pomalejsi"
else:
    porovnani = "stejne rychlé"
print(f"Bez NumPy: {f1} S NumPy: {f2}")
print(f"Numpy je {f1/f2} {porovnani}")
