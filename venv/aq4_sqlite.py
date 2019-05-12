# Python code to demonstrate table creation and
# insertions with SQL

# importing module
import sqlite3

# connecting to the database
connection = sqlite3.connect("Emp.db")

# cursor
crsr = connection.cursor()



# SQL command to create a table in the database
sql_command = """CREATE TABLE emp ( 
                    EmpID INTEGER PRIMARY KEY, 
                    DeptName VARCHAR(20), 
                    Gross_Salary INTEGER);"""

# execute the statement
crsr.execute(sql_command)

# SQL command to insert the data in the table
sql_command = """INSERT INTO emp VALUES (1, "Quality Control", 10000);"""
crsr.execute(sql_command)

# another SQL command to insert the data in the table
sql_command = """INSERT INTO emp VALUES (2, "Finance", 20000);"""
crsr.execute(sql_command)

sql_command = """INSERT INTO emp VALUES (3, "Quality Control", 50000);"""
crsr.execute(sql_command)

# another SQL command to insert the data in the table
sql_command = """INSERT INTO emp VALUES (4, "Finance", 60000);"""
crsr.execute(sql_command)



# To save the changes in the files. Never skip this.
# If we skip this, nothing will be saved in the database.
connection.commit()


#Till here not requiired
# from here onwards answers the question


# connecting to the database
connection = sqlite3.connect("Emp.db")

# cursor
crsr = connection.cursor()

#sql command to find the sum of gross salary of employees working under Quality Control Department
sql_command = """SELECT sum(Gross_Salary) FROM emp where DeptName = "Quality Control"; """
crsr.execute(sql_command)

ans = crsr.fetchall()

# loop to print all the data
for i in ans:
	print(i)

# close the connection
connection.close()
