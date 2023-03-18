# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 22:34:20 2023

@author: Administrator
"""
import pandas
import configparser
import os,base64


def b64(name):
    b64raw = str(name)
    tmp = b64raw.encode("utf-8")
    based = base64.b64encode(tmp)
    return based
    

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
    
nameall = pandas.read_csv(os.path.join(os.getcwd(),routeall),encoding="ANSI",index_col=False)
namegirl = pandas.read_csv(os.path.join(os.getcwd(),routegirls),encoding="ANSI",index_col=False)
nameboy = pandas.read_csv(os.path.join(os.getcwd(),routeboys),encoding="ANSI",index_col=False)
nameall['b64coded'] = nameall.apply(lambda x: b64(x['name']).decode("UTF-8"), axis=1)
namegirl['b64coded'] = namegirl.apply(lambda x: b64(x['name']).decode("UTF-8"), axis=1)
nameboy['b64coded'] = nameboy.apply(lambda x: b64(x['name']).decode("UTF-8"), axis=1)
nameall.to_csv(os.path.join(os.getcwd(),routeall),encoding="ANSI",index=False)
namegirl.to_csv(os.path.join(os.getcwd(),routegirls),encoding="ANSI",index=False)
nameboy.to_csv(os.path.join(os.getcwd(),routeboys),encoding="ANSI",index=False)
print("all csv had added base64 code")
os.system("pause")