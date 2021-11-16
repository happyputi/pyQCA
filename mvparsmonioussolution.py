from tkinter import *
import csv
import codecs
import numpy as np
import pandas as pd
import os
import itertools
import mvminization
import mvparsmoniouscalculate
def mvparsmonious():
    data1=pd.read_csv("truthtable-mv.csv",header=None)
    source=np.array(data1)
    ca1=np.delete(source,0,0)
    hang=ca1.shape[0]
    lie=ca1.shape[1]
    data = pd.read_csv("numberofvariable.csv", header=None)
    source5 = np.array(data)
    lie1 = source5.shape[1]
    mv1 =[]
    for w in range(lie1):
        mv1.append(source5[0][w])
    print("the set of variables' number is:"+str(mv1))
    condi=[]
    for i in range(hang):
        if ca1[i][lie-1]=="0":
            condi1=[]
            for j in range(lie-4):
                condi1.append(ca1[i][j])
            condi.append(condi1)
    judg=[]
    for i in range(hang):
        condi1=[]
        for j in range(lie-4):
            condi1.append(ca1[i][j])
        judg.append(condi1)
    tru0 = []
    for i in range(hang):
        a = ca1[i][lie - 4]
        b = ca1[i][lie - 1]
        if (a == '0'and b=="0"):
            cas = ''
            for j in range(lie - 3):
                cas = cas + ca1[i][j]
            tru0.append(cas)
        if (b == '1'and judg[i] not in condi):
            cas = ''
            for j in range(lie - 4):
                cas = cas + ca1[i][j]
            cas = cas+"0"
            tru0.append(cas)
    parsmonioussolution0,parsmonioussolution01=mvminization.mvminizationsolution(tru0,mv1)
    result=mvparsmoniouscalculate.mvcalculatesolution(parsmonioussolution0,0)
    tru0 = []
    for i in range(hang):
        a = ca1[i][lie - 4]
        b = ca1[i][lie - 1]
        if (a == '1'and b=="0"):
            cas = ''
            for j in range(lie - 3):
                cas = cas + ca1[i][j]
            tru0.append(cas)
        if (b == '1'and judg[i] not in condi):
            cas = ''
            for j in range(lie - 4):
                cas = cas + ca1[i][j]
            cas = cas+"1"
            tru0.append(cas)
    parsmonioussolution1,parsmonioussolution11=mvminization.mvminizationsolution(tru0,mv1)
    result=mvparsmoniouscalculate.mvcalculatesolution(parsmonioussolution1,1)
    tru0 = []
    for i in range(hang):
        a = ca1[i][lie - 4]
        b = ca1[i][lie - 1]
        if (a == '2'and b=="0"):
            cas = ''
            for j in range(lie - 3):
                cas = cas + ca1[i][j]
            tru0.append(cas)
        if (b == '1'and judg[i] not in condi):
            cas = ''
            for j in range(lie - 4):
                cas = cas + ca1[i][j]
            cas = cas+"2"
            tru0.append(cas)
    if len(tru0)!=0:
        parsmonioussolution2,parsmonioussolution21=mvminization.mvminizationsolution(tru0,mv1)
        result=mvparsmoniouscalculate.mvcalculatesolution(parsmonioussolution2,2)
    tru0 = []
    for i in range(hang):
        a = ca1[i][lie - 4]
        b = ca1[i][lie - 1]
        if (a == '3'and b=="0"):
            cas = ''
            for j in range(lie - 3):
                cas = cas + ca1[i][j]
            tru0.append(cas)
        if (b == '1'and judg[i] not in condi):
            cas = ''
            for j in range(lie - 4):
                cas = cas + ca1[i][j]
            cas = cas+"3"
            tru0.append(cas)
    if len(tru0)!=0:
        parsmonioussolution3,parsmonioussolution31=mvminization.mvminizationsolution(tru0,mv1)
        result=mvparsmoniouscalculate.mvcalculatesolution(parsmonioussolution3,3)
    tru0 = []
    for i in range(hang):
        a = ca1[i][lie - 4]
        b = ca1[i][lie - 1]
        if (a == '4'and b=="0"):
            cas = ''
            for j in range(lie - 3):
                cas = cas + ca1[i][j]
            tru0.append(cas)
        if (b == '1'and judg[i] not in condi):
            cas = ''
            for j in range(lie - 4):
                cas = cas + ca1[i][j]
            cas = cas+"4"
            tru0.append(cas)
    if len(tru0)!=0:
        parsmonioussolution4,parsmonioussolution31=mvminization.mvminizationsolution(tru0,mv1)
        result=mvparsmoniouscalculate.mvcalculatesolution(parsmonioussolution4,4)
    tru0 = []
    for i in range(hang):
        a = ca1[i][lie - 4]
        b = ca1[i][lie - 1]
        if (a == '5'and b=="0"):
            cas = ''
            for j in range(lie - 3):
                cas = cas + ca1[i][j]
            tru0.append(cas)
        if (b == '1'and judg[i] not in condi):
            cas = ''
            for j in range(lie - 4):
                cas = cas + ca1[i][j]
            cas = cas+"5"
            tru0.append(cas)
    if len(tru0)!=0:
        parsmonioussolution5,parsmonioussolution31=mvminization.mvminizationsolution(tru0,mv1)
        result=mvparsmoniouscalculate.mvcalculatesolution(parsmonioussolution5,5)
