# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 16:16:52 2023

@author: HTony03
"""

import configparser,os,pandas
cfg_file = r"C:\\random.cfg"
conf = configparser.ConfigParser()
conf.read(cfg_file)
config = open(cfg_file,"r+")

routeall = conf.get("csv_route","csv_all")
routeboys = conf.get("csv_route","csv_boys")
routegirls = conf.get("csv_route","csv_girls")

nameall = pandas.read_csv(os.path.join(os.getcwd(),routeall),encoding="ANSI",index_col=False)
nameboy = pandas.read_csv(os.path.join(os.getcwd(),routeboys),encoding="ANSI",index_col=False)
namegirl = pandas.read_csv(os.path.join(os.getcwd(),routegirls),encoding="ANSI",index_col=False)


conf.set("csv_route","CSV_all_len",str(len(nameall)))
conf.set("csv_route","CSV_boys_len",str(len(nameboy)))
conf.set("csv_route","CSV_girls_len",str(len(namegirl)))

conf.write(config)
config.close()
print("config saved to ",(cfg_file))
os.system("pause")
