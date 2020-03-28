import os
import sys
import constant
from tkinter import messagebox
import dbModule as dB
import timeModule as tM
import datetime
import utility.common as common

def findScripts():
    scriptNames=[]
    exceptionCheck=0
    try:
        for script in os.listdir(constant.PATH):
            if script.endswith(".py"):
                scriptNames.append(script)
    except Exception as e:
        exceptionCheck=1
        print("Directory not found for scripts: "+str(e))
        raise
    if len(scriptNames)==0 and exceptionCheck==0:
        messagebox.showinfo("Error","No scripts with proper extension found on the PATH:"+constant.PATH)
    print ("Files with proper extensions:"+str(scriptNames))
    return scriptNames

def sortScriptsWithTime(scriptNames):
    temp=[]
    for script in scriptNames:
        startIndex=script.find('_')
        endIndex=script.find('.')
        temp.append(int(script[(startIndex+1):(endIndex)])) #taking only timestamp and making a list
    n=len(temp)
    try:
        for i in range(0,n,1):
            for k in range(0,n-i-1,1):
                if temp[k]>temp[k+1]:
                    tem=temp[k]
                    temf=scriptNames[k]
                    temp[k]=temp[k+1]
                    scriptNames[k]=scriptNames[k+1]
                    temp[k+1]=tem
                    scriptNames[k+1]=temf
    except Exception as e:
        print("Exception Occured: "+str(e))
        raise
    print("After sorting the order is:"+str(scriptNames))
    return scriptNames

def insertScriptsForUp(script):
    tuple=[]
    now=datetime.datetime.now()
    lowDate=tM.getLowDate()
    objTuple=(script,1,now,0,lowDate)
    tuple.append(objTuple)
    try:
        dB.insertScript(tuple)
    except Exception as e:
        raise

def getAllScriptsForUp():
    allScriptDict=[]
    scriptNames=[]
    try:
        allScriptDict=dB.getAllScriptsFromDBForUp()
    except Exception as e:
        raise
    for script in allScriptDict:
        scriptNames.append(script['script_name'])
    return scriptNames

def runScripts(scriptsFromPath,scriptsFromDB):
    filterdlist=[]
    for file in scriptsFromPath:
        if file not in scriptsFromDB:
            filterdlist.append(file)
    print("Not In DB: "+str(filterdlist))
    if constant.PATH not in sys.path:
        sys.path.append(constant.PATH)     #inserting path of the scripts on run time
    for script in filterdlist:
        query=common.getSqlFromModule(script)
        print ("The query fetched from script is :"+str(query))
        try:
            dB.runQuery(query)
        except Exception as e:
            messagebox.showinfo("Error","Script has some problem :"+str(script))
            print("stoping executing next script")
            return
        print("Script executed succesfully :"+str(script))
        insertScriptsForUp(script)

def createScript(fileName):
    rootPath=os.path.dirname(os.path.realpath(__file__))
    templatePath=os.path.join(rootPath,"internal_files")    
    tStamp=tM.getDate()
    fileName=fileName+"_"+tStamp+".py"
    fp=None
    fp1=None
    try:
        fp1=open((os.path.join(templatePath,constant.TEMPLATE)),'r')
        content=fp1.read()
        fp=open((os.path.join(constant.PATH,fileName)),'a+')
        print("File Created With Name : "+fileName)
        fp.write(content)
    except Exception as e:
        messagebox.showinfo("Error","Can not create file on specific path: "+str(e))
        raise
    finally:
        if fp1 is not None:
            fp1.close()
        if fp is not None:
            fp.close()    




