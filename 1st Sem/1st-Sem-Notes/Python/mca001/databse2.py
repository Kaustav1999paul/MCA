import pymysql
class MyDatabase:
	def _init_(self):
		self.db=pymysql.connect(host="172.16.34.105", user="mca111", password="mca111", db="mca111")
		self.cur = self.db.cursor()
		self.cur.execute("CREATE TABLE IF NOT EXISTS Employee (EMPCODE INT, NAME VARCHAR(30), ADDRESS VARCHAR(50), DOB VARCHAR(50),MOBILE VARCHAR(13), STATUS VARCHAR(20), DESIGNATION VARCHAR(20), PRIMARY KEY(EMPCODE))")

	def insert(self):
		print("Enter Employee Details")
		empcode = int(input("Employee Code : "))
		name = input("Employee Name : ")
		add = input("Employee Address : ")
		dob = input("Date of Birth :")
		mobile = input("Contact : ")
		status = input("Status : ")
		desg = input("Designation : ") 

		query = ("INSERT INTO Employee (EMPCODE,NAME,ADDRESS,DOB,MOBILE,STATUS,DESIGNATION) VALUES(%s,%s,%s,%s,%s,%s,%s)")
		record = (empcode, name, add, dob, mobile, status, desg)
		self.cur.execute(query, record)
		self.db.commit()
	def display(self):
		print("SLNO\tEMPID\tNAME\tADDRESS\tDOB\tMOBILE\tSTATUS\tDESIGNATION")
		count=0
		self.cur.execute("SELECT * FROM Employee")
		for row in self.cur.fetchall():
			count =+ 1
			print(count,end="\t")
			print(f'{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}\t{row[6]}')

	def delete(self):
		delcode = int(input("Enter the Employee Code to delete : "))
		query = ("DELETE FROM Employee WHERE EMPCODE=%s")
		record = delcode
		self.cur.execute(query,record)
		self.db.commit()
print("----MENU----")
print("1. ADD EMPLOYEE RECORD")
print("2. DISPLAY ALL EMPLOYEES RECORD")
print("3. DELETE EMPLOYEE RECORD")
print("4. Exit")
mdb = MyDatabase()
while(True):
	try:
		ch = int(input("Enter your Choice : "))
		if ch == 1:
			mdb.insert()
		elif ch == 2:
			mdb.display()
		elif ch == 3:
			mdb.delete()
		elif ch == 4:
			break
		else:
			print("Invalid choice")
	except:
		print("Enter only the options given above")