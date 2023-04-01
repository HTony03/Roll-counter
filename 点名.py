# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 16:18:41 2022

@author: HTony03
"""

import pandas
import random,configparser
import os,base64
from configparser import NoOptionError

"""
from tkinter import *
root = Tk()
root.title("random name")
root.geometry("300x100+630+80")
root.mainloop()
"""

class choose():
    def __init__(self):
        self.modepg1 = 0
        self.modepg2 = 0
    def __call__(self,page):
        if page == 1:
            return self.modepg1
        else:
            return self.modepg2
    def choose(self,lang,self_config_csv1_name,self_config_csv2_name,self_config_csv3_name):
        choosed = 0
#        global modepg1
#        global modepg2
        while choosed == 0 and self.modepg2 != 4:
############pg1
            while 1:
                try:
                    if lang == 1:
                        self.modepg1 = int(input("name model(1:all students 2:girls 3:boys 4:others):"))
                    elif lang == 2:
                        self.modepg1 = int(input("学生模型(1:所有学生 2:女同学 3:男同学 4:其他):"))
                except ValueError:
                    if lang == 1:
                        print("Input error")
                    else:
                        print("输入错误")
                else:
                    if self.modepg1 != 1 and self.modepg1 != 2 and self.modepg1 != 3 and self.modepg1 != 4:
                        if lang == 1:
                            print("Input error")
                        else:
                            print("输入错误")
                    else:
                        if self.modepg1 == 4:
                            choosed == 0
                        else:
                            choosed = 1
                        self.modepg2 = 5
                        break
############pg2
            if choosed == 0:
                while 1:
                    try:
                        if lang == 1:
                            self.modepg2 = int(input("name model(1:"+self_config_csv1_name+" 2:"+self_config_csv2_name+" 3:"+self_config_csv3_name+" 4:previous page):"))
                        elif lang == 2:
                            self.modepg2 = int(input("学生模型(1:"+self_config_csv1_name+" 2:"+self_config_csv2_name+" 3:"+self_config_csv3_name+" 4:上一页):"))
                    except ValueError:
                        if lang == 1:
                            print("Input error")
                        else:
                            print("输入错误")
                    else:
                        if self.modepg2 != 1 and self.modepg2 != 2 and self.modepg2 != 3 and self.modepg2 != 4:
                            if lang == 1:
                                print("Input error")
                            else:
                                print("输入错误")
                        else:
                            choosed = 1
                            break
    def modepg1(self):
        return self.modepg1
    def modepg2(self):
        return self.modepg2

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





def readcsv(route):
    return pandas.read_csv(os.path.join(os.getcwd(),route),encoding="ANSI",index_col=False)

def checklen(orignal,readlen,lang):
       if len(orignal) != int(readlen):
           if lang == 1:
               print("length in the cfg file does not mach the csv file")
               print("please check the cfg file and the csv file")
           else:
               print("cfg中长度与csv文件不一致")
               print("请检查cfg文件与csv文件")
           os.system("pause")
           exit()
       else:
           pass

def rand(named,num):
    name2 = []
    for i in range(num):
        d = random.randint(0,len(named)-1)
        name2.append(named.iloc[d,1])
        named = named.drop(d)
        named.reset_index(drop=True,inplace=True)
    for a in range(len(name2)):
        print(base64.b64decode(name2[a]).decode("UTF-8"))
        
def rand_del(named,num,location,model_index):
    name2 = []
    for i in range(num):
        d = random.randint(0,len(named)-1)
        name2.append(named.iloc[d,1])
        named = named.drop(d)
        named.reset_index(drop=True,inplace=True)
    for a in range(len(name2)):
        print(base64.b64decode(name2[a]).decode("UTF-8"))
    named.to_csv(os.path.join(os.getcwd(),location),mode="w",encoding="ANSI",index=False)
    
    
    cfg_file = r"C:\\random.cfg"
    conf = configparser.ConfigParser()
    conf.read(cfg_file)
    config = open(cfg_file,"w")
    name = pandas.read_csv(os.path.join(os.getcwd(),location),encoding="ANSI",index_col=False)
    conf.set("csv_route","self_config_csv"+str(model_index)+"_len",str(len(name)))
    conf.write(config)
    config.close()


def cfgdef():
    # -*- coding: utf-8 -*-
    """
    Created on Thu Mar 16 10:07:52 2023

    @author: HTony03
    """

    import configparser,os,pandas
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

    if os.path.exists(r"C:\rand\all.csv") and os.path.exists(r"C:\rand\girl.csv") and os.path.exists(r"C:\rand\boy.csv"):
        nameall = pandas.read_csv(r"C:\rand\all.csv",encoding="ANSI",index_col=False)
        nameboy = pandas.read_csv(r"C:\rand\boy.csv",encoding="ANSI",index_col=False)
        namegirl = pandas.read_csv(r"C:\rand\girl.csv",encoding="ANSI",index_col=False)
        conf.set("csv_route","CSV_all_len",str(len(nameall)))
        conf.set("csv_route","CSV_boys_len",str(len(nameboy)))
        conf.set("csv_route","CSV_girls_len",str(len(namegirl)))
    else:
        print(""""csv files are not in C:\ rand\ folder""")
        print("please rewrite the route or put the csv file into the folder and run the write_len.exe or write_len.py")
    conf.write(cfgfile)
    cfgfile.close()
    print("config saved to ",(cfg_file))
    os.system("pause")


def reget_len():
    global self_config_csv1_len
    global self_config_csv2_len
    global self_config_csv3_len
    cfg_file = r"C:\\random.cfg"
    config = configparser.ConfigParser()
    config.read(cfg_file)
    try:
        self_config_csv1_len = config.get("csv_route","self_config_csv1_len")
    except NoOptionError:
        pass
    try:
        self_config_csv2_len = config.get("csv_route","self_config_csv2_len")
    except NoOptionError:
        pass
    try:
        self_config_csv3_len = config.get("csv_route","self_config_csv3_len")
    except NoOptionError:
        pass

#read cfg
cfg_file = r"C:\\random.cfg"
while 1:
    if os.path.exists(os.path.join(os.getcwd(),cfg_file)):
        config = configparser.ConfigParser()
        config.read(cfg_file)
        routeall = config.get("csv_route","csv_all")
        routeboys = config.get("csv_route","csv_boys")
        routegirls = config.get("csv_route","csv_girls")
        lenall = config.get("csv_route","csv_all_len")
        lenboys = config.get("csv_route","csv_boys_len")
        lengirls = config.get("csv_route","csv_girls_len")
        languages = config.get("random_configs","language")
        try:
            self_config_csv1_route = config.get("csv_route","self_config_csv1_route")
            self_config_csv1_name = config.get("csv_route","self_config_csv1_name")
            self_config_csv1_len = config.get("csv_route","self_config_csv1_len")
            self_config_csv1_delete_name = config.get("csv_route","self_config_csv1_delete_name")
        except NoOptionError:
            self_config_csv1_route = ""
            self_config_csv1_name = "NULL"
        else:
            if self_config_csv1_route == "":
                self_config_csv1_route = ""
                self_config_csv1_name = "NULL"
        try:
            self_config_csv2_route = config.get("csv_route","self_config_csv2_route")
            self_config_csv2_name = config.get("csv_route","self_config_csv2_name")
            self_config_csv2_len = config.get("csv_route","self_config_csv2_len")
            self_config_csv2_delete_name = config.get("csv_route","self_config_csv2_delete_name")
        except NoOptionError:
            self_config_csv2_route = ""
            self_config_csv2_name = "NULL"
        else:
            if self_config_csv2_route == "":
                self_config_csv2_route = ""
                self_config_csv2_name = "NULL"
        try:
            self_config_csv3_route = config.get("csv_route","self_config_csv3_route")
            self_config_csv3_name = config.get("csv_route","self_config_csv3_name")
            self_config_csv3_len = config.get("csv_route","self_config_csv3_len")
            self_config_csv3_delete_name = config.get("csv_route","self_config_csv3_delete_name")
        except NoOptionError:
            self_config_csv3_route = ""
            self_config_csv3_name = "NULL"
        else:
            if self_config_csv3_route == "":
                self_config_csv3_route = ""
                self_config_csv3_name = "NULL"
        break
    else:
        cfgdef()
if languages != "Chinese" and languages != "English":
    print("The language config in random.cfg is not right")
    print("please check the random.cfg")
    os.system("pause")
    exit()
if languages == "Chinese":
    lang = 2
else:
    lang = 1
if os.path.exists(os.path.join(os.getcwd(),routeall)) and os.path.exists(os.path.join(os.getcwd(),routeboys)) and os.path.exists(os.path.join(os.getcwd(),routegirls)):
    pass
else:
    if lang == 1:
        print("files in random.cfg does not all exists")
        print("please check the random.cfg")
    else:
        print("cfg中文件不都存在")
        print("请检查random.cfg")
    os.system("pause")
    exit()


#language
rage = 1


custom_csv = "False"
################################

while rage != 0:
    while 1:
        tempory = choose()
        tempory.choose(lang,self_config_csv1_name,self_config_csv2_name,self_config_csv3_name)
        namepg1 = tempory.__call__(1)
        namepg2 = tempory.__call__(2)
        checknull = 0
        if namepg1 == 1:
            name = readcsv(routeall)
            checklen(name, lenall,lang)
            break
        elif namepg1 == 2:
            name = readcsv(routeboys)
            checklen(name, lengirls,lang)
            break
        elif namepg1 == 3:
            name = readcsv(routeboys)
            checklen(name, lenboys,lang)
            break
        else:
            custom_csv = "True"
            if namepg2 == 1:
                if self_config_csv1_route == "":
                    if lang == 1:
                        print("the model you choose is null")
                    else:
                        print("所选的为空模型")
                    
                else:
                    name = readcsv(self_config_csv1_route)
                    checklen(name,self_config_csv1_len,lang)
                    del_name = self_config_csv1_delete_name
                    loc = self_config_csv1_route
                    model_index = 1
                    break
            elif namepg2 == 2:
                if self_config_csv2_route == "":
                    if lang == 1:
                        print("the model you choose is null")
                    else:
                        print("所选的为空模型")
                else:
                    name = readcsv(self_config_csv2_route)
                    checklen(name,self_config_csv2_len,lang)
                    del_name = self_config_csv2_delete_name
                    loc = self_config_csv2_route
                    model_index = 2
                    break
            elif namepg2 == 3:
                if self_config_csv2_route == "":
                    if lang == 1:
                        print("the model you choose is null")
                    else:
                        print("所选的为空模型")
                else:
                    name = readcsv(self_config_csv3_route)
                    checklen(name,self_config_csv3_len,lang)
                    del_name = self_config_csv3_delete_name
                    loc = self_config_csv3_route
                    model_index = 3
                    break
            
    
    if lang == 1:
        print("max student num:",len(name))
        while 1:
            try:
                num = int(input("num of students:"))
                if custom_csv == "True" and del_name == "True":
                    rand_del(name,num,os.path.join(os.getcwd(),loc),model_index)
                    reget_len()
                else:
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
                if custom_csv == "True" and del_name == "True":
                    rand_del(name,num,os.path.join(os.getcwd(),loc),model_index)
                    reget_len()
                else:
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

