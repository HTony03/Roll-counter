# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 22:17:33 2023

@author: HTony03
"""



import pandas
import random,configparser
import os,base64
from configparser import NoOptionError

cfg_file = r"C:\\random.cfg"

config = configparser.ConfigParser()
config.read(cfg_file)
routeall = config.get("csv_route","csv_all")
routeboys = config.get("csv_route","csv_boys")
routegirls = config.get("csv_route","csv_girls")
lenall = config.get("csv_route","csv_all_len")
lenboys = config.get("csv_route","csv_boys_len")
lengirls = config.get("csv_route","csv_girls_len")
languages = config.get("random_configs","language")
def readcsv(route):
    return pandas.read_csv(os.path.join(os.getcwd(),route),encoding="ANSI",index_col=False)

def createcsv(lang):
    while 1:
        try:
            if lang == 1:
                model = int(input("copy from which name model(1:all students 2:girls 3:boys):"))
            elif lang == 2:
                model = int(input("从哪个学生模型复制(1:所有学生 2:女同学 3:男同学):"))
        except ValueError:
            if lang == 1:
                print("Input error")
            else:
                print("输入错误")
        else:
            if model != 1 and model != 2 and model != 3:
                if lang == 1:
                    print("Input error")
                else:
                    print("输入错误")
            else:
                break
        
    if lang == 1:
        name = input("the model name:")
        while 1:
            try:
                index = int(input("index of the model:"))
            except ValueError:
                print("Input error")
            else:
                if index != 1 and index != 2 and index != 3:
                    print("Input error")
                else:
                    break
        while 1:

            del_name = input("delete name after chosen it(True:yes,False:no):")
            if del_name != "True" and del_name != "False":
                print("输入错误")
            else:
                break
    else:
        name = input("模型名称:")
        while 1:
            try:
                index = int(input("模型序号:"))
            except ValueError:
                print("输入错误")
            else:
                if index != 1 and index != 2 and index != 3:
                    print("输入错误")
                else:
                    break
        while 1:
            del_name = input("摇到名字后是否删除名字(True:是,False:否):")
            if del_name != "True" and del_name != "False":
                print("输入错误")
            else:
                break
        #copy csv
        if model == 1:
            names = readcsv(routeall)
        elif model == 2:
            names = readcsv(routeboys)
        elif model == 3:
            names = readcsv(routeboys)
        try:
            names.to_csv(r"""C:\rand\ """+name+".csv",mode="x",encoding="ANSI",index=False)
        except FileExistsError:
            name = "custom_config"+str(index)
            names.to_csv(r"""C:\rand\ """+name+".csv",mode="x",encoding="ANSI",index=False)
        #
        cfg_file = r"C:\\random.cfg"
        conf = configparser.ConfigParser()
        cfgfile = open(cfg_file,"r+")
        conf.read(cfg_file)
        conf.set("csv_route","self_config_csv"+str(index)+"_name",name)
        conf.set("csv_route","self_config_csv"+str(index)+"_len",str(len(names)))
        conf.set("csv_route","self_config_csv"+str(index)+"_route",r"""C:\rand\ """+name+".csv")
        conf.set("csv_route","self_config_csv"+str(index)+"_delete_name",del_name)
        conf.write(cfgfile)
        cfgfile.close()
        
        print("new csv created as "+name+".csv in the rand folder")
if languages == "Chinese":
    lang = 2
else:
    lang = 1
createcsv(lang)
os.system("pause")