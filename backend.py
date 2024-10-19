import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",password="Dev@2512",database="employee")
c= mydb.cursor()
login = False
Eid = input("Enter employee id: ")
pwd = input("Enter Password: ")
c.execute("select * from pro_info")
for row in c:
	if (Eid == row[0] and pwd == row[1]):
		login = True
		break
if (login):
	print("Login Successful")
else:
	print("Login Unsuccessful")