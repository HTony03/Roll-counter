# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 16:18:41 2022

@author: hpx
"""

import pandas
import random,configparser
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

rage = 1
while 1:
    try:
        lang = int(input("language(1:English 2:中文):"))
        if lang != 1 and lang != 2:
            print("输入错误")
        else:
            break
    except ValueError:
        print("输入错误")
    else:
        break
    
#read cfg
cfg_file = r"C:\\random.cfg"
if os.path.exists(os.path.join(os.getcwd(),cfg_file)):
    config = configparser.ConfigParser()
    config.read(cfg_file)
    routeall = config.get("csv_route","csv_all")
    routeboys = config.get("csv_route","csv_boys")
    routegirls = config.get("csv_route","csv_girls")
if os.path.exists(os.path.join(os.getcwd(),routeall)) and os.path.exists(os.path.join(os.getcwd(),routeboys)) and os.path.exists(os.path.join(os.getcwd(),routegirls)):
    pass
else:
    print("files in random.cfg does not all exists")
    print("please check the random.cfg")
    os.system("pause")
    exit()
#


################################

while rage != 0:
    if lang == 1:
        mode = int(input("name model(1:all students 2:girls 3:boys):"))
    elif lang == 2:
        mode = int(input("学生模型(1:所有学生 2:女同学 3:男同学):"))
    if mode == 1:
        name = pandas.read_csv(os.path.join(os.getcwd(),routeall),encoding="ANSI",index_col=False)
    elif mode == 2:
        name = pandas.read_csv(os.path.join(os.getcwd(),routegirls),encoding="ANSI",index_col=False)
    elif mode == 3:
        name = pandas.read_csv(os.path.join(os.getcwd(),routeboys),encoding="ANSI",index_col=False)
################################
#name = []
    if lang == 1:
        print("max student num:",len(name)-1)
        num = input("num of students:")
        rand(name,num)
        rage = int(input("again?(0:no 1:yes):"))
    elif lang == 2:
        print("最大人数:",len(name)-1)
        num = input("随机人数:")
        rand(name,num)
        rage = int(input("再来一次?(0:否 1:是):"))
os.system("pause")

