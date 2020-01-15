import mysql.connector

cnx = mysql.connector.connect(user='root', password='',
                              host='192.168.88.203',
                              database='ruslan')

query = ("SELECT * FROM test")
cursor = cnx.cursor()
cursor.execute(query)
record = cursor.fetchall()

print(record)

cnx.close()