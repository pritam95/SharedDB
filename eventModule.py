import os
import datetime
import timeModule as tm
from tkinter import messagebox

def createScript(fileName):
    print("Inside:"+__name__)
    tStamp=tm.getDate()
    tempName=fileName.get()
    if tempName.find(' ') != -1:
        messagebox.showinfo("Error","Can not contain space in name")
        return
    path="/home/pritam/Desktop"
    fileName=tempName+"_"+tStamp+".txt"
    fp=open((os.path.join(path,fileName)),'a+')
    print("File Created With Name : "+fileName)
    fp.write("Test Data")
    fp.close()

def runUpward(fileName):
    scriptNames=findScripts()
    scriptNames=sortScriptsWithTime(scriptNames)

def findScripts():
    scriptNames=[]
    for script in os.listdir("/home/pritam/Desktop"):
        if script.endswith(".txt"):
            scriptNames.append(script)
    print ("Files with proper extensions:"+str(scriptNames))
    return scriptNames

def sortScriptsWithTime(scriptNames):
    temp=[]
    for script in scriptNames:
        startIndex=script.find('_')
        endIndex=script.find('.')
        temp.append(script[(startIndex+1):(endIndex)]) #taking only timestamp and making a list
    n=len(temp)
    for i in range(0,n,1):
        for k in range(0,n-i-1,1):
            if temp[k]>temp[k+1]:
                tem=temp[k]
                temf=scriptNames[k]
                temp[k]=temp[k+1]
                scriptNames[k]=scriptNames[k+1]
                temp[k+1]=tem
                scriptNames[k+1]=temf
    print("After sorting the order is:"+str(scriptNames))
    return scriptNames
