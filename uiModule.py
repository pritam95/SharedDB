import tkinter as tk
import eventModule as evnt

def rootUi(mainWindow):
    print ("Inside:"+__name__)
    fileName=tk.StringVar()
    createButton(mainWindow,"First",fileName)
    createLabel(mainWindow,"Enter File Name")
    createEntry(mainWindow,fileName)


def createButton(mainWindow,purpose,fileName):
    newButton=tk.Button(mainWindow,text=purpose,command=lambda:evnt.createScript(fileName))
    newButton.pack()

def createLabel(mainWindow,purpose):
    newLabel=tk.Label(mainWindow,text=purpose)
    newLabel.pack()

def createEntry(mainWindow,varName):
    newEntry=tk.Entry(mainWindow,textvariable=varName)
    newEntry.pack()