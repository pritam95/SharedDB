import mysql.connector
import utility.constant as constant

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

def runQuery(query):
    try:
        connection = mysql.connector.connect(host=constant.HOST,database=constant.DATABASE,user=constant.USER,password=constant.PASSWORD)
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
    except Exception as e:
        print("Something is Wrong IN Query :"+str(e))
        raise
    finally:
        if (connection is not None and connection.is_connected()):
            closeConnection(cursor,connection)    

def closeConnection(cursor,connection):
    cursor.close()
    connection.close()
    print("MySQL connection is closed")

   