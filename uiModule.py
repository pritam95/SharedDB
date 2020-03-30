import tkinter as tk
import eventModule as evnt

def rootUi(mainWindow):
    print ("Inside:"+__name__)
    fileName=tk.StringVar()
    createButton(mainWindow,"Create Script",fileName,evnt.createScript)
    createButton(mainWindow,"Run Upwards",fileName,evnt.runUpward)
    createLabel(mainWindow,"Enter File Name:")
    createEntry(mainWindow,fileName)

def createButton(mainWindow,purpose,fileName,action):
    newButton=tk.Button(mainWindow,text=purpose,command=lambda:action(fileName))
    newButton.pack()

def createLabel(mainWindow,purpose):
    newLabel=tk.Label(mainWindow,text=purpose)
    newLabel.pack()

def createEntry(mainWindow,varName):
    newEntry=tk.Entry(mainWindow,textvariable=varName)
    newEntry.pack()