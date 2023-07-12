import numpy as np
import time

mat1 = [[2,3,1,5,6,7],
        [1,3,2,5,6,7],
        [2,4,3,5,6,7],
        [2,6,2,5,6,7],
        [1,3,2,5,6,7],
        [1,3,2,5,6,7]]
mat2 = [[1,2,1,5,6,7],
        [3,4,3,5,6,7],
        [2,6,2,5,6,7],
        [2,6,2,5,6,7],
        [1,3,2,5,6,7],
        [1,3,2,5,6,7]]


def součin_matic(matice1, matice2):
    start = time.time()
    for i in range(100):
        if len(matice1[0]) != len(matice2):
            raise ValueError("Tyto matice se nedají násobit!")

    
        vysledek = [[0 for i in range(len(matice2[0]))] for i in range(len(matice1))]

    
        for i in range(len(matice1)):
            for j in range(len(matice2[0])):
                for k in range(len(matice2)):
                    vysledek[i][j] += matice1[i][k] * matice2[k][j]
    konec = time.time()
    
    return (vysledek,konec - start)

def součin_matic_numpy(matice1,matice2):
    start = time.time()
    for i in range(100):
        result = np.dot(matice1, matice2)
    konec = time.time()
    
    return (result,konec - start)
    



vysledek = součin_matic(mat1, mat2)
print(f"Bez numpy: {vysledek[1]}")

vysledek_numpy = součin_matic_numpy(mat1,mat2)
print(f"S numpy: {vysledek_numpy[1]}")

if vysledek[1] > vysledek_numpy[1]:
    print(f"Numpy je {vysledek[1]/vysledek_numpy[1]}krát rychlejší!")
elif vysledek[1] < vysledek_numpy[1]:
    print(f"Numpy je {vysledek_numpy[1]/vysledek[1]}krát pomalejší!")
else:
    print("Numpy je stejne rychle!")



