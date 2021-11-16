from tkinter import *
import csv
import codecs
import numpy as np
import pandas as pd
import os
import itertools
def check(qwe,lon):
    data = pd.read_csv("case-mv.csv", header=None)
    source = np.array(data)
    ca1 = np.delete(source, 0, 0)
    hang = ca1.shape[0]
    lie = ca1.shape[1]
    ca2 = []
    for i in range(hang):
        ca2.append([str(j) for j in ca1[i]])
    kkk = qwe
    lll = lon
    ch = []
    a = 0
    uniq=[]
    for k in range(lll):
        ch.append(kkk[k])
    for n in range(len(ca2)):
        df = []
        for m in range(lll):
            df.append(ca2[n][m])
        if "-" not in kkk:
            if df == ch:
                a = a + 1
                uniq.append(ca2[n][0:lll])
        else:
            for p in range(lon):
                if kkk[p] == "-":
                    xxx = p
                    df[xxx] = "-"
            if df == ch:
                a = a + 1
                uniq.append(ca2[n][0:lll])
    return (a,uniq)
def findsame(www):
    bi=www
    data = pd.read_csv("case-mv.csv", header=None)
    source = np.array(data)
    ca3=np.delete(source, 0, 0)
    finlie = ca3.shape[1]
    if www==finlie:
        fin=ca3
    else:
        fin=np.delete(ca3,www,1)
    finhang=fin.shape[0]
    fincheck=[]
    for r in range(finhang):
        fincheck.append([str(j) for j in fin[r]])
    refin=[]
    renum=[]
    for o in range(len(fincheck)):
        if fincheck.count(fincheck[o])>1:
            if fincheck[o] not in refin:
                refin.append(fincheck[o])
                renum.append(fincheck.count(fincheck[o])-1)
    return refin,renum
def samecolumn(valu):
    data = pd.read_csv("case-mv.csv", header=None)
    source = np.array(data)
    ca1 = np.delete(source, 0, 0)
    hang = ca1.shape[0]
    lie = ca1.shape[1]
    ca2 = []
    for i in range(hang):
        ca2.append([str(j) for j in ca1[i]])
    xyz = valu
    b = 0
    for k in range(len(ca2)):
        if ca2[k][len(ca2[k])-1]==xyz:
            b=b+1
    return b
def mvcalculatesolution(data2,last1):
    last=last1
    data = pd.read_csv("case-mv.csv", header=None)
    source = np.array(data)
    ca1 = np.delete(source, 0, 0)
    hang = ca1.shape[0]
    lie = ca1.shape[1]
    result1=data2
    solution=[]
    for i in range(len(result1)):
        if type(result1[i][len(result1[i])-1]) == str:
            if result1[i][len(result1[i])-1]!="-":
                solution.append(result1[i])
    flag = []
    long = []
    for i in range(len(solution)):
        a = 0
        for j in range(len(solution[i])):
            if type(solution[i][j]) == list:
                a = a + 1
                b = len(solution[i][j])
        if a == 0:
            flag.append(0)
            long.append(0)
        else:
            flag.append(1)
            long.append(b)
    result = []
    for i in range(len(flag)):
        if flag[i] == 0:
            result.append(solution[i])
        else:
            for k in range(long[i]):
                result2 = []
                for j in range(len(solution[i])):
                    if type(solution[i][j]) != list:
                        result2.append(solution[i][j])
                    else:
                        result2.append(solution[i][j][k])
                result.append(result2)
    laresu=[]
    for id in result:
        if id not in laresu:
            laresu.append(id)
    if len(laresu) != 0:
        with open("parsmonioussolution-mv.csv", "a", newline="", encoding="utf-8") as csvfile1:
            writer = csv.writer(csvfile1, delimiter=',')
            writer.writerow(["result=" + source[0][lie - 1] + str(last)+":"])
        print("result=" + source[0][lie - 1] + str(last)+":")
        with open("parsmonioussolution-mv.csv", "a", newline="", encoding="utf-8") as csvfile1:
            writer = csv.writer(csvfile1, delimiter=',')
            writer.writerow(["solutions", "rawcoverage", "uniquecoverage", "consistency"])
        print("  solutions   ", "rawcoverage", "uniquecoverage", "consistency")
        wrire0 = []
        for i in range(len(laresu)):
            if "-" not in laresu[i]:
                ad = ""
                for j in range(len(laresu[i]) - 1):
                    ad = ad + source[0][j] + laresu[i][j] + "*"
                wrire0.append(ad)
            else:
                af = ""
                for k in range(len(laresu[i]) - 1):
                    if laresu[i][k] != "-":
                        af = af + source[0][k] + laresu[i][k] + "*"
                    else:
                        af = af + ""
                wrire0.append(af)
        ac = []
        for i in range(len(laresu)):
            aa, item = check(laresu[i], len(laresu[i]))
            ac.append(item)
        repea1 = []
        for m in range(len(ac)):
            noeq = 0
            for n in range(len(ac[m])):
                ttag = 0
                for p in range(len(ac)):
                    if ac[m][n] not in ac[p]:
                        ttag = ttag + 1
                if (ttag == len(ac) - 1):
                    noeq = noeq + 1
            repea1.append(noeq)
        xx = []
        zz = []
        y = 0
        for t in range(hang):
            if ca1[t][len(ca1[t]) - 1] == str(last):
                y = y + 1
        for j in range(len(laresu)):
            x, item = check(laresu[j], len(laresu[j]))
            for k in range(len(item)):
                if item[k] not in xx:
                    xx.append(item[k])
            z, item1 = check(laresu[j], len(laresu[j]) - 1)
            for n in range(len(item1)):
                if item1[n] not in zz:
                    zz.append(item1[n])
            if x != 0:
                toprin1 = []
                toprin1.append(wrire0[j])
                rawcov = round(x / y, 6)
                toprin1.append(rawcov)
                uniquecov = round((repea1[j]) / y, 6)
                toprin1.append(uniquecov)
                consis = round(x / z, 6)
                toprin1.append(consis)
                with open("parsmonioussolution-mv.csv", "a", newline="", encoding="utf-8") as csvfile1:
                    writer = csv.writer(csvfile1, delimiter=',')
                    writer.writerow(toprin1)
                print(toprin1)
        jiaoyan1 = 0
        jiaoyan2 = 0
        aaa, bbb = findsame(lie)
        for u in range(len(aaa)):
            if aaa[u] in xx:
                jiaoyan1 = jiaoyan1 + bbb[u]
        ccc, ddd = findsame(lie - 1)
        for v in range(len(ccc)):
            if ccc[v] in zz:
                jiaoyan2 = jiaoyan2 + ddd[v]
        if y != 0:
            solucov = round((len(xx) + jiaoyan1) / y, 6)
            print("solutioncoverage:" + str(solucov))
            ae = ["solutioncoverage:", str(solucov)]
            with open("parsmonioussolution-mv.csv", "a", newline="", encoding="utf-8") as csvfile1:
                writer = csv.writer(csvfile1, delimiter=',')
                writer.writerow(ae)
        if (len(zz) + jiaoyan2) != 0:
            solucon = round((len(xx) + jiaoyan1) / (len(zz) + jiaoyan2), 6)
            print("solutionconsistency:" + str(solucon))
            be = ["solutionconsistency:", str(solucon)]
            with open("parsmonioussolution-mv.csv", "a", newline="", encoding="utf-8") as csvfile1:
                writer = csv.writer(csvfile1, delimiter=',')
                writer.writerow(be)
    return
