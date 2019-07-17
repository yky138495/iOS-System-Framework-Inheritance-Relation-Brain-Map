import requests
import time
import os
import json
import sqlite3
import re
import sys
import codecs
from itertools import islice
from bs4 import BeautifulSoup



current_file_path = os.path.abspath(os.path.dirname(__file__))
print(current_file_path)

filename = os.path.split(current_file_path)[1]
print(filename)

base_path = current_file_path + '/'
framework_name=filename
framework_ext='.framework'

db_base_path = base_path
file_dir = db_base_path

execute_str="CREATE TABLE sys_framework(\
ID  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,\
name  TEXT UNIQUE  NOT NULL,\
super_name  TEXT  NOT NULL,\
type  TEXT ,\
dome  TEXT ,\
protol  TEXT);"


if __name__ == "__main__":
   
  path=db_base_path+framework_name+'.db'
  print(path)

  #DB
  conn = sqlite3.connect(path)
  c = conn.cursor()
  
  print("Opened database successfully")
  try:
    c.execute(execute_str)
    conn.commit()
  except (sqlite3.OperationalError or sqlite3.IntegrityError):
    print(file_dir)
          
  walk_path=base_path+framework_name+framework_ext+'/Headers/'
  print(walk_path)

  for root,dirs,files in os.walk(walk_path):
    for name in files:
      name_path = os.path.join(root,name)
      f = open(name_path)
      str = f.read()
      p = r'@interface ([a-zA-Z]*) : ([a-zA-Z]*)'
      aa = re.search(p, str)
      str_aa=''
      if aa:
        str_aa = aa.group()

      p1 = r'@interface ([a-zA-Z]*) :'   
      aa1 = re.search(p1, str)
      stra= ''
      if aa1:
        stra = aa1.group()

      super_name = str_aa.replace(stra,'')
      super_name = super_name.replace(' ','')

      if super_name:
          name_t = name.replace('.h','')
          type1 = name + '--'+framework_name
          strsql = "INSERT INTO sys_framework (name,super_name,type) VALUES ('" + name_t + "','" + super_name + "','" + type1+ "')"
          print(strsql)
          try:
            c.execute(strsql)
            conn.commit()
          except sqlite3.IntegrityError:
            print(sqlite3.IntegrityError)
     
      
    for name in dirs:
      print('dir name = ' + name)
      

 






