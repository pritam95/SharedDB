import datetime

def getTimestamp(dtObject,timeZone):
    return (int(dtObject.replace(tzinfo=datetime.timezone.utc).timestamp()))

def getDate():
    now=datetime.datetime.now()
    print (str(now))
    unixTstamp=getTimestamp(now,"utc")
    print (str(unixTstamp))
    return (str(unixTstamp))

def getLowDate():
    lowDate='01/01/1980'
    lowDateObj=datetime.datetime.strptime(lowDate, '%d/%m/%Y')
    return lowDateObj  