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

import main

# Input
xi = np.array([1])


def reg(x, y):
    n = x.size
    x_total = np.sum(x)
    y_total = np.sum(y)
    x_sq_total = np.sum(x ** 2)
    xy_total = np.sum(x * y)
    # Cari persamaan regresi
    b = (n * xy_total - x_total * y_total) / (n * x_sq_total - (x_total) * x_total)
    a = y_total / n - b * x_total / n
    return a, b


def f_reg(xi_):
    a_, b_ = reg(x_, y_)
    return a_ + b_ * xi_


def plot_reg(x, y, N=100):
    # a, b = reg(x, y)

    x_min = np.hstack((x, xi_)).min()
    x_max = np.hstack((x, xi_)).max()

    yi = f_reg(xi)
    x_plot = np.linspace(x_min, x_max, N)
    y_plot = f_reg(x_plot)

    fig, ax = plt.subplots()
    ax.plot(x, y, 'ro', label='data')
    ax.plot(xi, yi, 'bs', label='titik yang diestimasi')
    ax.plot(x_plot, y_plot, 'g', label='garis regresi')
    plt.xlabel("x")
    plt.ylabel("f(x) = y")
    plt.show()
    return


# ---------------------------------------------------------------------#


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


def regression_interface():
    """Regression Interface Program
    """
    global x_, y_
    global a_, b_
    global xi_, yi_

    x_ = np.arange(0)
    y_ = np.arange(0)
    xi_ = np.arange(0)
    yi_ = np.arange(0)

    while True:
        print("========================")
        print("1. Input/Edit Data")
        print("2. Tampilkan data")
        print("3. Taksir titik x")
        print("4. Tampilkan grafik regresi")
        print("5. Kembali ke menu sebelumnya")
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
            try:
                a_, b_ = reg(x_, y_)
            except:
                print("Data belum diinput!")
            else:
                while True:
                    i_xi = input("Masukkan x yang ingin ditaksir: ")
                    try:
                        i_xi = int(i_xi)
                    except:
                        print("Angka yang dimasukkan salah!")
                    else:
                        break
                i_yi = f_reg(i_xi)
                yi_ = np.append(yi_, i_yi)
                xi_ = np.append(xi_, i_xi)
                print("Nilai pada x yang ditaksir adalah: ")
                print(i_yi)
                input("Tekan enter untuk melanjutkan..")
        elif c == 4:
            try:
                plot_reg(x_, y_)
            except:
                print("Data belum diinput!")
        elif c == 5:
            main.main()
        elif c == 0:
            main.main()
        elif c == 99:
            break
        else:
            pass


# ----------------------------------------------------#

if __name__ == "__main__":
    regression_interface()
