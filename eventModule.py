from tkinter import messagebox
import other_modules.subEventModule as subEvt
import utility.common as common
import uiModule as ui

def createScript(fileName):
    print("Inside:"+__name__)
    ui.RootUi.printStatus("Creating new script.......")
    tempName=fileName.get()
    response=common.nameValidator(tempName)
    if response==False:
        return
    try:   
        subEvt.createScript(tempName)
    except Exception as e:
        ui.RootUi.printStatus("Script creation failed......")
        return
    fileName.set("")
    ui.RootUi.printStatus("Script creation complete.......")

def runUpward():
    ui.RootUi.printStatus("Running scripts started........")
    scriptNames=[]
    try:
        scriptNames=subEvt.findScripts()
    except Exception as e:
        ui.RootUi.printStatus("Running scripts failed........")
        return
    if len(scriptNames)>0:
        try:
            scriptNames=subEvt.sortScriptsWithTime(scriptNames)
        except Exception as e:
            ui.RootUi.printStatus("Running scripts failed........")
            raise
    else:
        ui.RootUi.printStatus("No scripts found on the specific directory,please check")
        return
    try:
        scriptsFromDb=subEvt.getAllScriptsForUp()
        if(len(scriptsFromDb)>0):
            scriptsFromDb=subEvt.sortScriptsWithTime(scriptsFromDb)
        subEvt.runScripts(scriptNames,scriptsFromDb)        
    except Exception as e:
            ui.RootUi.printStatus("Running scripts failed........")
            return
    ui.RootUi.printStatus("Running scripts completed........")

def setUp():
    try:
        ui.RootUi.printStatus("Strarting setup.......")
        subEvt.checkSetup()
        ui.RootUi.printStatus("Setup completed.......")
    except Exception as e:
        ui.RootUi.printStatus("Setup failed......")
        return

