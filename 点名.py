# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 16:18:41 2022

@author: hpx
"""

import pandas
import random
import os
"""
from tkinter import *
root = Tk()
root.title("random name")
root.geometry("300x100+630+80")
root.mainloop()
"""
def rand(named,num):
    name2 = []
    for i in range(int(num)):
        d = random.randint(0,len(named)-1)
        name2.append(named.iloc[d,0])
        named = named.drop(d)
        named.reset_index(drop=True,inplace=True)
    
   
    for a in range(len(name2)):
        print(name2[a])
#    print(named)
#rand([1,2,3,4,5],2)
rage = 1
################################
#name = pandas.read_csv(r"C:\Users\Administrator\Desktop\点名器\all.csv",encoding="ANSI",index_col=False)
while rage != 0:
    mode = int(input("name mode(1:all students 2:grils 3:boys):"))
    if mode == 1:
        name = pandas.read_csv(r"C:\Users\Administrator\Desktop\点名器\all.csv",encoding="ANSI",index_col=False)
    elif mode == 2:
        name = pandas.read_csv(r"C:\Users\Administrator\Desktop\点名器\gril.csv",encoding="ANSI",index_col=False)
    elif mode == 3:
        name = pandas.read_csv(r"C:\Users\Administrator\Desktop\点名器\boy.csv",encoding="ANSI",index_col=False)
################################
#name = []
    print("max student num:",len(name)-1)
    num = input("num of students:")
    rand(name,num)
    rage = int(input("again?(0:no 1:yes):"))
os.system("pause")
"""
for i in range(int(num)):
    d = random.randint(0,len(name)-1)
    name2.append(name[d])
"""
#print(name2)
"""
for i in range(int(num)):
    d = random.randint(0,len(name)-1)
    name2.append(name.iloc[d,0])
    name = name.drop(d)
    print(name)
print(name2)
"""
