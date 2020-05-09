import tkinter as tk
import eventModule as evnt

class RootUi():
    "UI Module creation for application"
    outputText=""
    def __init__(self,mainWindow):
        self.mainWindow=mainWindow
        self.mainFrame=tk.LabelFrame(self.mainWindow)
        self.scriptEntryContent=tk.StringVar()
        self.scriptEntryLabel=tk.Label(self.mainFrame,text="Enter Script Name:")
        self.scriptEntry=tk.Entry(self.mainFrame,textvariable=self.scriptEntryContent)
        self.scriptCreateButton=tk.Button(self.mainFrame,text="Create Script",command=lambda:evnt.createScript(self.scriptEntryContent))
        self.setupButton=tk.Button(self.mainFrame,text="Run Setup",command=lambda:evnt.setUp())
        self.runUpwardButton=tk.Button(self.mainFrame,text="Run Upward",command=lambda:evnt.runUpward())
        RootUi.outputText=tk.Text(self.mainFrame)
        self.outputTextScrollBar=tk.Scrollbar(self.mainFrame, command=RootUi.outputText.yview,orient=tk.VERTICAL)
        RootUi.outputText.insert(tk.END,"SharedDB Runing......\n")
        self.clearHistoryButton=tk.Button(self.mainFrame,text="Clear History",command=lambda:RootUi.clearHistory())
        self.setWidgets()

    def setWidgets(self):
        self.mainFrame.pack(expand="yes",padx=7,pady=7)
        self.mainFrame.configure(padx=5,pady=5)
        self.scriptEntryLabel.grid(row=0,column=0,padx=2,pady=2)
        self.scriptEntry.grid(row=0,column=1,padx=1,pady=1)
        self.scriptCreateButton.grid(row=0,column=2,padx=2,pady=2)
        self.scriptCreateButton.configure(height=1,width=10)
        self.setupButton.grid(row=1,column=2,padx=2,pady=2)
        self.setupButton.configure(height=1,width=10)        
        self.runUpwardButton.grid(row=2,column=2,padx=2,pady=2)
        self.runUpwardButton.configure(height=1,width=10)
        RootUi.outputText.grid(row=1,column=0,padx=2,pady=2,rowspan=4,columnspan=2)
        RootUi.outputText.configure(height=7,width=40,yscrollcommand=self.outputTextScrollBar.set,state='disabled')
        self.outputTextScrollBar.grid(row=1,column=1,sticky=tk.N+tk.S+tk.E,rowspan=4,padx=2,pady=2)
        self.clearHistoryButton.grid(row=3,column=2,padx=2,pady=2)
        self.clearHistoryButton.configure(height=1,width=10)

    @staticmethod
    def printStatus(msg):
        RootUi.outputText.configure(state='normal')
        RootUi.outputText.insert(1.0,"\n")
        RootUi.outputText.insert(1.0,msg)
        RootUi.outputText.configure(state='disabled')

    @staticmethod
    def clearHistory():
        RootUi.outputText.configure(state='normal')
        RootUi.outputText.delete(1.0, tk.END)
        RootUi.outputText.configure(state='disabled')
