# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 13:51:35 2023

@author: Arribaat
"""

import json,os
#app dir handling
def find_app_dir():
    script_dir = os.path.dirname(os.path.abspath(__name__))
    root_dir = os.path.dirname(script_dir)
    app_dir = root_dir.split()
    return app_dir[0]

def write_path(username):
    app_dir = find_app_dir()
    global path_usr_data
    path_usr_data =  app_dir +"\\proyek_wallabi"+"\\usr_data\\"+username+".json"
    #+"\\Proyek_Wallabi" kalau di vs
    #tidak perlu kalau di .bat file
    return path_usr_data

def write_path_plan(username):
    app_dir = find_app_dir()
    global path_usr_data
    path_usr_data =  app_dir +"\\proyek_wallabi"+"\\usr_report\\"+username+"_report"+".json"
    #+"\\Proyek_Wallabi" kalau di vs
    #tidak perlu kalau di .bat file
    return path_usr_data

#create cache file
def usr_path_data_create(username):
    path_arr = []
    path_arr.append(path_usr_data)
    path_arr.append(username)
    with open("cache.json","w") as newfile: 
        json.dump(path_arr,newfile)
    return

def del_data():
    os.remove("cache.json")
    return

#read username
def read_username():
    with open("cache.json",'r') as path_data:
        path_var = json.load(path_data)
    return path_var[1]

#access username.json
def read_data(username):
    path_data = write_path(username)
    with open(path_data,"r") as datauser: 
        data_user = json.load(datauser) 
    return data_user
    
def add_data(username,user_arr):
    path_data = write_path(username)
    with open(path_data,'x') as newfile:
        json.dump(user_arr,newfile)
    return

def load_data(username,user_arr):
    path_data = write_path(username)
    with open(path_data,'w') as newcontent: 
        json.dump(user_arr,newcontent) 
    return

#access plan.json
def read_report(username):
    path_data = write_path_plan(username)
    with open(path_data,'r') as dataplan: 
        data_plan = json.load(dataplan) 
    return data_plan
    
def add_report(username):
    path_data = write_path_plan(username)
    plans_base_arr = []
    with open(path_data,'x') as newfile:
        json.dump(plans_base_arr,newfile)
    print("Saved succesfully")
    return plans_base_arr

def load_report(username,plans_arr):
    path_data = write_path_plan(username)
    with open(path_data,'w') as newcontent:
        json.dump(plans_arr,newcontent)
    return

        