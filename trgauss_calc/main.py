import numpy as np

import InterpolatePol as ip
import Gauss
import LeastSquareReg as lsr
import Trapezoidal


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

def main():
    print("========================")
    print("Menu Utama")
    print("========================")
    print("1. Metode Gauss")
    print("1. Metode Trapezoidal")
    print("3. Metode Regresi Kuadrat Terkecil")
    print("4. Metode Interpolasi Polinom Newton")
    print("5. Tentang Program")
    print("------------------------")
    a = choice()
    if a==1:
        Gauss.gauss_interface()
    elif a==2:
        Trapezoidal.trapezoidal_interface()
    elif a==3:
        lsr.regression_interface()
    elif a==4:
        ip.interpol_interface()

if __name__ == "__main__":
    main()