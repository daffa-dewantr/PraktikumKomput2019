"""
Tugas Besar Komputasi Geofisika: Kelompok 1
---
Modul .py untuk semua menu dalam program
---
"""

import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


# ================================================================================#
# Main Function
# ================================================================================#

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


# ---------------------------------------------------------------#
def f_trap(fx):
    """fungsi penunjang metode trapezoidal. input string fx --> evaluate fx
    f = f_trap('2*x**2')
    f(2) --> 2*2**2 = 8
    """

    def f(x) -> float:
        return eval(fx)

    return f


def trapezoidal(f, x_min, x_max, n=1000) -> float:
    """input fx --> function, x_min, x_max. return hasil integrasi
    """
    h = (x_max - x_min) / n  # lebar grid
    jum = 0.5 * f(x_min)
    for i in range(1, n):
        xi = x_min + h * i
        jum = jum + f(xi)
    jum = jum + 0.5 * f(x_max)
    hasil = jum * h
    return hasil


# ------------------------------------------------------------------------------#

def least_square_regression(x, y):
    """membuat fungsi f dari hasil regresi:
    f = least_square_regression(np.array([1,2,3,4,5]), np.array([-12,-4,4,12,15]))
    f(xi) --> estimasi nilai pada xi
    """
    n = x.size
    x_total = np.sum(x)
    y_total = np.sum(y)
    x_sq_total = np.sum(x ** 2)
    xy_total = np.sum(x * y)
    # Cari persamaan regresi
    b = (n * xy_total - x_total * y_total) / (n * x_sq_total - x_total * x_total)
    a = y_total / n - b * x_total / n

    def f(xi):
        return a + b * xi

    return f


# --------------------------------------------------------------------------------#
def interpolate_polinom(x, y, n_polinom):
    """membuat fungsi f dari hasil interpolasi:
    f = least_square_regression(np.array([1,2,3,4,5]), np.array([-12,-4,4,12,15]), 5)
    f(xi) --> estimasi nilai pada xi
    """
    n = len(x)
    n_polinom += 1
    # Membuat matriks polinom interpolasi kolom 1
    ST = np.zeros((n, n))
    ST[:][0] += y
    ST = np.transpose(ST)
    # Memperbaharui matriks polinom interpolasi
    for i in range(1, n_polinom):
        for j in range(n - i):
            ST[j][i] = (ST[j + 1][i - 1] - ST[j][i - 1]) / (x[i + j] - x[j])

    def f(xi):
        jum = ST[0][0]
        for col in range(1, n_polinom):
            suku = ST[0][col]
            for row in range(col):
                suku = suku * (xi - x[row])
            jum = jum + suku
        return jum

    return f


# --------------------------------------------------------------------------------#

# ================================================================================#
# Main Program
# ================================================================================#

def clear():
    """Fungsi clear layar terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')


def choice():
    while True:
        try:
            i = int(input("Masukan menu untuk melanjutkan: "))
        except:
            pass
        else:
            break
    return i

def tentang_program():
    print("====================================")
    print("Tugas Komputasi Kelompok 1")
    print("------------------------------------")
    print("1. Daffa Dewantara - 12317012")
    print("2. Jonathan Adii - 12317028")
    print("3. Ariq Gustama P. - 12317052")
    print("------------------------------------")
    print("dibuat sebagai pemenuhan tugas akhir")
    print("====================================")
    print("====================================")
    print("====================================")
    print("====================================")
    print("====================================")
    print("====================================")
    print("====================================")

def main_menu():
    clear()
    print("====================================")
    print("Menu Utama")
    print("====================================")
    print("1. Metode Gauss")
    print("1. Metode Trapezoidal")
    print("3. Metode Regresi Kuadrat Terkecil")
    print("4. Metode Interpolasi Polinom Newton")
    print("5. Tentang Program")
    print("-----------------------------------")
    c = choice()
    if c == 1:
        gauss_main_menu()
    elif c == 2:
        trapezoidal_main_menu()
    elif c == 3:
        regression_main_menu()
    elif c == 4:
        interpolate_main_menu()
    elif c == 5:
        tentang_program()
    else:
        main_menu()


# ================================================================#
# Gauss Program
# ================================================================#


def input_polinom(n):
    """n=derajat polinom
    """
    a = np.zeros((n, n))
    b = np.zeros(n)
    print("------------------------------------")
    print(f"Input polinomial derajat {n}")
    print("------------------------------------")
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
                    pass
                else:
                    break
        while True:
            try:
                print(f"b[{i}] = ", end='')
                b[i] = int(input())
            except:
                pass
            else:
                break
    return a, b


def lihat_polinom(a, b):
    n = len(a)
    for i in range(0, n):
        print("|", end=' ')
        for j in range(0, n):
            print(f"{a[i][j]}", end=' ')
            if j == n - 1:
                print(f"| |x{i}|  |{b[i]}|")
    return None


def input_file_gauss(file):
    line = []
    a = []
    b = []
    with open(file, 'r') as r:
        for l in r:
            line.append(l)
    n = len(line)
    for ln in range(n):
        line_split = line[ln].split()
        for i in range(n):
            a.append(line_split[i])
        b.append(line_split[-1])
    a = np.array(a, dtype='float').reshape(n, n)
    b = np.array(b, dtype='float')
    return a, b


def output_file(x, file):
    with open(file, 'x') as writer:
        for i in x:
            writer.write(f"{i} ")
    return None


# --------------------------------------------------------------------------------------#


def gauss_main_menu(a=None, b=None):
    """Menu program Gauss"""
    while True:
        clear()
        print("====================================")
        print("PROGRAM METODE GAUSS")
        print("====================================")
        try:
            lihat_polinom(a, b)
        except:
            print("----")
        print("------------------------------------")
        print("1. Input soal secara manual")
        print("2. Input soal dari file")
        print("3. Hitung solusi")
        print("0. Kembali ke menu utama")
        print("99. Keluar Program")
        print("------------------------------------")
        c = choice()
        if c == 1:
            print("------------------------------------")
            print("1. SPL 3 Variabel")
            print("2. SPL 4 Variabel")
            print("3. SPL 5 Variabel")
            c = choice()
            if c == 1:
                a, b = input_polinom(3)
            elif c == 2:
                a, b = input_polinom(4)
            elif c == 2:
                a, b = input_polinom(5)
            else:
                pass
        elif c == 2:
            print("------------------------------------")
            try:
                file = input("Masukkan lokasi file: ")
                open(file)
            except:
                print("------------------------------------")
                print("file tidak ditemukan!")
            else:
                a, b = input_file_gauss(file)
            finally:
                print("------------------------------------")
                print("Tekan enter untuk melanjutkan.")
                input()
        elif c == 3:
            try:
                x = gauss(a, b)
            except:
                print("------------------------------------")
                print("......soal belum diinput............")
                print("------------------------------------")
                print("Tekan enter untuk melanjutkan.")
                input()
            else:
                print("------------------------------------")
                print("Solusi adalah:")
                print(x)
                print("------------------------------------")
                while True:
                    c = input("Ketik solusi ke dalam file?(y/n) ")
                    if c == 'y' or c == 'Y':
                        print("------------------------------------")
                        file = input("Lokasi file: ")
                        try:
                            output_file(x, file)
                        except:
                            print("------------------------------------")
                            print("terjadi kesalahan!")
                        finally:
                            print("------------------------------------")
                            print("Tekan enter untuk melanjutkan.")
                            input()
                    elif c == 'n' or c == 'N':
                        break
                    else:
                        pass
        elif c == 0:
            main_menu()
        elif c == 99:
            break
        else:
            pass


# ================================================================#
# Trapezoidal Program
# ================================================================#

def test_fx(fx, x=0):
    return eval(fx)


def input_fx():
    while True:
        print("------------------------------------")
        print("Gunakan variabel x!")
        print("** untuk pangkat, * untuk kali.")
        print("Contoh: 2*x**2+x+2")
        print("------------------------------------")
        fx = input("input persamaan: ")
        try:
            test_fx(fx, 0)
        except:
            print("error!")
        else:
            break
    return fx


def input_file_trapezoidal(file):
    with open(file, 'r') as r:
        fx = r.readline()
        try:
            test_fx(fx, 0)
        except:
            print("------------------------------------")
            print("error!")
        else:
            return fx


def graph_fx_trapezoidal(func):
    a = int(input("Masukkan batas bawah: "))
    b = int(input("Masukkan batas atas: "))
    x = np.arange(a, b, 0.01)

    fig, ax = plt.subplots()

    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data', 0))  # set position of x spine to x=0
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))  # set position of y spine to y=0
    ax.grid(True)
    ax.plot(x, func(x), 'r', label='Fx')
    legend = ax.legend(loc=2)
    plt.xlabel("x")
    plt.ylabel("f(x) = y")
    plt.show()
    return None


# --------------------------------------------------------------------------------------#


def trapezoidal_main_menu(fx=None):
    """Trapezoidal Interface Program"""
    while True:
        clear()
        print("====================================")
        print("Trapezoidal Method Program")
        print("====================================")
        print(f"Fx = {fx}")
        print("------------------------------------")
        print("1. Input persamaan manual")
        print("2. Input persamaan dari file")
        print("3. Tampilkan grafik dari persamaan")
        print("4. Hitung solusi trapezoidal")
        print("0. Kembali ke menu utama")
        print("99. Exit program")
        print("------------------------------------")
        c = choice()
        if c == 1:
            fx = input_fx()
            func = f_trap(fx)
        elif c == 2:
            print("------------------------------------")
            file = input("Lokasi file: ")
            try:
                open(file, 'r')
            except:
                print("------------------------------------")
                print("file tidak ditemukan!")
            else:
                fx = input_file_trapezoidal(file)
                func = f_trap(fx)
            finally:
                print("------------------------------------")
                print("Tekan enter untuk melanjutkan.")
                input()
        elif c == 3:
            try:
                test_fx(fx, 0)
            except:
                print("------------------------------------")
                print("......soal belum diinput............")
                print("------------------------------------")
                print("Tekan enter untuk melanjutkan.")
                input()
            else:
                graph_fx_trapezoidal(func)
            finally:
                print("------------------------------------")
                print("Tekan enter untuk melanjutkan.")
                input()
        elif c == 4:
            print("------------------------------------")
            try:
                a = int(input("Masukkan batas bawah: "))
                b = int(input("Masukkan batas atas: "))
                n = int(input("Masukkan step: "))
                solusi = trapezoidal(func, a, b, n)
            except:
                print("------------------------------------")
                print("terjadi kesalahan!")
            else:
                print("------------------------------------")
                print(f"Solusi adalah: {solusi}")
                print("------------------------------------")
            finally:
                while True:
                    c = input("Ketik solusi ke dalam file?(y/n) ")
                    if c == 'y' or c == 'Y':
                        print("------------------------------------")
                        file = input("Lokasi file: ")
                        try:
                            output_file(solusi, file)
                        except:
                            print("------------------------------------")
                            print("terjadi kesalahan!")
                        finally:
                            print("------------------------------------")
                            print("Tekan enter untuk melanjutkan.")
                            input()
                    elif c == 'n' or c == 'N':
                        break
                    else:
                        pass
                print("------------------------------------")
                print("Tekan enter untuk melanjutkan.")
                input()
        elif c == 0:
            main_menu()
        elif c == 99:
            break
        else:
            pass


# ================================================================#
# ================================================================#


def input_data():
    x = []
    y = []
    while True:
        try:
            print("------------------------------------")
            i_x = int(input("x: "))
            i_y = int(input("y: "))
        except:
            print("------------------------------------")
            print("error!")
        else:
            x.append(i_x)
            y.append(i_y)
            print("..........data dimasukkan...........")
        finally:
            print("Ketik q untuk kembali")
            i = input("Enter untuk melanjutkan input data: ")
            if i == 'q' or i == 'Q':
                break
    x = np.array(x, dtype='float')
    y = np.array(y, dtype='float')
    return x, y


def input_file_data(file):
    with open(file, 'r') as r:
        data = r.readlines()
    line = len(data)
    x = []
    y = []
    for i in range(line):
        data_split = data[i].split()
        x.append(data_split[0])
        y.append(data_split[1])
    x = np.array(x, dtype='float')
    y = np.array(y, dtype='float')
    return x, y


def tambah_data(x, y):
    while True:
        try:
            print("------------------------------------")
            i_x = int(input("x: "))
            i_y = int(input("y: "))
        except:
            print("------------------------------------")
            print("error!")
        else:
            x = np.append(x, i_x)
            y = np.append(y, i_y)
            print(".........data dimasukkan............")
        finally:
            print("Ketik q untuk kembali")
            i = input("Enter untuk melanjutkan input data: ")
            if i == 'q' or i == 'Q':
                break
    return x, y


def edit_data(x, y):
    print("------------------------------------")
    lihat_data(x, y)
    try:
        print("------------------------------------")
        i_no = int(input("Nomor data yang diedit: "))
        i_xy = input("x/y: ")
    except:
        print("------------------------------------")
        print("error!")
    else:
        i_no -= 1
        if i_xy == 'x' or i_xy == 'X':
            print("------------------------------------")
            print(f"Nilai sebelumnya: {x[i_no]}")
            try:
                print("------------------------------------")
                i_x = int(input("Nilai baru: "))
            except:
                print("------------------------------------")
                print("angka yang dimasukkan salah!")
            else:
                x[i_no] = i_x
        if i_xy == 'y' or i_xy == 'Y':
            print("------------------------------------")
            print(f"Nilai sebelumnya: {y[i_no]}")
            try:
                print("------------------------------------")
                i_y = int(input("Nilai baru: "))
            except:
                print("------------------------------------")
                print("angka yang dimasukkan salah!")
            else:
                y[i_no] = i_y
        print("..........data diperbaharui.........")
        print("Tekan enter untuk melanjutkan.")
        input()
    return x, y


def lihat_data(x, y, graph=False):
    counter = 1
    print(f"no\t|\tx\t\ty")
    j = 0
    for i in x:
        print(f"{counter}\t|\t{i}\t\t{y[j]}")
        j += 1
        counter = counter + 1
    return None


# ================================================================#
# Lease Square Regression Program
# ================================================================#

def regression_main_menu(x=None, y=None, xi=np.arange(0), yi=np.arange(0)):
    """Regression Interface Program
    """
    while True:
        clear()
        print("====================================")
        print("Regression Method Program")
        print("====================================")
        print("1. Input/Edit Data")
        print("2. Lihat data")
        print("3. Taksir titik x")
        print("4. Tampilkan grafik regresi")
        print("0. Kembali ke menu utama")
        print("99. Exit program")
        print("------------------------------------")
        c = choice()
        if c == 1:
            print("------------------------------------")
            print("1. Input data secara manual")
            print("2. Input data dari file")
            print("3. Edit data")
            print("4. Tambah data")
            print("------------------------------------")
            c = choice()
            if c == 1:
                x, y = input_data()
            elif c == 2:
                print("------------------------------------")
                file = input("Lokasi file: ")
                try:
                    open(file, 'r')
                except:
                    print("------------------------------------")
                    print("file tidak ditemukan!")
                else:
                    x, y = input_file_data(file)
                    print("------------------------------------")
                    lihat_data(x, y)
                finally:
                    print("------------------------------------")
                    print("Tekan enter untuk melanjutkan.")
                    input()
                pass
            elif c == 3:
                try:
                    x, y = edit_data(x, y)
                except:
                    pass
            elif c == 4:
                try:
                    x, y = tambah_data(x, y)
                except:
                    pass

        elif c == 2:
            print("------------------------------------")
            try:
                lihat_data(x, y)
            except:
                pass
            else:
                c = input("Ketik y untuk tampilkan grafik: ")
                if c == 'y' or c == 'Y':
                    plt.plot(x, y, 'r.')
                    plt.show()
            finally:
                print("------------------------------------")
                print("Tekan enter untuk melanjutkan.")
                input()

        elif c == 3:
            print("------------------------------------")
            try:
                i_xi = int(input("Masukkan x yang ingin ditaksir nilainya: "))
                f = least_square_regression(x, y)
            except:
                print("error!")
            else:
                print("------------------------------------")
                i_yi = f(i_xi)
                print(f"Nilai taksiran adalahL {i_yi}")
                xi = np.append(xi, i_xi)
                yi = np.append(yi, i_yi)
                print(".......Nilai taksiran disimpan......")
            finally:
                print("------------------------------------")
                print("Tekan enter untuk melanjutkan.")
                input()
        elif c == 4:
            try:
                f = least_square_regression(x, y)
                if xi.size > 0 and yi.size > 0:
                    x_min = np.minimum(np.amin(x), np.amin(xi))
                    x_max = np.maximum(np.amax(x), np.amax(xi))
                else:
                    x_min = np.amin(x)
                    x_max = np.amax(x)
            except:
                print("error!")
            else:
                graph_fx_data(f, x, y, xi, yi, x_min - 1, x_max + 1)
            finally:
                print("------------------------------------")
                print("Tekan enter untuk melanjutkan.")
                input()
        elif c == 0:
            main_menu()
        elif c == 99:
            break
        else:
            pass


# ================================================================#
# Interpolate Polinom Program
# ================================================================#


def interpolate_main_menu(x=None, y=None, xi=np.arange(0), yi=np.arange(0), n_polinom=None):
    """Regression Interface Program
        """
    while True:
        clear()
        print("====================================")
        print("Interpolate Method Program")
        print("====================================")
        print("1. Input/Edit Data")
        print("2. Lihat data")
        print("3. Input derajat polinomial")
        print("4. Taksir titik x")
        print("5. Tampilkan grafik interpolasi")
        print("0. Kembali ke menu utama")
        print("99. Exit program")
        print("------------------------------------")
        c = choice()
        if c == 1:
            print("------------------------------------")
            print("1. Input data secara manual")
            print("2. Input data dari file")
            print("3. Edit data")
            print("4. Tambah data")
            print("------------------------------------")
            c = choice()
            if c == 1:
                x, y = input_data()
            elif c == 2:
                print("------------------------------------")
                file = input("Lokasi file: ")
                try:
                    open(file, 'r')
                except:
                    print("------------------------------------")
                    print("file tidak ditemukan!")
                else:
                    x, y = input_file_data(file)
                    print("------------------------------------")
                    lihat_data(x, y)
                finally:
                    print("------------------------------------")
                    print("Tekan enter untuk melanjutkan.")
                    input()
                pass
            elif c == 3:
                try:
                    x, y = edit_data(x, y)
                except:
                    pass
            elif c == 4:
                try:
                    x, y = tambah_data(x, y)
                except:
                    pass
        elif c == 2:
            print("------------------------------------")
            try:
                lihat_data(x, y)
            except:
                pass
            else:
                c = input("Ketik y untuk tampilkan grafik: ")
                if c == 'y' or c == 'Y':
                    plt.plot(x, y, 'r.')
                    plt.show()
            finally:
                print("------------------------------------")
                print("Tekan enter untuk melanjutkan.")
                input()
        elif c == 3:
            print("------------------------------------")
            print(f"Derajat polinom sebelumnya: {n_polinom}")
            try:
                print("------------------------------------")
                print(f"derajat maksimal: {len(x)}")
                n_polinom = int(input("Masukkan derajat polinom yang baru: "))
                assert n_polinom < len(x)
            except:
                print("------------------------------------")
                print("error!")
                n_polinom = None
            else:
                print("------------------------------------")
                print(".derajat polinom telah diperbaharui.")
        elif c == 4:
            print("------------------------------------")
            try:
                i_xi = int(input("Masukkan x yang ingin ditaksir: "))
                f = interpolate_polinom(x, y, n_polinom)
            except:
                print("terjadi kesalahan!")
            else:
                print("------------------------------------")
                i_yi = f(i_xi)
                print(f"Nilai taksiran adalah {i_yi}")
                xi = np.append(xi, i_xi)
                yi = np.append(yi, i_yi)
                print(".......nilai taksiran disimpan......")
            finally:
                print("------------------------------------")
                print("Tekan enter untuk melanjutkan.")
                input()
        elif c == 5:
            try:
                f = interpolate_polinom(x, y, n_polinom)
                if xi.size > 0 and yi.size > 0:
                    x_min = np.minimum(np.amin(x), np.amin(xi))
                    x_max = np.maximum(np.amax(x), np.amax(xi))
                else:
                    x_min = np.amin(x)
                    x_max = np.amax(x)
            except:
                print("error!")
            else:
                graph_fx_data(f, x, y, xi, yi, x_min - 0.5, x_max + 0.5)
            finally:
                print("------------------------------------")
                print("Tekan enter untuk melanjutkan.")
                input()
        elif c == 0:
            main_menu()
        elif c == 99:
            break
        else:
            pass


# -----------------------------------------------------------------------------------------#

def graph_fx_data(f, x, y, xi, yi, x_min, x_max):
    """Fungsi untuk membuat grafik dari data."""
    matplotlib.use('png')

    x_plot = np.linspace(x_min, x_max, 1000)
    y_plot = f(x_plot)

    fig, ax = plt.subplots()
    ax.plot(x, y, 'ro', label='data')
    ax.plot(xi, yi, 'bs', label='titik yang diestimasi')
    ax.plot(x_plot, y_plot, 'g', label='garis regresi/interpolasi')
    ax.axis('tight')
    legend = ax.legend()
    plt.xlabel("x")
    plt.ylabel("f(x) = y")
    plt.show()

    c = input("Ketik y untuk menyimpan gambar: ")
    if c == 'y' or c == 'Y':
        try:
            print("------------------------------------")
            i = int(input("Nama file: "))
            plt.savefig(i)
        except:
            print("error!")
    return None


if __name__ == '__main__':
    main_menu()
