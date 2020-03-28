import os
import importlib
import sys

def getSqlFromModule(script):
    moduleName=os.path.splitext(script)[0]
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