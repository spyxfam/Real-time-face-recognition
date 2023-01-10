import mysql.connector
conn=mysql.connector.connect(host="127.0.0.1",username="root",pasword="Akshatha17*",database="facerecognitions")
my_cursor=conn.cursor()
conn.commit()
conn.close()
print("connection sucessfull")