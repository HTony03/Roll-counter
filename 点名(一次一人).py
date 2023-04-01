# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 13:57:52 2022

@author: HTony03
"""

import pandas
import random
import os,configparser,base64
#cfg file
cfg_file = r"C:\\random.cfg"
if os.path.exists(os.path.join(os.getcwd(),cfg_file)):
    config = configparser.ConfigParser()
    config.read(cfg_file)
    routeall = config.get("csv_route","csv_all")
    lenall = config.get("csv_route","csv_all_len")
if os.path.exists(os.path.join(os.getcwd(),routeall)):
    pass
else:
    print("files in random.cfg does not exists")
    print("please check the random.cfg")
    os.system("pause")
    exit()
name = pandas.read_csv(os.path.join(os.getcwd(),routeall),encoding="ANSI",index_col=False)
if len(name) != int(lenall):
    print("length in the cfg file does not mach the csv file")
    print("please check the cfg file and the csv file")
    os.system("pause")
    os.exit()
num= 1
name2 = []
for i in range(num):
    d = random.randint(0,len(name)-1)
    name2.append(name.iloc[d,1])
    named = name.drop(d)
    named.reset_index(drop=True,inplace=True)
for a in range(len(name2)):
    print(base64.b64decode(name2[a]).decode("UTF-8"))
os.system("pause")
