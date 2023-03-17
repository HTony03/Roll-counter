# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 13:57:52 2022

@author: admin
"""

import pandas
import random
import os,configparser
#cfg file
cfg_file = r"C:\\random.cfg"
if os.path.exists(os.path.join(os.getcwd(),cfg_file)):
    config = configparser.ConfigParser()
    config.read(cfg_file)
    routeall = config.get("csv_route","csv_all")
if os.path.exists(os.path.join(os.getcwd(),routeall)):
    pass
else:
    print("files in random.cfg does not exists")
    print("please check the random.cfg")
    os.system("pause")
    exit()
#

name = pandas.read_csv(os.path.join(os.getcwd(),routeall),encoding="ANSI",index_col=False)
num= 1
name2 = []

for i in range(int(num)):
    d = random.randint(0,len(name)-1)
    name2.append(name.iloc[d,0])
    named = name.drop(d)
    named.reset_index(drop=True,inplace=True)


for a in range(len(name2)):
    print(name2[a])
os.system("pause")
