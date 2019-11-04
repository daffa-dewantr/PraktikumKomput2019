# -*- coding: utf-8 -*-
"""Trapezoidal.py
[kelompok 1]

function:
    trap(a,x_min,x_max,N=1000) return hasil integral
    a adalah koefisien polinomial:
        a = [an,an-1,an-2,...,a0]
        y = an*x**n + an-1*x**n-1 + an-2*x**n-2 + ... + a0
    x_min, x_max merupakan batas integral
    N merupakan jumlah step dalam integral metode trapezoidal.
        Default N=1000, semakin besar semakin tepat nilainya
"""
import numpy as np

#input
a = np.array([1,0,0])

def trap(a, x_min, x_max, N=1000):
    """N = jumlah grid
    """

    fx = ''        
    q = len(a)-1
    for i in a:
        if i != a[0]:
            fx += '+'
        fx += '%s*x**%s' % (i,q)
        q-=1
    
    def f(x):
        x = x
        return eval(fx)
    
    h=(x_min-x_max)/N   #lebar grid
    jum=0.5*f(x_min)
    for i in range (1,N):
        xi = x_min+h*i
        jum = jum+f(xi)
    jum = jum + 0.5 * f(x_max)
    hasil = jum * h
    return hasil
    