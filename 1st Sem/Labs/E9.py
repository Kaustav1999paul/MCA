import pymysql
db = pymysql.connect(host='172.16.34.105',user='mca001',passwd='mca001',database='mca001')
cur = db.cursor()

class MyDatabase:

	def display(self):
		cur.execute("Show databases")
		for db in cur:
			print(db)

	def create(self):
		cur.execute("Create table emp(name varchar(20),slno int(20),address varchar(20)")
		print("Table has been created")

	def showtable(self):
		print("The table created is : ")
		cur.execute("Describe table emp")
		cur.execute("Show tables")
		for self.tb in cur:
			print(self.tb)

	def insert(self):
		self.sqlform = "Insert into emp(name,slno,address) values(%s,%s,%s)"
		self.employee = [("kaustav",101,"bangalore")]
		cur.executemany(self.sqlform, self.employee)
		db.commit()
		print("Values have been inserted")

	def displaytable(self):
		print("Contents that are in the table are")
		cur.execute("Select * from emp")
		self.result = cur.fetchall()
		for self.row in self.result:
			print(self.row)

	def delete(self,slno):
		self.sql = "Delete from emp where slno = '%s'"%(int(slno))
		cur.execute(self.sql)
		db.commit()
		print("Record has been deleted")

	def droptable(self):
		self.delt = "Drop table emp"
		cur.execute(self.delt)
		db.commit()
		print("Table has been dropped")

# Object creation
data = MyDatabase()

# Menu OPTIONS
while True:
    print("\n1.DISPLAY DATABASE \n2.CREATE TABLE \n3.DISPLAY TABLE AND STRUCTURE \n4.INSERT VALUES \n5.DISPLAY ALL TABLE CONTENTS \n6.DELETE A RECORD \n7.DROP THE TABLE \n8.EXIT \n\n")
    ch = int(input("Enter your choice : "))
    if ch==1:
        print("------------------------------------------------------------------------------------")
        data.display()
        print("------------------------------------------------------------------------------------")
    elif ch==2:
        print("------------------------------------------------------------------------------------")
        data.create()
        print("------------------------------------------------------------------------------------")
    elif ch==3:
        print("------------------------------------------------------------------------------------")
        data.showtable()
        print("------------------------------------------------------------------------------------")
    elif ch==4:
        print("------------------------------------------------------------------------------------")
        data.insert()
        print("------------------------------------------------------------------------------------")
    elif ch==5:
        print("------------------------------------------------------------------------------------")
        data.displaytable()
        print("------------------------------------------------------------------------------------")
    elif ch==6:
        print("------------------------------------------------------------------------------------")
        sl = int(input("Enter the serial no. that to be deleted from DB : "))
        data.delete(sl)
        print("------------------------------------------------------------------------------------")
    elif ch==7:
        print("------------------------------------------------------------------------------------")
        data.droptable()
        print("------------------------------------------------------------------------------------")
    elif ch==8:
        print("------------------------------------------------------------------------------------")
        exit()
        print("------------------------------------------------------------------------------------")
    else:
        print("------------------------------------------------------------------------------------")
        print("That is a wrong choice")
        print("------------------------------------------------------------------------------------")
        break





