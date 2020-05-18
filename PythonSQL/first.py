import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
   database="PYTHON_sql1"
)
mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE PYTHON_sql1")
#mycursor.execute("SHOW DATABASES")
#for x in mycursor:
 # print(x)
#mycursor.execute("CREATE TABLE STUDENT_DATA(Name VARCHAR(30),Age INTEGER,Id INTEGER)")
#mycursor.execute("INSERT INTO STUDENT_DATA(Name,Age,Id)VALUES('DIKSHA',28,123)")
#mydb.commit()
#sql="INSERT INTO STUDENT_DATA(Name,Age,Id)VALUES(%s,%s,%s)"
#val=[("anju",25,3789),("steffy",25,9087),("sruthi",23,4532)]
#mycursor.executemany(sql,val)
mycursor.execute("SELECT * FROM STUDENT_DATA")
CUR=mycursor.fetchall()
for i in CUR:
    print(i)