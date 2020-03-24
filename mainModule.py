import tkinter as tk
import uiModule as ui

if __name__ == '__main__':
    rootWindow=tk.Tk()
    print ("Root Window Created:"+__name__)
    rootWindow.title("SharedDB")
    ui.rootUi(rootWindow)
    rootWindow.mainloop()
