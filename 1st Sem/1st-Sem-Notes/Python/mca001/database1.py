import pymysql
class employee:
	def _init_(self):
		self.db=pymysql.connect(host="localhost",user="root",passwd="Tanuj1509@gmail",db="emp")
		self.cur=self.db.cursor()
		self.cur.execute("CREATE TABLE IF NOT EXISTS emp(EMPCODE INT,NAME VARCHAR(30),STATUS VARCHAR(20),DOB VARCHAR(20),PRIMARY KEY(EMPCODE))")
	def insert(self):
		print("Insert into database")
		empcode=int(input("enter the employee code : "))
		name=input("enter the name : ")
		status=input("enter the designation : ")
		dob=input("enter the date of birthd : ")
		query=("INSERT INTO emp (EMPCODE,NAME,STATUS,DOB)VALUES(%s,%s,%s,%s)")
		record=(empcode,name,status,dob)
		self.cur.execute(query,record)
		self.db.commit()
	def display(self):
		print("DISPLAY employee ")
		self.cur.execute("SELECT * FROM emp")
		for row in self.cur.fetchall():
			print(row[0])
			print(row[1])
			print(row[2])
			print(row[3])
			print("")
	def delete(self):
		delcode=int(input("enter the empcode : "))
		query=("DELETE FROM emp WHERE EMPCODE=%s")
		self.cur.execute(query,delcode)
		self.db.commit()
print("1.employee insert")
print("2.display")
print("3.delete")
em=employee()
while True:
	ch=int(input("enter the choice : "))
	if ch==1:
		em.insert()
	elif ch==2:
		em.display()
	elif ch==3:
		em.delete()
	else:
		quit()