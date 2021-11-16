from tkinter import *
import csv
import codecs
import numpy as np
import pandas as pd
import os
import itertools
data = pd.read_csv("case-mv.csv",header=None)
source=np.array(data)
ca4=np.delete(source,0,0)
def truthtable():
    title=[]
    biao = source[0]
    for i in range(len(biao)):
      title.append(biao[i])
    title1 =["number","raw consist","logicalitem"]
    title.extend(title1)
    with open("truthtable-mv.csv", "a", newline="", encoding="utf-8") as csvfile1:
        writer = csv.writer(csvfile1, delimiter=',')
        writer.writerow(title)
    data = pd.read_csv("case-mv.csv", header=None)
    a = np.array(data)
    hang = a.shape[0]
    data = pd.read_csv("numberofvariable.csv", header=None)
    source5 = np.array(data)
    lie = source5.shape[1]
    mv =[]
    for w in range(lie):
        mv.append(source5[0][w])
    print("the set of variables' number is:"+str(mv))
    ab = len(mv)
    ef = []
    for i in range(0,ab):
        cd = []
        for j in range(0,mv[i]):
            cd.append(j)
        ef.append(cd)
    aa = itertools.product(*ef)
    bb = list(aa)
    cc=[]
    for i in range(len(bb)):
        dd=list(bb[i])
        cc.append(dd)
    ca5=[]
    for i in range(hang-1):
        ca5.append([int(j) for j in ca4[i]])
    for i in range(len(cc)):
        num=0
        for j in range(len(ca5)):
            if (ca5[j]==cc[i]):
                num=num+1
        cc[i].append(num)
    la=[]
    for i in range(len(cc)):
        la1=[]
        for j in range(len(cc[i])):
            a=cc[i][j]
            la1.append(a)
        la.append(la1)
    for i in range(len(cc)):
        cc[i].pop()
        cc[i].pop()
    for i in range(len(cc)):
        hh=len(cc[i])
        aa=la[i][hh+1]
        bb1=0
        for j in range(len(cc)):
            if (i!=j):
                if(cc[i]==cc[j]):
                    bb1 = bb1+la[j][hh+1]
        bb=bb1+la[i][hh+1]
        if (bb!=0):
            rawcon=aa/bb
            la[i].append("%.6f" % rawcon)
        else:
            la[i].append("")
        if (la[i][hh+1]==0):
            la[i].append(1)
        else:
            la[i].append(0)
        with open("truthtable-mv.csv", "a", newline="", encoding="utf-8") as csvfile1:
            writer = csv.writer(csvfile1, delimiter=',')
            writer.writerow(la[i])
        with open("truthtable-mv-backup.csv", "a", newline="", encoding="utf-8") as csvfile1:
            writer = csv.writer(csvfile1, delimiter=',')
            writer.writerow(la[i])
#truthtable()