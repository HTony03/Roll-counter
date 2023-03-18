# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 10:07:52 2023

@author: Administrator
"""

import configparser,os
cfg_file = r"C:\\random.cfg"
conf = configparser.ConfigParser()
cfgfile = open(cfg_file,"w")
conf.add_section("csv_route")
conf.set("csv_route","CSV_all",r"C:\rand\all.csv")
conf.set("csv_route","CSV_girls",r"C:\rand\girl.csv")
conf.set("csv_route","CSV_boys",r"C:\rand\boy.csv")
conf.add_section("random_configs")
conf.set("random_configs","language","English")
conf.write(cfgfile)
cfgfile.close()
print("config saved to ",(cfg_file))
os.system("pause")
