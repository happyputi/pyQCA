from tkinter import *
import csv
import codecs
import numpy as np
import pandas as pd
import os
import itertools
def mvminizationsolution(data2,mv2):
    data1=data2
    mv=mv2
    def listcom(x, y):
        z = []
        cwcw1 = x
        cwcw2 = y
        cwcw1 = cwcw1 + cwcw2
        for id in cwcw1:
            if id not in z:
                z.append(id)
        z = sorted(z)
        cwcw1 = []
        cwcw2 = []
        return z
    def combine(m, n):
        a = len(m)
        b = len(n)
        c = []
        count = 0
        for i in range(a):
            if (m[i] == n[i]):
                c.append(m[i])
            else:
                e = []
                f = []
                if type(m[i]) is str:
                    e.append(m[i])
                else:
                    e = m[i]
                if type(n[i]) is str:
                    f.append(n[i])
                else:
                    f = n[i]
                d = listcom(e, f)
                if d[0] == "-":
                    d = '-'
                else:
                    if len(d) == mv[i]:
                        d = '-'
                c.append(d)
                count = count + 1
        if (count > 1):
            return None
        else:
            return c
    def find_prime_implicants(data):
        if type(data) == set:
            newList = list(data)
        if type(data) == list:
            newList = list(data)
        size = len(newList)
        IM = []
        im = []
        im2 = []
        mark = [0] * size
        m = 0
        for i in range(size):
            for j in range(i + 1, size):
                d = combine((newList[i]), (newList[j]))
                if d != None:
                    im.append(d)
                    mark[i] = 1
                    mark[j] = 1
                else:
                    continue
        mark2 = [0] * len(im)
        for p in range(len(im)):
            for n in range(p + 1, len(im)):
                if (p != n and mark2[n] == 0):
                    if (im[p] == im[n]):
                        mark2[n] = 1
        for r in range(len(im)):
            if (mark2[r] == 0):
                im2.append(im[r])
        for q in range(size):
            if (mark[q] == 0):
                IM.append(newList[q])
                m = m + 1
        if (m == size or size == 1):
            return IM
        else:
            return IM + find_prime_implicants(im2)
    minterms=data1
    resu1 = find_prime_implicants(minterms)
    flag = []
    long = []
    for i in range(len(resu1)):
        a = 0
        for j in range(len(resu1[i])):
            if type(resu1[i][j]) == list:
                a = a + 1
                b = len(resu1[i][j])
        if a == 0:
            flag.append(0)
            long.append(0)
        else:
            flag.append(1)
            long.append(b)
    result = []
    for i in range(len(flag)):
        if flag[i] == 0:
            result.append(resu1[i])
        else:
            for k in range(long[i]):
                result2 = []
                for j in range(len(resu1[i])):
                    if type(resu1[i][j]) != list:
                        result2.append(resu1[i][j])
                    else:
                        result2.append(resu1[i][j][k])
                result.append(result2)
    return resu1,result