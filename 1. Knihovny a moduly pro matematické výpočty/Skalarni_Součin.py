import numpy as np
import time as t

v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
start = t.time()
for i in range(10000):
    vysledek = v1 @ v2
konec = t.time()
cas_numpy = konec - start
print(f"Numpy: {cas_numpy}")

def skalarni_soucin(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError("Vektory musí mít stejnou délku!")
    
    vysledek = 0
    start = t.time()
    for i in range(10000):
        for i in range(len(vector1)):
            vysledek += vector1[i] * vector2[i]
    konec = t.time()
    
    return konec - start


v1 = [1, 2, 3]
v2 = [4, 5, 6]
cas = skalarni_soucin(v1, v2)
print(f"Bez Numpy: {cas}")

if cas_numpy > cas:
    print(f"Numpy je {cas_numpy/cas}-krát pomalejší!")
elif cas_numpy < cas:
    print(f"Numpy je {cas/cas_numpy}-krát rychlejší!")
else:
    print("Numpy je stejně rychlé!")
