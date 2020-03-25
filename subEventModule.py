import os
import constant
from tkinter import messagebox

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
