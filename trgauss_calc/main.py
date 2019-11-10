import numpy as np

import InterpolatePol as ip
import Gauss
import LeastSquareReg as lsr
import Trapezoidal



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
        gauss_inf()
    elif a==2:
        trap_inf()
    elif a==3:
        reg_inf()
    elif a==4:
        interpol_inf()

def trap_inf():
    """Interface Trapezoidal
    """        
    print("========================")    
    print("1. ")
    print("2. ")
    print("3. ")
    print("4. ")
    print("0. ")
    #elif a==3:
    #
    #elif a==4:
    #    
    #elif a==5:
        
def gauss_inf():
        """Gauss Interface Program
        """    
        print("========================")    
        print("1. Sistem Persamaan Linier (SPL) 3 Variabel")
        print("2. SPL 4 Variabel")
        print("3. SPL 5 Variabel")
        print("4. Kembali ke menu sebelumnya")
        print("0. Kembali ke menu utama")
        a = choice()
        if a==1:
            soal()



main()

"""

c = int(input())
        if c == 1:
            a,b = Gauss.input_polinom(3)
            print(a)
            print(b)
            print("Hasil:")
            print(Gauss.gauss(a, b))
        elif c == 2:
            a,b = Gauss.input_polinom(4)
            print(a)
            print(b)
            print("Hasil:")
            print(Gauss.gauss(a, b))
        elif c == 3:
            a,b = Gauss.input_polinom(5)
            print(a)
            print(b)
            print("Hasil:")
            print(Gauss.gauss(a, b))
        elif c == 4:
            main()
        elif c == 0:
            main()
        else:
            print("Error.... try again")
            gauss_inf()

"""