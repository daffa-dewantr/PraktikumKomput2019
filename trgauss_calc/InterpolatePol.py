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

import main


def st(x, y, n_polinom):
    N = len(x)
    n_polinom += 1
    # Membuat matriks polinom interpolasi kolom 1
    ST = np.zeros((N, N))
    ST[:][0] += y
    ST = np.transpose(ST)
    # Memperbaharui matriks polinom interpolasi
    for j in range(1, n_polinom):
        for i in range(N - j):
            ST[i][j] = (ST[i + 1][j - 1] - ST[i][j - 1]) / (x[i + j] - x[i])
    return ST


def f_intp(xi, n_polinom):
    jum = ST[0][0]
    for i in range(1, n_polinom):
        suku = ST[0][i]
        for j in range(i):
            suku = suku * (xi - x_[j])
        jum = jum + suku
    return jum


def plot_intp(x_min, x_max):
    n = 100
    x_plot = np.linspace(x_min, x_max, n)
    y_plot = f_intp(x_plot, n_polinom)

    fig, ax = plt.subplots()
    ax.plot(x_, y_, 'ro', label='data')
    ax.plot(x_plot, y_plot, "g", label='garis interpolasi derajat')
    plt.xlabel("x")
    plt.ylabel("f(x) = y")
    plt.show()
    return


# ------------------------------------------------------------------------#

def input_data():
    x = []
    y = []
    while True:
        i_x = input("x: ")
        i_y = input("y: ")
        try:
            int(i_x)
            int(i_y)
        except:
            print("Data salah!!")
        else:
            x.append(i_x)
            y.append(i_y)
            i_exit = input("Data dimasukkan, Ketik q untuk kembali ke menu sebelumnya")
            if i_exit == 'q' or i_exit == 'Q':
                break
    x = np.array(x, dtype='float')
    y = np.array(y, dtype='float')
    return x, y


def lihat_data(graph=False):
    counter = 1
    print(f"no\t|\tx\t\ty")
    j = 0
    for i in x_:
        print(f"{counter}\t|\t{i}\t\t{y_[j]}")
        j += 1
        counter = counter + 1

    if graph is True:
        c = input("Masukkan y untuk melihat grafik: ")
        if c == 'y' or c == 'Y':
            fig, ax = plt.subplots()
            ax.plot(x_, y_, 'ro', label='data')
            plt.xlabel("x")
            plt.ylabel("y")
            plt.show()


def edit_data():
    global x_, y_

    print("------------------------")
    lihat_data()
    print("------------------------")

    i_no = input("Nomor data yang diedit: ")
    i_xy = input("x/y: ")
    try:
        i_no = int(i_no)
    except:
        print("Terjadi kesalahan!")
    else:
        print("------------------------")
        i_no = i_no - 1
        if i_xy == 'x' or i_xy == 'X':
            print(x_[i_no])
            i_x = input("Nilai baru: ")
            try:
                int(i_x)
            except:
                print("Angka yang dimasukkan salah!")
            else:
                x_[i_no] = i_x
        if i_xy == 'y' or i_xy == 'Y':
            print(y_[i_no])
            i_y = input("Nilai baru: ")
            try:
                int(i_y)
            except:
                print("Angka yang dimasukkan salah!")
            else:
                y_[i_no] = i_y
        print("Data diperbaharui")
    return


def tambah_data():
    global x_, y_
    while True:
        i_x = input("x: ")
        i_y = input("y: ")
        try:
            i_x = int(i_x)
            i_y = int(i_y)
        except:
            print("Data salah!!")
        else:
            x_ = np.append(x_, i_x)
            y_ = np.append(y_, i_y)
            i_exit = input("Data dimasukkan, Ketik q untuk kembali ke menu sebelumnya")
            if i_exit == 'q' or i_exit == 'Q':
                break


def choice():
    while True:
        try:
            i = int(input("Masukan menu untuk melanjutkan: "))
        except ValueError:
            print("Angka yang dimasukkan salah!")
            print("------------------------")
        else:
            break
    return i


def interpol_interface():
    """Gauss Interface Program
    """
    global x_, y_, n_polinom
    global ST
    global xi_, yi_

    n_polinom = 0
    x_ = np.arange(0)
    y_ = np.arange(0)
    xi_ = np.arange(0)
    yi_ = np.arange(0)

    while True:
        print("========================")
        print("1. Input/Edit Data")
        print("2. Tampilkan data")
        print("3. Masukkan derajat polinom")
        print("4. Taksir titik x")
        print("5. Tampilkan grafik interpolasi")
        print("6. Kembali ke menu sebelumnya")
        print("0. Kembali ke menu utama")
        print("99. Exit program")
        c = choice()
        if c == 1:
            print("========================")
            print("1. Input data secara manual")
            print("2. Input data dari file")
            print("3. Edit data")
            print("4. Tambah data")
            c = choice()
            if c == 1:
                x_, y_ = input_data()
            if c == 2:
                """
                Input data dari file
                """
                pass
            if c == 3:
                try:
                    edit_data()
                except:
                    print("Data belum ada.")
            if c == 4:
                try:
                    tambah_data()
                except:
                    print("Data belum ada.")
        elif c == 2:
            print("------------------------")
            lihat_data()
            print("------------------------")
            input("Enter untuk melanjutkan...")
        elif c == 3:
            print("------------------------")
            print("Derajat polinom sebelumnya adalah: ")
            if n_polinom == 0:
                print("Belum diinput")
            else:
                print(n_polinom)
            print("------------------------")
            while True:
                n_polinom = input("Masukkan derajat polinom yang baru: ")
                try:
                    n_polinom = int(n_polinom)
                except:
                    print("Angka yang dimasukkan salah!!")
                else:
                    break

        elif c == 4:
            try:
                ST = st(x_, y_, n_polinom)
            except:
                print("Terjadi kesalahan!")
            else:
                while True:
                    i_xi = input("Masukkan x yang ingin ditaksir: ")
                    try:
                        i_xi = int(i_xi)
                    except:
                        print("Angka yang dimasukkan salah!")
                    else:
                        break
                i_yi = f_intp(i_xi, n_polinom)
                yi_ = np.append(yi_, i_yi)
                xi_ = np.append(xi_, i_xi)
                print("Nilai pada x yang ditaksir adalah: ")
                print(i_yi)
                input("Tekan enter untuk melanjutkan..")

        elif c == 5:
            ST = st(x_, y_, n_polinom)
            x_min = np.amin(x_)
            x_max = np.amax(x_)
            plot_intp(x_min, x_max)

        elif c == 6:
            main.main()
        elif c == 0:
            main.main()
        elif c == 99:
            break
        else:
            pass


# --------------------------------------------------------------#

if __name__ == '__main__':
    interpol_interface()
