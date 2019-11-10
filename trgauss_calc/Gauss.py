# -*- coding: utf-8 -*-
"""InterpolatePol.py
[kelompok 1]
"""
import numpy as np

"""
a = np.array([[2.0, 7.0, 5.0, 5.0], 
              [3.0, 6.0, 8.0, 2.0], 
              [5.0, 4.0, 9.0, 1.0], 
              [2.0, 7.0, 5.0, 1.0]])
b=[14.0, 17.0, 18.0, 20.0]

#a = np.array([[2.0, 7.0, 5.0], 
#              [3.0, 6.0, 8.0], 
#              [5.0, 4.0, 9.0]])
#b=[14.0, 17.0, 18.0]
"""

def gauss(a, b):
    """
    gauss(a,b) return x yang dicari dengan persamaan gauss dari koefisien polinom a
    a dan b adalah koefisien polinomial:
        a = [an,an-1,an-2,...,a0]
        b = an*x**n + an-1*x**n-1 + an-2*x**n-2 + ... + a0
    """
    n = len(a)
    ai = np.copy(a)
    bi = np.copy(b)
    a_temp = np.copy(a)
    # P merupakan jumlah pengulangan kode sebanyak derajat polinom yang dicari
    for p in range(0, 2):
        # Menyamakan baris
        for i in range(p, n):
            for j in range(p, n):
                if a_temp[j][p] != 0:
                    ai[i][p::] *= a_temp[j][p]
                bi[i] *= a_temp[j][p]
            if a_temp[i][p] != 0:
                ai[i][p::] /= a_temp[i][p]
                bi[i] /= a_temp[i][p]
        # Eliminasi
        for i in range(p + 1, n):
            ai[i][p::] -= ai[p][p::]
            bi[i] -= bi[p]
        # Cari nilai x dengan mengalikan a inverse dengan b
        x = np.linalg.inv(ai).dot(bi)
        return x


# --------------------------------------------------------------------------------------------#

def input_polinom(n):
    """n=derajat polinom
    """
    n = n
    a = np.zeros((n, n))
    b = np.zeros(n)
    print(f"Input polinomial derajat {n}")
    for i in range(0, n):
        print("|", end=' ')
        for j in range(0, n):
            print(f"a{i}{j}", end=' ')
            if j == n - 1:
                print(f"| |x{i}|  |b{i}|")
    for i in range(0, n):
        for j in range(0, n):
            while True:
                try:
                    print(f"a[{i}][{j}] = ", end='')
                    a[i][j] = int(input())
                except:
                    print('......You did not enter a valid integer! Try again!')
                else:
                    break
        while True:
            try:
                print(f"b[{i}] = ", end='')
                b[i] = int(input())
            except:
                print('......You did not enter a valid integer! Try again!')
            else:
                break

    return a, b


def lihat_polinom():
    global a_, b_
    n = len(a_)
    for i in range(0, n):
        print("|", end=' ')
        for j in range(0, n):
            print(f"{a_[i][j]}", end=' ')
            if j == n - 1:
                print(f"| |x{i}|  |{b_[i]}|")


def input_file():
    print("------------------------")
    file = input("Lokasi file: ")
    print("------------------------")
    input("Tekan enter untuk melanjutkan.. (kembali ke menu sebelumnya)")
    global a_, b_, j
    line = []
    a = []
    b = []
    with open(file, 'r') as r:
        for l in r:
            line.append(l)
    n = len(line)
    for i in range(n):
        line_split = line[i].split()
        for j in range(n):
            a.append(line_split[j])
        j += 1
        b.append(line_split[j])

    a_ = np.array(a, dtype='float').reshape(n, n)
    b_ = np.array(b, dtype='float')
    return


def output_file():
    print("------------------------")
    file = input("Lokasi file: ")
    print("------------------------")
    input("Tekan enter untuk melanjutkan.. (kembali ke menu sebelumnya)")
    x_ = gauss(a_, b_)
    with open(file, 'x') as w:
        for i in x_:
            w.write(f"{i} ")
    return


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


def question(n):
    """
    n = derajat polinomial
    """
    global a_, b_, x_
    while True:
        print("------------------------")
        print("Pilih:")
        print("1. Input soal secara manual")
        print("2. Input soal dari file")
        print("3. Lihat soal(persamaan)")
        print("4. Hitung solusi")
        print("5. Tulis solusi ke dalam file")
        print("6. Kembali ke menu sebelumnya")
        print("0. Kembali ke menu utama")
        print("------------------------")
        a = choice()
        if a == 1:
            a_, b_ = input_polinom(n)
        elif a == 2:
            file = input_file()
        elif a == 3:
            try:
                lihat_polinom()
            except:
                print("...Soal belum diinput")
                input("Tekan enter untuk melanjutkan.. (kembali ke menu sebelumnya)")
        elif a == 4:
            try:
                x_ = gauss(a_, b_)
                print("------------------------")
                print(f"Solusi adalah: {x_}")
                print("------------------------")
                input("Tekan enter untuk melanjutkan.. (kembali ke menu sebelumnya)")
            except:
                print("...Soal belum diinput")
                input("Tekan enter untuk melanjutkan.. (kembali ke menu sebelumnya)")
        elif a == 5:
            output_file()
        elif a == 6:
            gauss_inf()
        elif a == 0:
            pass
        else:
            pass


def gauss_inf():
    """Gauss Interface Program
    """
    a_ = np.array(0)
    b_ = np.array(0)
    x_ = np.array(0)
    n_ = 0

    print("========================")
    print("1. Sistem Persamaan Linier (SPL) 3 Variabel")
    print("2. SPL 4 Variabel")
    print("3. SPL 5 Variabel")
    print("4. SPL 6 Variabel")
    print("5. SPL 7 Variabel")
    print("6. Kembali ke menu sebelumnya")
    print("0. Kembali ke menu utama")
    while True:
        a = choice()
        if a == 1:
            question(3)
        elif a == 2:
            question(4)
        elif a == 3:
            question(5)
        elif a == 4:
            question(6)
        elif a == 5:
            question(7)
        elif a == 6:
            pass
        elif a == 0:
            pass
        else:
            pass


# -------------------------------------------#

gauss_inf()
