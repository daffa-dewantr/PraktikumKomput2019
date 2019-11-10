# -*- coding: utf-8 -*-
"""InterpolatePol.py
[kelompok 1]

input = x,
        y,
        n_polinom --> derajat interpolasi yg diinginkan
        
function:
    St(x,y,n_polinom) return matriks ST untuk mencari fungsi interpolasi
    f_intp(xi) return y interpolasi dari data x dan y
    plot_intp() return gambar plot persamaan interpolasi dari data (x,y)
"""
import numpy as np
import matplotlib.pyplot as plt

#Input
x = np.array([0.0,1.0,2.5,3.0,4.0])
y = np.array([1,0.5,-0.4161,-1.9900,-2.6536])
n_polinom = 5

def St(x,y,n_polinom):
    N = len(x)
    n_polinom += 1
    #Membuat matriks polinom interpolasi kolom 1
    ST = np.zeros((N, N))
    ST[:][0] += y
    ST = np.transpose(ST)
    #Memperbaharui matriks polinom interpolasi
    for j in range (1,n_polinom):
        for i in range(N-j):
            ST[i][j] = (ST[i+1][j-1] - ST[i][j-1])/(x[i+j]-x[i])
    return ST

def f_intp(xi):   
    jum = ST[0][0]
    for i in range(1,n_polinom):
        suku = ST[0][i]
        for j in range(i):
            suku = suku*(xi-x[j])
        jum = jum + suku
    return jum
    
def plot_intp(x_min, x_max):
    N = 100    
    x_plot = np.linspace(x_min, x_max,N)
    y_plot = f_intp(x_plot)
    
    fig, ax = plt.subplots()
    ax.plot(x,y, 'ro', label='data')
    ax.plot(x_plot, y_plot, "g", label='garis interpolasi derajat')
    plt.xlabel("x")
    plt.ylabel("f(x) = y")
    plt.show()
    return

ST = St(x,y,n_polinom)

