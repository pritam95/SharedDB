import os
import timeModule as tm
import constant
from tkinter import messagebox
import subEventModule as subEvt

def createScript(fileName):
    print("Inside:"+__name__)
    tStamp=tm.getDate()
    tempName=fileName.get()
    if tempName.find(' ') != -1:
        messagebox.showinfo("Error","Can not contain space in name")
        return
    fileName=tempName+"_"+tStamp+".txt"
    fp=None
    try:
        fp=open((os.path.join(constant.PATH,fileName)),'a+')
        print("File Created With Name : "+fileName)
        fp.write("Test Data")
    except Exception as e:
        messagebox.showinfo("Error","Can not create file on specific path: "+str(e))
    finally:
        if fp is not None:
            fp.close()

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

