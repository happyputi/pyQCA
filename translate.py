from tkinter import *
import csv
import codecs
import numpy as np
import pandas as pd
import os
import itertools
def translate1(data1):
    bxy=[]
    data = pd.read_csv("case.csv", header=None)
    source = np.array(data)
    condition1=source[0]
    condition = np.delete(condition1, len(condition1)-1, 0)
    bi=data1
    uvw=[]
    for i in range(len(bi)-1):
        bxy.append(bi[i][0])
    bk=[]
    for j in range(len(bxy)):
        tet=bxy[j]
        a=""
        for k in range(len(tet)):
            e=tet[k]
            if (k!=len(tet)-1):
                    if (e=="1"):
                        a=a+(condition[k])+"*"
                    elif(e=="0"):
                        a=a+ ("~"+condition[k])+"*"
            else:
                if (e=="1"):
                    a=a+(condition[k])
                elif(e=="0"):
                    a=a+ ("~"+condition[k])
        bk.append(a)
    for i in range(len(bi)-1):
        jkl=[]
        jkl.append(bk[i])
        for j in range(1,4):
            jkl.append(bi[i][j])
        uvw.append(jkl)
    return(uvw)
