import mysql.connector
mydb=mysql.connector.connect(
host="localhost",
user="root",
password="root",
database="PYTHON_DATA"
)
mycursor=mydb.cursor()
#mycursor.execute("CREATE DATABASE PYTHON_DATA")
mycursor.execute("CREATE TABLE Person(Name VARCHAR(30),Age INTEGER,Address VARCHAR(50))")
#mycursor.execute("INSERT INTO Person(Name,Age,Address)VALUES('DIKSHA',28,'KOCHI')")
#mydb.commit()
#sql="INSERT INTO Person(Name,Age,Address)VALUES(%s,%s,%s)"
#val=[("suraj",30,"shimla"),("sonu",22,"jaipur"),("seema",26,"pune"),("meenu",29,"kolkata"),("bhupi",28,"ernakulam")]
#mycursor.executemany(sql,val)
mydb.commit()