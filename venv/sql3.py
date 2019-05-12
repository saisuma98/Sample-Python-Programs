import sqlite3


connection = sqlite3.connect("Emp.db")

cursor = connection.cursor()

sqlCmd = "Drop TABLE emp;"



try:
    cursor.execute(sqlCmd)

except :
    print("Error")
finally:
    connection.close()