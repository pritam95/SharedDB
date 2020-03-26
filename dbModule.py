import mysql.connector
import constant

def insertScript(tuple):
    connection=None
    try:
        connection = mysql.connector.connect(host=constant.HOST,database=constant.DATABASE,user=constant.USER,password=constant.PASSWORD)
        cursor = connection.cursor(prepared=True) #this will return MySQLCursorPrepared object
        query = "INSERT INTO db_control (script_name,run_up_flag,up_runtime,run_down_flag,down_runtime) VALUES (%s,%s,%s,%s,%s)"
        cursor.executemany(query, tuple)
        connection.commit()
        print("From "+__name__+": inserScript method insertd succesfully")
    except Exception as e:
        print("Something is Wrong IN inserScript :"+str(e))
        raise
    finally:
        if (connection is not None and connection.is_connected()):
            closeConnection(cursor,connection)

def getAllScriptsFromDBForUp():
    allScripts=[]
    try:
        connection = mysql.connector.connect(host=constant.HOST,database=constant.DATABASE,user=constant.USER,password=constant.PASSWORD)
        cursor = connection.cursor(dictionary=True) #this will return MySQLCursorPrepared object
        query = "SELECT * FROM db_control d WHERE d.run_up_flag=1"
        cursor.execute(query)
        allScripts=cursor.fetchall()
    except Exception as e:
        print("Something is Wrong IN inserScript :"+str(e))
        raise
    finally:
        if (connection is not None and connection.is_connected()):
            closeConnection(cursor,connection)
    return allScripts

def closeConnection(cursor,connection):
    cursor.close()
    connection.close()
    print("MySQL connection is closed")

def createDictionary(cursor):
    list=[]
    columnNames=cursor.column_names
    noOfCol=len(columnNames)
    print("-----------------------")
    #print(cursor.fetchall())
    for result in cursor.fetchall():
        dict={}
        for i in range(0,noOfCol,1):
            dict[columnNames[i]]=result[i]
        list.append(dict)
    print(list)    
