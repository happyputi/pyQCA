from tkinter import *
import csv
import codecs
import numpy as np
import pandas as pd
import os
import itertools
import mvminization
import mvintermediatecalculate
def mvintermediate():
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
    intermediatesolution0,intermediatesolution01=mvminization.mvminizationsolution(tru0,mv1)
    result=mvintermediatecalculate.mvcalculatesolution(intermediatesolution0,0)
    tru0 = []
    for i in range(hang):
        a = ca1[i][lie - 4]
        b = ca1[i][lie - 1]
        if (a == '1'and b=="0"):
            cas = ''
            for j in range(lie - 3):
                cas = cas + ca1[i][j]
            tru0.append(cas)
    intermediatesolution1,intermediatesolution11=mvminization.mvminizationsolution(tru0,mv1)
    result=mvintermediatecalculate.mvcalculatesolution(intermediatesolution1,1)
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
        intermediatesolution2,intermediatesolution21=mvminization.mvminizationsolution(tru0,mv1)
        result=mvintermediatecalculate.mvcalculatesolution(intermediatesolution2,2)
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
        intermediatesolution3,intermediatesolution31=mvminization.mvminizationsolution(tru0,mv1)
        result=mvintermediatecalculate.mvcalculatesolution(intermediatesolution3,3)
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
        intermediatesolution4,intermediatesolution31=mvminization.mvminizationsolution(tru0,mv1)
        result=mvintermediatecalculate.mvcalculatesolution(intermediatesolution4,4)
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
        intermediatesolution5,intermediatesolution31=mvminization.mvminizationsolution(tru0,mv1)
        result=mvintermediatecalculate.mvcalculatesolution(intermediatesolution5,5)
