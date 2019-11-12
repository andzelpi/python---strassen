#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Moduł:
a) mnożenie macierzy z definicji
"""


def mnozenie_def(a, b):
    l_c = len(a)
    c = [[0]*l_c for i in range(l_c)]
    for i in range(l_c):
        for j in range(l_c):
            for k in range(l_c):
                c[i][j] += a[i][k] * b[k][j]
    return c


'''
A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 1], [2, 2, 3, 3]]
B = [[1, 2, 3, 4], [1, 2, 5, 6], [1, 2, 3, 4], [1, 2, 3, 4]]
C = mnozenie_def(A, B)
print(C)
'''
