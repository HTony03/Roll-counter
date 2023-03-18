# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 16:18:41 2022

@author: hpx
"""

import pandas
import random,configparser
import os,base64
"""
from tkinter import *
root = Tk()
root.title("random name")
root.geometry("300x100+630+80")
root.mainloop()
"""
def rand(named,num):
    name2 = []
    for i in range(num):
        d = random.randint(0,len(named)-1)
        name2.append(named.iloc[d,1])
        named = named.drop(d)
        named.reset_index(drop=True,inplace=True)
    for a in range(len(name2)):
        print(base64.b64decode(name2[a]).decode("UTF-8"))


def cfgdef():
    cfg_file = r"C:\\random.cfg"
    conf = configparser.ConfigParser()
    cfgfile = open(cfg_file,"w")
    conf.add_section("csv_route")
    conf.set("csv_route","CSV_all",r"C:\rand\all.csv")
    conf.set("csv_route","CSV_girls",r"C:\rand\girl.csv")
    conf.set("csv_route","CSV_boys",r"C:\rand\boy.csv")
    conf.add_section("random_configs")
    while 1:
        try:
            languages = int(input("language(1:English,2:Chinese):"))
        except ValueError:
            print("Input error")
        else:
            if languages != 1 and languages != 2:
                print("Input error")
            else:
                break
    if languages == 1:
        conf.set("random_configs","language","English")
    else:
        conf.set("random_configs","language","Chinese")
    conf.write(cfgfile)
    cfgfile.close()
    print("config saved to ",(cfg_file))


    
#read cfg
cfg_file = r"C:\\random.cfg"
while 1:
    if os.path.exists(os.path.join(os.getcwd(),cfg_file)):
        config = configparser.ConfigParser()
        config.read(cfg_file)
        routeall = config.get("csv_route","csv_all")
        routeboys = config.get("csv_route","csv_boys")
        routegirls = config.get("csv_route","csv_girls")
        languages = config.get("random_configs","language")
        break
    else:
        cfgdef()
if os.path.exists(os.path.join(os.getcwd(),routeall)) and os.path.exists(os.path.join(os.getcwd(),routeboys)) and os.path.exists(os.path.join(os.getcwd(),routegirls)):
    pass
else:
    print("files in random.cfg does not all exists")
    print("please check the random.cfg")
    os.system("pause")
    exit()
if languages != "Chinese" and languages != "English":
    print("The language config in random.cfg is not right")
    print("please check the random.cfg")
    os.system("pause")
    exit()

#language
rage = 1
if languages == "Chinese":
    lang = 2
else:
    lang = 1


################################

while rage != 0:
    
    ############model########
    while 1:
        try:
            if lang == 1:
                mode = int(input("name model(1:all students 2:girls 3:boys):"))
            elif lang == 2:
                mode = int(input("学生模型(1:所有学生 2:女同学 3:男同学):"))
            else:
                if lang == 1:
                    print("Input error")
                else:
                    print("输入错误")
        except ValueError:
            if lang == 1:
                print("Input error")
            else:
                print("输入错误")
        else:
            if mode != 1 and mode != 2 and mode != 3:
                if lang == 1:
                    print("Input error")
                else:
                    print("输入错误")
            else:
                break
    ########################
    
    #auto_choose_model
    if mode == 1:
        name = pandas.read_csv(os.path.join(os.getcwd(),routeall),encoding="ANSI",index_col=False)
    elif mode == 2:
        name = pandas.read_csv(os.path.join(os.getcwd(),routegirls),encoding="ANSI",index_col=False)
    elif mode == 3:
        name = pandas.read_csv(os.path.join(os.getcwd(),routeboys),encoding="ANSI",index_col=False)
    
    
    if lang == 1:
        print("max student num:",len(name))
        while 1:
            try:
                num = int(input("num of students:"))
                rand(name,num)
            except ValueError:
                print("Input error")
            else:
                break
        while 1:
            try:
                rage = int(input("again?(0:no 1:yes):"))
            except ValueError:
                print("Input error")
            else:
                if rage != 0 and rage != 1:
                    print("Input error")
                else:
                    break
    elif lang == 2:
        print("最大人数:",len(name))
        while 1:
            try:
                num = int(input("随机人数:"))
                rand(name,num)
            except ValueError:
                print("输入错误")
            else:
                break
        while 1:
            try:
                rage = int(input("再来一次?(0:否 1:是):"))
            except ValueError:
                print("输入错误")
            else:
                if rage != 0 and rage != 1:
                    print("输入错误")
                else:
                    break
os.system("pause")

