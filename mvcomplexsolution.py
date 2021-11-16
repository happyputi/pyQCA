from tkinter import *
import csv
import codecs
import numpy as np
import pandas as pd
import os
import itertools
import mvminization
import mvcomplexcalculate
def mvcomplex():
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
    complexsolution0,complexsolution01=mvminization.mvminizationsolution(tru0,mv1)
    result=mvcomplexcalculate.mvcalculatesolution(complexsolution0,0)
    tru0 = []
    for i in range(hang):
        a = ca1[i][lie - 4]
        b = ca1[i][lie - 1]
        if (a == '1'and b=="0"):
            cas = ''
            for j in range(lie - 3):
                cas = cas + ca1[i][j]
            tru0.append(cas)
    complexsolution1,complexsolution11=mvminization.mvminizationsolution(tru0,mv1)
    result=mvcomplexcalculate.mvcalculatesolution(complexsolution1,1)
    tru0 = []
    for i in range(hang):
        a = ca1[i][lie - 4]
        b = ca1[i][lie - 1]
        if (a == '2'and b=="0"):
            cas = ''
            for j in range(lie - 3):
                cas = cas + ca1[i][j]
            tru0.append(cas)
    if len(tru0)!=0:
        complexsolution2,complexsolution21=mvminization.mvminizationsolution(tru0,mv1)
        result=mvcomplexcalculate.mvcalculatesolution(complexsolution2,2)
    tru0 = []
    for i in range(hang):
        a = ca1[i][lie - 4]
        b = ca1[i][lie - 1]
        if (a == '3'and b=="0"):
            cas = ''
            for j in range(lie - 3):
                cas = cas + ca1[i][j]
            tru0.append(cas)
    if len(tru0)!=0:
        complexsolution3,complexsolution31=mvminization.mvminizationsolution(tru0,mv1)
        result=mvcomplexcalculate.mvcalculatesolution(complexsolution3,3)
    tru0 = []
    for i in range(hang):
        a = ca1[i][lie - 4]
        b = ca1[i][lie - 1]
        if (a == '4'and b=="0"):
            cas = ''
            for j in range(lie - 3):
                cas = cas + ca1[i][j]
            tru0.append(cas)
    if len(tru0)!=0:
        complexsolution4,complexsolution31=mvminization.mvminizationsolution(tru0,mv1)
        result=mvcomplexcalculate.mvcalculatesolution(complexsolution4,4)
    tru0 = []
    for i in range(hang):
        a = ca1[i][lie - 4]
        b = ca1[i][lie - 1]
        if (a == '5'and b=="0"):
            cas = ''
            for j in range(lie - 3):
                cas = cas + ca1[i][j]
            tru0.append(cas)
    if len(tru0)!=0:
        complexsolution5,complexsolution31=mvminization.mvminizationsolution(tru0,mv1)
        result=mvcomplexcalculate.mvcalculatesolution(complexsolution5,5)
