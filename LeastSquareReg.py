# -*- coding: utf-8 -*-
"""LeastSquareReg.py
[kelompok 1]

function:
    reg(x,y) return a & b pada persamaan regresi
    f_reg(x) return y estimasi melalui persamaan regresi 
    plot_reg(x,y) return gambar plot regresi data (x,y) dan titik yang diestimasi

"""
import numpy as np
import matplotlib.pyplot as plt

#Input
x = np.array([0.1, 0.4, 0.5, 0.7, 0.7, 0.9])
y = np.array([0.61, 0.92, 0.99, 1.52, 1.47, 2.03])
xi = np.array([1])

def reg(x,y):
    n = x.size
    x_total = np.sum(x)
    y_total = np.sum(y)
    x_sq_total = np.sum(x**2)
    xy_total = np.sum(x*y)
    #Cari persamaan regresi
    b = (n * xy_total - x_total * y_total) / (n * x_sq_total - (x_total) * x_total)
    a = y_total/n - b * x_total/n
    return a,b

def f_reg(xi): 
    a,b = reg(x,y)
    return a + b * xi

def plot_reg(x,y,N=100):
    a,b = reg(x,y)

    x_min = np.hstack((x,xi)).min()
    x_max = np.hstack((x,xi)).max()

    yi = f_reg(xi)    
    x_plot = np.linspace(x_min, x_max,N)
    y_plot = f_reg(x_plot)
    
    fig, ax = plt.subplots()
    ax.plot(x, y, 'ro', label='data')
    ax.plot(xi, yi, 'bs', label='titik yang diestimasi')
    ax.plot(x_plot, y_plot, 'g', label='garis regresi')
    plt.xlabel("x")
    plt.ylabel("f(x) = y")
    plt.show()
    return

