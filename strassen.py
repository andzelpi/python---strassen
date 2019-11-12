#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Moduł:
b) mnożenie macierzy za pomoca algorytmu Strassena
"""


def dodawanie(a, b):
    l_c = len(a)
    c = [[0]*l_c for i in range(l_c)]
    for i in range(l_c):
        for j in range(l_c):
            c[i][j] += a[i][j] + b[i][j]
    return c


def odejmowanie(a, b):
    l_c = len(a)
    c = [[0]*l_c for i in range(l_c)]
    for i in range(l_c):
        for j in range(l_c):
            c[i][j] += a[i][j] - b[i][j]
    return c


def strassen(a, b):
    l_c = len(a)
    if l_c == 2:

        m1 = (a[0][0] + a[1][1]) * (b[0][0] + b[1][1])
        m2 = (a[1][0] + a[1][1]) * b[0][0]
        m3 = a[0][0] * (b[0][1] - b[1][1])
        m4 = a[1][1] * (b[1][0] - b[0][0])
        m5 = (a[0][0] + a[0][1]) * b[1][1]
        m6 = (a[1][0] - a[0][0]) * (b[0][0] + b[0][1])
        m7 = (a[0][1] - a[1][1]) * (b[1][0] + b[1][1])

        c = [[0]*l_c for i in range(l_c)]
        c[0][0] = m1 + m4 - m5 + m7
        c[0][1] = m3 + m5
        c[1][0] = m2 + m4
        c[1][1] = m1 - m2 + m3 + m6

        return c

    else:
        #1
        l_c2 = l_c//2
        an11 = [[0]*l_c2 for i in range(l_c2)]
        an12 = [[0]*l_c2 for i in range(l_c2)]
        an21 = [[0]*l_c2 for i in range(l_c2)]
        an22 = [[0]*l_c2 for i in range(l_c2)]
        bn11 = [[0]*l_c2 for i in range(l_c2)]
        bn12 = [[0]*l_c2 for i in range(l_c2)]
        bn21 = [[0]*l_c2 for i in range(l_c2)]
        bn22 = [[0]*l_c2 for i in range(l_c2)]

        #2
        for i in range(l_c2):
            for j in range(l_c2):
                an11[i][j] = a[i][j]
                an12[i][j] = a[i][j + l_c2]
                an21[i][j] = a[i + l_c2][j]
                an22[i][j] = a[i + l_c2][j + l_c2]
                bn11[i][j] = b[i][j]
                bn12[i][j] = b[i][j + l_c2]
                bn21[i][j] = b[i + l_c2][j]
                bn22[i][j] = b[i + l_c2][j + l_c2]

        #3
        m1 = strassen(dodawanie(an11, an22), dodawanie(bn11, bn22)) # m1 = (a11 + a22) * (b11 + b22)
        m2 = strassen(dodawanie(an21, an22), bn11) # m2 = (a21 + a22) * (b11) 
        m3 = strassen(an11, odejmowanie(bn12, bn22)) # m3 = (a11) * (b12 - b22)
        m4 = strassen(an22, odejmowanie(bn21, bn11)) # m4 = (a22) * (b21 - b11)
        m5 = strassen(dodawanie(an11, an12), bn22) # m5 = (a11 + a12) * (b22)   
        m6 = strassen(odejmowanie(an21, an11), dodawanie(bn11, bn12)) # m6 = (a21 - a11) * (b11 + b12)
        m7 = strassen(odejmowanie(an12, an22), dodawanie(bn21, bn22)) # m7 = (a12 - a22) * (b21 + b22

        #4
        c = [[0]*l_c for i in range(l_c)]
        c11 = odejmowanie(dodawanie(dodawanie(m1, m4), m7), m5) # c11 = m1 + m4 - m5 + m7
        c12 = dodawanie(m3, m5) # c12 = m3 + m5
        c21 = dodawanie(m2, m4) # c21 = m2 + m4
        c22 = odejmowanie(dodawanie(dodawanie(m1, m3), m6), m2) # c22 = m1 - m2 + m3 + m6

        #5
        for i in range(l_c2):
            for j in range(l_c2):
                c[i][j] = c11[i][j]
                c[i][j + l_c2] = c12[i][j]
                c[i + l_c2][j] = c21[i][j]
                c[i + l_c2][j + l_c2] = c22[i][j]
        return c

#komentarze do #1, 2, 3, 4, 5 zawarte w pliku info.txt

'''
A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 1], [2, 2, 3, 3]]
B = [[1, 2, 3, 4], [1, 2, 5, 6], [1, 2, 3, 4], [1, 2, 3, 4]]
C = strassen(A, B)
print(C)
'''

