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
    print(""""csv files are not in C:\rand\ folder""")
    print("please rewrite the route or put the csv file into the folder and run the write_len.exe or write_len.py")


conf.write(cfgfile)
cfgfile.close()
print("config saved to ",(cfg_file))
os.system("pause")
