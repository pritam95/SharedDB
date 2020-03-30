import os
import importlib
import sys
from tkinter import messagebox
import re
import utility.constant as constant

def getSqlFromModule(script):
    moduleName=os.path.splitext(script)[0]             #omiting the extension of a file name
    print ("Module to be imported: "+str(moduleName))
    mod=importlib.import_module(moduleName)
    query=mod.up()
    if moduleName in sys.modules:   
        del(sys.modules[moduleName])
    return query

def createDictionary(cursor):
    list=[]
    columnNames=cursor.column_names
    noOfCol=len(columnNames)
    for result in cursor.fetchall():
        dict={}
        for i in range(0,noOfCol,1):
            dict[columnNames[i]]=result[i]
        list.append(dict)
    print(list)

def nameValidator(name):
    if name=='':
        messagebox.showinfo("Error","Name is blank")
        return False
    if name.find(' ') != -1:
        messagebox.showinfo("Error","Can not contain space in name")
        return False
    regex=re.compile(constant.SPECIALCHARACTER)
    if regex.search(name):
        messagebox.showinfo("Error","Can not contain any special charectar")
        return False
    return True
      
