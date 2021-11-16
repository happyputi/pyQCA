import csv
import codecs
import numpy as np
import pandas as pd
import os
import itertools
data = pd.read_csv("case.csv",header=None)
source=np.array(data)
ca4=np.delete(source,0,0)
ca1=np.delete(ca4,ca4.shape[1]-1,1)
hang=ca1.shape[0]
lie=ca1.shape[1]
ca2=[]
ca6=ca4[:,lie]
ca5=[float(i) for i in ca6]
for i in range(hang):
    ca2.append([float(j) for j in ca1[i]])
matrix1 = [[1.00]*(lie)]*(hang)
matrix=np.array(matrix1)
ca=np.array(ca2)
noca = matrix-ca
def truthtable():
    title=[]
    biao = source[0]
    for i in range(len(biao)):
      title.append(biao[i])
    title1 =["number","raw consist","logicalitem"]
    title.extend(title1)
    #print(title)
    with open("truthtable.csv", "a", newline="", encoding="utf-8") as csvfile1:
        writer = csv.writer(csvfile1, delimiter=',')
        writer.writerow(title)
    with open("truthtablebackup.csv", "a", newline="", encoding="utf-8") as csvfile1:
        writer = csv.writer(csvfile1, delimiter=',')
        writer.writerow(title)
    table1 = list(itertools.product([False,True],repeat=lie))
    table2 = np.array(table1)
    table3 = list(itertools.product([True, False], repeat=lie))
    table4 = np.array(table3)
    table = table2 + 0
    nottable = table4 + 0
    for j in range(len(table)):
        num = 0
        min3 = 0
        min5 = 0
        for i in range(len(ca)):
            mul1 = np.multiply(np.array(table[j]), np.array(ca[i]))
            mul2 = np.multiply(np.array(nottable[j]), np.array(noca[i]))
            mul = mul1 + mul2
            min1 = min(mul)
            min1 = round(min1,2)
            if min1 > 0.5:
                num = num + 1
            tablelist = table[j].tolist()
            min3 = min3 + min1
            min2 = min(min1, ca5[i])
            min5 = min5 + min2
        if num == 0:
            tablelist.append("")
            tablelist.append(num)
            tablelist.append("")
            tablelist.append(1)
        else:
            rawcon = min5 / min3
            if (rawcon>=0.8):
                tablelist.append(1)
                tablelist.append(num)
            else:
                tablelist.append(0)
                tablelist.append(num)
            tablelist.append("%.6f" % rawcon)
            tablelist.append(0)
        with open("truthtable.csv", "a", newline="", encoding="utf-8") as csvfile1:
            writer = csv.writer(csvfile1, delimiter=',')
            writer.writerow(tablelist)
        with open("truthtablebackup.csv", "a", newline="", encoding="utf-8") as csvfile1:
            writer = csv.writer(csvfile1, delimiter=',')
            writer.writerow(tablelist)
truthtable()

