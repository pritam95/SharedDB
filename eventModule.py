from tkinter import messagebox
import other_modules.subEventModule as subEvt
import utility.common as common

def createScript(fileName):
    print("Inside:"+__name__)
    tempName=fileName.get()
    response=common.nameValidator(tempName)
    if response==False:
        return
    try:   
        subEvt.createScript(tempName)
    except Exception as e:
        return
    fileName.set("")

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
        messagebox.showinfo("Error","No scripts found on the specific directory,please check")
        return
    try:
        scriptsFromDb=subEvt.getAllScriptsForUp()
        print("All scripts from Database till executed in upward mode are: "+str(scriptsFromDb))
        if(len(scriptsFromDb)>0):
            scriptsFromDb=subEvt.sortScriptsWithTime(scriptsFromDb)
        subEvt.runScripts(scriptNames,scriptsFromDb)        
    except Exception as e:
            messagebox.showinfo("Error","runUpward Method:something is worng: "+str(e))
            return

