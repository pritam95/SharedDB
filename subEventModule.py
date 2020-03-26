import os
import constant
from tkinter import messagebox
import dbModule as dB
import timeModule as tM
import datetime

def findScripts():
    scriptNames=[]
    exceptionCheck=0
    try:
        for script in os.listdir(constant.PATH):
            if script.endswith(".txt"):
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

def insertScriptsForUp(allScripts):
    tuple=[]
    now=datetime.datetime.now()
    lowDate=tM.getLowDate()
    for script in allScripts:
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
    insertScriptsForUp(filterdlist)

def createScript(fileName):
    rootPath=os.path.dirname(os.path.realpath(__file__))
    templatePath=os.path.join(rootPath,"internal_files")    
    tStamp=tM.getDate()
    fileName=fileName+"_"+tStamp+".txt"
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
    finally:
        if fp1 is not None:
            fp1.close()
        if fp is not None:
            fp.close()    




