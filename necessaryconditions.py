from tkinter import *
import csv
import codecs
import numpy as np
import pandas as pd
import os
import itertools
import minization
import calculate
def check():
    data=pd.read_csv("case.csv",header=None)
    a = np.array(data)
    hang = a.shape[0]
    lie = a.shape[1]
    result=[]
    for j in range(0, lie - 1):
        c = 0
        e = 0
        g = 0
        u = 0
        v = 0
        resu=[]
        for i in range(1, hang):
            b = min(a[i, j], a[i, lie - 1])
            c += float(b)
            r = float(a[i,j])
            s = 1-r
            t = min(s, float(a[i, lie - 1]))
            u +=float(t)
            v +=s
            d = a[i, j]
            e += float(d)
            f = a[i, lie - 1]
            g += float(f)
        con = round(c / e,6)
        resu.append(a[0,j])
        resu.append(con)
        cov = round(c / g,6)
        resu.append(cov)
        nocon = round(u/v,6)
        nocov = round(u/g,6)
        h = a[0, j]
        result.append(resu)
    for j in range(0, lie - 1):
        c = 0
        e = 0
        g = 0
        u = 0
        v = 0
        resu = []
        for i in range(1, hang):
            b = min(a[i, j], a[i, lie - 1])
            c += float(b)
            r = float(a[i, j])
            s = 1 - r
            t = min(s, float(a[i, lie - 1]))
            u += float(t)
            v += s
            d = a[i, j]
            e += float(d)
            f = a[i, lie - 1]
            g += float(f)
        nocon = round(u / v, 6)
        nocov = round(u / g, 6)
        resu.append("~"+a[0, j])
        resu.append(nocon)
        cov = round(c / g, 6)
        resu.append(nocov)
        h = a[0, j]
        result.append(resu)
    with open("nessaryconditions.csv", "a", newline="", encoding="utf-8") as csvfile1:
        writer = csv.writer(csvfile1, delimiter=',')
        writer.writerow(["condition","consistency","coverage"])
        for i in range(len(result)):
            writer.writerow(result[i])
    print ("Conditions tested:","\t")
    print ("condition","consistency","coverage")
    for i in range(len(result)):
        print (result[i])












