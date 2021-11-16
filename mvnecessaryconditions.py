from tkinter import *
import csv
import codecs
import numpy as np
import pandas as pd
import os
import itertools
import minization
import calculate
data=pd.read_csv("case-mv.csv",header=None)
a = np.array(data)
hang = a.shape[0]
lie = a.shape[1]
def inputpa():
    data=pd.read_csv("case-mv.csv",header=None)
    a = np.array(data)
    hang = a.shape[0]
    lie = a.shape[1]
    mvv = []
    for i in range(0,lie):
        x = input("Please enter the number of values of variable " + str(i+1) +  ":")
        mvv.append(int(x))
    print("The set of number is:",mvv)
    with open("numberofvariable.csv", "a", newline="", encoding="utf-8") as csvfile1:
        writer = csv.writer(csvfile1, delimiter=',')
        writer.writerow(mvv)
    return mvv
def nece():
    mv1=inputpa()
    fi=[]
    resu1=[]
    for i in range(0, lie):
        e = mv1[i]
        g = []
        resu = []
        for j in range(0,e):
            c = 0
            d = ""
            for k in range(1, hang):
                jud=int(a[k][i])
                if jud == j:
                    c=c+1
            g.append(c)
            d = d+a[0][i]+str(j)
            resu.append(d)
        resu1.append(resu)
        fi.append(g)
    com=[]
    for i in range(0, lie-1):
        e = mv1[i]
        f = mv1[lie-1]
        d=[]
        for j in range(0,e):
            for k in range(0,f):
                c = 0
                for g in range(1,hang):
                    x=int(a[g][i])
                    y=int(a[g][lie-1])
                    if x==j and y==k:
                        c=c+1
                d.append(c)
        com.append(d)
    item1=[]
    for i in range(len(resu1)-1):
        item2=[]
        for j in range(len(resu1[i])):
            for k in range(len(resu1[len(resu1)-1])):
                item=resu1[i][j]+" VS "+resu1[len(resu1)-1][k]
                item2.append(item)
        item1.append(item2)
    cacon=[]
    calen=len(fi)-1
    for i in range(len(fi)-1):
        cacon1=[]
        for j in range(len(fi[i])):
            for k in range(len(fi[calen])):
                cacon1.append(fi[i][j])
        cacon.append(cacon1)
    cacov=[]
    cavlen=len(fi)-1
    for i in range(len(fi)):
        cacov1=[]
        for j in range(len(fi[i])):
            for k in range(len(fi[calen])):
                cacov1.append(fi[cavlen][k])
        cacov.append(cacov1)
    result=[]
    for i in range(len(item1)):
        for j in range(len(item1[i])):
            result2=[]
            consis=round(com[i][j]/cacon[i][j],6)
            coverag=round(com[i][j]/cacov[i][j],6)
            result2.append(item1[i][j])
            result2.append(consis)
            result2.append(coverag)
            result.append(result2)
    with open("nessaryconditions-mv.csv", "a", newline="", encoding="utf-8") as csvfile1:
        writer = csv.writer(csvfile1, delimiter=',')
        writer.writerow(["condition","consistency","coverage"])
        for i in range(len(result)):
            writer.writerow(result[i])
    print ("Conditions tested:","\t")
    print ("      condition       ","consistency","   coverage")
    for i in range(len(result)):
        print (result[i])
    return(mv1)
#nece()












