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
import matplotlib.pyplot as plt
import numpy as np


def trap(fx, x_min, x_max, N=1000):
    """N = jumlah grid
    """

    """
    fx = ''        
    q = len(a)-1
    for i in a:
        if i != a[0]:
            fx += '+'
        fx += '%s*x**%s' % (i,q)
        q-=1
    """

    fx = fx

    def f(x):
        return eval(fx)

    h = (x_min - x_max) / N  # lebar grid
    jum = 0.5 * f(x_min)
    for i in range(1, N):
        xi = x_min + h * i
        jum = jum + f(xi)
    jum = jum + 0.5 * f(x_max)
    hasil = jum * h
    return hasil


# -------------------------------------------------------------------------------------#


def choice():
    while True:
        try:
            i = int(input("Masukan menu untuk melanjutkan: "))
        except ValueError:
            print('......You did not enter a valid integer! Try again!')
            print("------------------------")
        else:
            break
    return i


def input_fx():
    while True:
        x = 0
        print("Gunakan ** untuk pangkat, * untuk kali, gunakan variabel x!")
        print("Contoh: 2*x**2+x+2")
        fx = input("input persamaan:")
        try:
            x = 0
            eval(fx)
        except:
            print("........Persamaan salah!")
        else:
            break
    return fx


def input_file():
    while True:
        print("------------------------")
        try:
            file = input("Lokasi file: ")
        except:
            print("File tidak ditemukan/salah!")
        with open(file, 'r') as r:
            fx = r.readline()
            try:
                x = 0
                eval(fx)
            except:
                print("........Persamaan salah!")
            else:
                break
    print("------------------------")
    input("Tekan enter untuk melanjutkan.. (kembali ke menu sebelumnya)")
    return fx


def output_file(fx):
    print("------------------------")
    file = input("Lokasi file: ")
    a = int(input("Masukkan batas bawah: "))
    b = int(input("Masukkan batas atas: "))
    N = int(input("Masukkan step: "))
    solusi_trap = trap(fx, a, b, N)
    with open(file, 'x') as w:
        w.write(solusi_trap)
    print("------------------------")
    input("Tekan enter untuk melanjutkan.. (kembali ke menu sebelumnya)")

    return


def graph_fx(fx):
    fx = fx

    def f(x):
        return eval(fx)

    a = int(input("Masukkan batas bawah: "))
    b = int(input("Masukkan batas atas: "))

    x = np.arange(a, b, 0.01)
    y = f(x)

    plt.plot(x, y)
    plt.show()
    pass


def trapezoidal_inf():
    """Gauss Interface Program
    """

    fx = ''
    solusi_trap = 0

    print("========================")
    print("1. Input persamaan manual")
    print("2. Input persamaan dari file")
    print("3. Tampilkan persamaan")
    print("4. Hitung solusi trapezoidal")
    print("5. Tulis solusi ke dalam file")
    print("6. Kembali ke menu sebelumnya")
    print("0. Kembali ke menu utama")
    while True:
        a = choice()
        if a == 1:
            fx = input_fx()
        elif a == 2:
            fx = input_file()
        elif a == 3:
            try:
                x = 0
                eval(fx)
            except:
                print("Persamaan belum ada...")
            else:
                graph_fx(fx)
        elif a == 4:
            print("------------------------")
            a = int(input("Masukkan batas bawah: "))
            b = int(input("Masukkan batas atas: "))
            N = int(input("Masukkan step: "))
            solusi_trap = trap(fx, a, b, N)
            print(f"Solusi adalah: {solusi_trap}")
            print("------------------------")
            input("Tekan enter untuk melanjutkan.. (kembali ke menu sebelumnya)")



        elif a == 5:
            output_file(fx)
        elif a == 6:
            pass
        elif a == 0:
            pass
        else:
            pass


trapezoidal_inf()
