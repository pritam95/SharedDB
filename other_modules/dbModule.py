import mysql.connector
import utility.constant as constant

def insertScript(dbInput):
    connection=None
    connection=dbInput['connection']
    tuple=dbInput['obj']
    try:
        cursor = connection.cursor(prepared=True) #this will return MySQLCursorPrepared object
        query = "INSERT INTO db_control (script_name,run_up_flag,up_runtime,run_down_flag,down_runtime) VALUES (%s,%s,%s,%s,%s)"
        cursor.executemany(query, tuple)
        print("From "+__name__+": inserScript method insertd succesfully")
    except Exception as e:
        print("Something is wrong :"+str(e))
        raise
    finally:
        if (connection is not None and connection.is_connected()):
            cursor.close()

def getAllScriptsFromDBForUp():
    allScripts=[]
    connection=None
    try:
        connection = mysql.connector.connect(host=constant.HOST,database=constant.DATABASE,user=constant.USER,password=constant.PASSWORD)
        cursor = connection.cursor(dictionary=True) 
        query = "SELECT * FROM db_control d WHERE d.run_up_flag=1"
        cursor.execute(query)
        allScripts=cursor.fetchall()
    except Exception as e:
        print("Something is wrong  :"+str(e))
        raise
    finally:
        if (connection is not None and connection.is_connected()):
            closeConnection(cursor,connection)
    return allScripts

def runQuery(dbInput):
    connection=None
    connection=dbInput['connection']
    query=dbInput['obj']
    try:
        cursor = connection.cursor()
        cursor.execute(query)
    except Exception as e:
        print("Something is Wrong :"+str(e))
        raise
    finally:
        if (connection is not None and connection.is_connected()):
            cursor.close()    

def checkDBSetup():
    allTables=[]
    connection=None
    try:
        connection = mysql.connector.connect(host=constant.HOST,database=constant.DATABASE,user=constant.USER,password=constant.PASSWORD)
        cursor = connection.cursor(dictionary=True) 
        query = "SHOW TABLES"
        cursor.execute(query)
        allTables=cursor.fetchall()
    except Exception as e:
        print("Something is wrong :"+str(e))
        raise
    finally:
        if (connection is not None and connection.is_connected()):
            cursor.close()
    return allTables

def createInternalDB():
    connection=None
    try:
        connection = mysql.connector.connect(host=constant.HOST,database=constant.DATABASE,user=constant.USER,password=constant.PASSWORD)
        cursor = connection.cursor()
        query="""CREATE TABLE db_control(
            id INT(11) AUTO_INCREMENT PRIMARY KEY,
            script_name VARCHAR(128) NOT NULL,
            run_up_flag INT(1) NOT NULL,
            up_runtime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            run_down_flag INT(1) NOT NULL,
            down_runtime TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"""
        cursor.execute(query)
        connection.commit()
    except Exception as e:
        print("Something is wrong  :"+str(e))
        raise
    finally:
        if (connection is not None and connection.is_connected()):
            closeConnection(cursor,connection)    

def openConnection():
    connection=None
    try:
        connection=mysql.connector.connect(host=constant.HOST,database=constant.DATABASE,user=constant.USER,password=constant.PASSWORD)
        return connection
    except Exception as e:
        print("Can not open DB connection")
        raise e

def commitAndCloseConnection(connection):
    if (connection is not None and connection.is_connected()):
        connection.commit()
        connection.close()
        print("MySQL connection commited and closed")
def closeConnection(cursor,connection):
    cursor.close()
    connection.close()
    print("MySQL connection is closed")

   
