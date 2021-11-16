from tkinter import *
import csv
import codecs
import numpy as np
import pandas as pd
import os
import itertools
data = pd.read_csv("case.csv",header=None)
source=np.array(data)
ca1=np.delete(source,0,0)
hang=ca1.shape[0]
lie=ca1.shape[1]
ca2=[]
for i in range(hang):
    ca2.append([float(j) for j in ca1[i]])
def calculatesolution(data2):
    result=data2
    solution=[]
    CMAX1=[]
    for m in range (len(result)):
        data = pd.read_csv("case.csv",header=None)
        source=np.array(data)
        ca1=np.delete(source,0,0)
        hang=ca1.shape[0]
        lie=ca1.shape[1]
        ca2=[]
        for i in range(hang):
            ca2.append([float(j) for j in ca1[i]])
        X=0
        Y=0
        CXY=0
        b=result[m]
        CMAX=[]
        for j in range(len(ca2)):
            xi1 = []
            for k in range(len(b)):
                if (b[k]=='1'):
                    min1=round(0+float(ca2[j][k]),2)
                elif (b[k]=='0'):
                    min1=round(1-float(ca2[j][k]),2)
                else:
                    min1=1
                xi1.append(min1)
            xi=min(xi1)
            CMAX.append(xi)
            yi=ca2[j][len(b)]
            cxy=min(xi,yi)
            X=X+xi
            Y=Y+yi
            CXY=CXY+cxy
        CMAX1.append(CMAX)
        consist=CXY/X
        rawcov=CXY/Y
        consistency=round(consist,6)
        rawcoverage=round(rawcov,6)
        solu=[]
        solu.append(b)
        solu.append(rawcoverage)
        solu.append(consistency)
        #print (solu)
        solution.append(solu)
    CMAX2=[]
    for o in range(len(ca2)):
        CMAX3=[]
        for p in range (len(CMAX1)):
            CMAX3.append(CMAX1[p][o])
            x=max(CMAX3)
        CMAX2.append(x)
    YLIST=[]
    for i in range(len(ca2)):
        YLIST.append(ca2[i][len(b)])
    CCMAXY=[]
    for j in range(len(ca2)):
        CCMAXY.append(min(CMAX2[j],YLIST[j]))
    cc = np.array(CCMAXY)
    ccmaxy = round(cc.sum(),2)
    cm = np.array(CMAX2)
    cmax2 =round(cm.sum(),2)
    yl = np.array(YLIST)
    ylist =round(yl.sum(),2)
    solutionconsistency=round((ccmaxy/cmax2),6)
    solutioncoverage=round((ccmaxy/ylist),6)
    uniquecover=unique(result)
    toresult=[]
    for i in range(len(result)):
        finalresult = []
        finalresult.append(solution[i][0])
        finalresult.append(solution[i][1])
        unique2=round(solutioncoverage-uniquecover[i],6)
        finalresult.append(unique2)
        finalresult.append(solution[i][2])
        toresult.append(finalresult)
    last = [solutioncoverage,solutionconsistency]
    toresult.append(last)
    return toresult
def unique(data1):
    global bcd1
    global other
    global abc
    result=data1
    xx1=[]
    for h in range(len(result)):
        xx=[]
        for i in range(len(ca2)):
            abc2=[]
            for j in range(len(result)):
                if (j!=h):
                    c=result[j]
                    abc=[]
                    for l in range(len(c)):
                            if (c[l] == '1'):
                                min1 = round(0 + float(ca2[i][l]), 2)
                            elif (c[l] == '0'):
                                min1 = round(1 - float(ca2[i][l]), 2)
                            else:
                                min1 = 1
                            abc.append(min1)
                    abc1=min(abc)
                    abc2.append(abc1)
            abc3=max(abc2)
            xx.append(abc3)
        xx1.append(xx)
    yy1=[]
    for i in range(len(ca2)):
        yy1.append(ca2[i][lie-1])
    unique1=[]
    for i in range(len(result)):
        zzz=xx1[i]
        zmin=[]
        for j in range(len(xx1[i])):
            aaa=min(zzz[j],yy1[j])
            zmin.append(aaa)
        zzmin1 = np.array(zmin)
        sum1 = round(zzmin1.sum(), 2)
        yy2 = np.array(yy1)
        sum2 = round(yy2.sum(), 2)
        unique=round(sum1/sum2,6)
        unique1.append(unique)
    return unique1
