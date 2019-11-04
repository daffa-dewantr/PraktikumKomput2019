# -*- coding: utf-8 -*-
"""InterpolatePol.py
[kelompok 1]

input = a,
        b,
        
function:
    gauss(a,b) return x yang dicari dengan persamaan gauss dari koefisien polinom a
    a dan b adalah koefisien polinomial:
        b = [an,an-1,an-2,...,a0]
        b = an*x**n + an-1*x**n-1 + an-2*x**n-2 + ... + a0 
"""
import numpy as np

a = np.array([[2.0, 7.0, 5.0, 5.0], 
              [3.0, 6.0, 8.0, 2.0], 
              [5.0, 4.0, 9.0, 1.0], 
              [2.0, 7.0, 5.0, 1.0]])
b=[14.0, 17.0, 18.0, 20.0]

#a = np.array([[2.0, 7.0, 5.0], 
#              [3.0, 6.0, 8.0], 
#              [5.0, 4.0, 9.0]])
#b=[14.0, 17.0, 18.0]

def gauss(a,b):
    n = len(a)
    ai = np.copy(a)
    bi = np.copy(b)
    a_temp = np.copy(a)
    #P merupakan jumlah pengulangan kode sebanyak derajat polinom yang dicari
    for p in range(0,2):
        #Menyamakan baris
        for i in range(p,n):
            for j in range(p,n):
                if a_temp[j][p] != 0:
                    ai[i][p::] *= a_temp[j][p]
                bi[i] *= a_temp[j][p]
            if a_temp[i][p] != 0:
                ai[i][p::] /= a_temp[i][p]
                bi[i] /= a_temp[i][p]
        #Eliminasi
        for i in range(p+1,n):
            ai[i][p::] -= ai[p][p::]
            bi[i] -= bi[p]
        a_temp = np.copy(ai)
        #Cari nilai x dengan mengalikan a inverse dengan b
        x = np.linalg.inv(ai).dot(bi)        
        return x
        
        
        