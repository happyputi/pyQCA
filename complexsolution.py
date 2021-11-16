from tkinter import *
import csv
import codecs
import numpy as np
import pandas as pd
import os
import itertools
import minization
import calculate
import translate
def complex():
    data1=pd.read_csv("truthtable.csv",header=None)
    source=np.array(data1)
    ca1=np.delete(source,0,0)
    hang=ca1.shape[0]
    lie=ca1.shape[1]
    tru=[]
    for i in range (hang):
        a = ca1[i][lie-4]
        if (a=='1'):
            cas = ''
            for j in range(lie-4):
                cas = cas+ca1[i][j]
            tru.append(cas)
    complexsolution=minization.find_prime_implicants(tru)
    result=calculate.calculatesolution(complexsolution)
    result1=translate.translate1(result)
    print ("solutions"+"\t"+"rawcoverage"+"\t"+"uniquecoverage"+"\t"+"consistency")
    for i in range(len(result1)):
        print (result1[i])
    print ("solutioncoverage:")
    print (result[len(result)-1][0])
    print ("solutionconsistency:")
    print (result[len(result)-1][1])
#complex()











