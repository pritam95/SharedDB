import os
import datetime
import timeModule as tm

def createScript(fileName):
    print("Inside:"+__name__)
    tStamp=tm.getDate()
    tempName=fileName.get()
    print(tempName)
    path="/home/pritam/Desktop"
    fileName=tempName+"_"+tStamp+".txt"
    fp=open((os.path.join(path,fileName)),'a+')
    print("File Created With Name : "+fileName)
    fp.write("Test Data")
    fp.close()
