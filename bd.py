import sqlite3

def manipulation(dataBase, command):
    connection = sqlite3.connect(dataBase)
    cursor = connection.cursor()
    cursor.execute(command)
    connection.commit()
    connection.close()

def selectData(dataBase, command):
    connection = sqlite3.connect(dataBase)
    cursor = connection.cursor()
    cursor.execute(command)
    lines = cursor.fetchall()

    for line in lines:
        print(line) 

def dataManipulation():
    commandInsert = "INSERT INTO estados (nome_estado, sigla_estado, nome_capital) VALUES('Pernambuco', 'PE', 'Recife')"        
    pathDb = ''
    commandSelect = "SELECT nome_estado, sigla_estado, nome_capital FROM estados"
    manipulation(pathDb, commandInsert)
    selectData(pathDb, commandSelect)


dataManipulation()    