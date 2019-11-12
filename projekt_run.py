#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Mnożenie macieży NxN gdzie N=2^n. Algorytm Strassena versus mnożenie z definicji. Dla jakich N algorytm Strassena zaczyna się opłacać?
Moduły do projekt_run.py:
a) mnozenie_defi.py
b) strassen.py
Opis do algorytmu Strassena oraz wniosek:
* info.txt
"""

import numpy as np
import matplotlib.pyplot as mp
import random
import time
import math
import mnozenie_defi as md
import strassen as stn



#Tworzenie macierzy NxN o wartościach do wartości maksymalnej
def stworz_macierz(wymiar, war_max):
    return [[random.randint(0, war_max) for i in range(wymiar)] for k in range(wymiar)]

#Test sprawdzający czas wykonania danej metody; A - macierz 1, B - macierz 2, powt - liczba powtórzeń wykonania
#nie przewiduje sprawdzania, czy macierze są rozmiaru kolejnych potęg 2 ze względu na założenie
def test(A, B, metoda, powt):
    if type(A) == list and type(B) == list and len(A) == len(A[0]) == len(B) == len(B[0]):
        czas = np.zeros(powt)
        for i in range(powt):
            start = time.time()
            C = metoda(A, B)
            end = time.time()
            czas[i] = end - start
        return czas
    else:
        print("Zły rozmiar macierzy")

if __name__ == "__main__":
    A = stworz_macierz(2, 10)
    B = stworz_macierz(2, 10)
    powt = 10
    cz_md = test(A, B, md.mnozenie_def, powt)
    cz_stn = test(A, B, stn.strassen, powt)
    sr_md0 = np.mean(cz_md)
    sr_stn0 = np.mean(cz_stn)

    A = stworz_macierz(4, 10)
    B = stworz_macierz(4, 10)
    powt = 10
    cz_md = test(A, B, md.mnozenie_def, powt)
    cz_stn = test(A, B, stn.strassen, powt)
    sr_md1 = np.mean(cz_md)
    sr_stn1 = np.mean(cz_stn)

    A = stworz_macierz(16, 10)
    B = stworz_macierz(16, 10)
    powt = 10
    cz_md = test(A, B, md.mnozenie_def, powt)
    cz_stn = test(A, B, stn.strassen, powt)
    sr_md2 = np.mean(cz_md)
    sr_stn2 = np.mean(cz_stn)

    A = stworz_macierz(64, 10)
    B = stworz_macierz(64, 10)
    powt = 10
    cz_md = test(A, B, md.mnozenie_def, powt)
    cz_stn = test(A, B, stn.strassen, powt)
    sr_md3 = np.mean(cz_md)
    sr_stn3 = np.mean(cz_stn)

    A = stworz_macierz(128, 10)
    B = stworz_macierz(128, 10)
    powt = 10
    cz_md = test(A, B, md.mnozenie_def, powt)
    cz_stn = test(A, B, stn.strassen, powt)
    sr_md4 = np.mean(cz_md)
    sr_stn4 = np.mean(cz_stn)


    print("\nŚredni czas wykonania dla mnożenia macierzy z definicji:\n")
    print(">>>2x2... {:.8f}s\n>>>4x4... {:.8f}s\n>>>8x8... {:.8f}s\n>>>64x64... {:.8f}s\n>>>128x128... {:.8f}s".format(sr_md0, sr_md1, sr_md2, sr_md3, sr_md4))
    print("\nŚredni czas wykonania dla mnożenia macierzy z algorytmu Strassena:\n")
    print(">>>2x2... {:.8f}s\n>>>4x4... {:.8f}s\n>>>8x8... {:.8f}s\n>>>64x64... {:.8f}s\n>>>128x128... {:.8f}s".format(sr_md0, sr_stn1, sr_stn2, sr_stn3, sr_stn4))
    sr_md = np.array([sr_md0, sr_md1, sr_md2, sr_md3, sr_md4])
    sr_stn = np.array([sr_md0, sr_stn1, sr_stn2, sr_stn3, sr_stn4])
    roz_m = np.array([2, 4, 16, 64, 128])
    mp.plot(roz_m, sr_md, 'bo', roz_m, sr_stn, 'r^')
    mp.title(u'Mnożenie z definicji versus algorytm Strassena')
    mp.xlabel(u'Rozmiar macierzy (N) użytych do obliczenia')
    mp.ylabel(u'Czas wykonania metody [s]')
    mp.show()


