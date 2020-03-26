import os
from tkinter import messagebox
import subEventModule as subEvt

def createScript(fileName):
    print("Inside:"+__name__)
    tempName=fileName.get()
    if tempName.find(' ') != -1:
        messagebox.showinfo("Error","Can not contain space in name")
        return
    subEvt.createScript(tempName)

def runUpward(fileName):
    scriptNames=[]
    try:
        scriptNames=subEvt.findScripts()
    except Exception as e:
        messagebox.showinfo("Error","runUpward Method:something is worng: "+str(e))
        return
    if len(scriptNames)>0:
        try:
            scriptNames=subEvt.sortScriptsWithTime(scriptNames)
        except Exception as e:
            messagebox.showinfo("Error","runUpward Method:something is worng: "+str(e))
            return
    else:
        messagebox.showinfo("Error","no scripts found on the specific directory,please check")
        return
    try:
        scriptsFromDb=subEvt.getAllScriptsForUp()
        print("All scripts from Database till executed are: "+str(scriptsFromDb))
        if(len(scriptsFromDb)>0):
            scriptsFromDb=subEvt.sortScriptsWithTime(scriptsFromDb)
        subEvt.runScripts(scriptNames,scriptsFromDb)        
    except Exception as e:
            messagebox.showinfo("Error","runUpward Method:something is worng: "+str(e))
            return

