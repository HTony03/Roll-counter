# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 10:08:10 2023

@author: HTony03
"""

import os
import configparser,pandas,random

cfg_file = r"C:\\random.cfg"
if os.path.exists(os.path.join(os.getcwd(),cfg_file)):
    config = configparser.ConfigParser()
    config.read(cfg_file)
    route1 = config.get("csv_route","csv_all")
    
if os.path.exists(os.path.join(os.getcwd(),route1)):
    name = pandas.read_csv(os.path.join(os.getcwd(),route1),encoding="ANSI",index_col=False)
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
else:
    print("file in random.cfg does not exists")
    print("please check the random.cfg")
    os.system("pause")