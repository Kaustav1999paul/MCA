import pymysql

def createTable(c):
    sql="CREATE TABLE employee (emp_id varchar(20),emp_name varchar(100), emp_age integer,emp_salary float)"
    c.execute(sql)
    print("Successfully created")

def addMany(c,d):
    sql="INSERT INTO employee(emp_id,emp_name,emp_age,emp_salary) VALUES(%s,%s,%s,%s)"
    value=[('1','Kishan',22,20330455506.0),('3','Krupa',21,200110044.0),('2','Jay',22,20035033.0),('4','Indrabhushan',22,20005521.0)]
    c.executemany(sql,value)
    print("Added Successfully")
    d.commit()
    
def searchData(c,name):
    sql="SELECT * FROM employee WHERE emp_name = '%s' "%name
    c.execute(sql)
    print("Data Found")
    for row in c:
        print(row)

def displayData(c):
    sql="SELECT * FROM employee"
    c.execute(sql)
    for row in c:
        print(row)

def dropTable(c):
    c.execute("DROP TABLE employee")
    print("Table Deleted")

db = pymysql.connect(host="172.16.34.105", user="mca012", passwd= "mca012", database= "mca012")
cursor=db.cursor()
while True:
    print("Enter 1 to create table")
    print("Enter 2 to add data")
    print("Enter 3 to add many")
    print("Enter 4 to search data by name")
    print("Enter 5 to display all data")
    print("Enter 6 to delete table")
    print("Enter 7 to exit")
    ch =int(input("Enter your choice\n"))
    if ch==1:
        createTable(cursor)
    elif ch==3:
        addMany(cursor,db)
    elif ch==4:
        name=input("Enter the name to be searched\n")
        searchData(cursor,name)
    elif ch==5:
        displayData(cursor)
    elif ch==6:
        dropTable(cursor)
    elif ch==7:
        print("Exited")
        break
    else:
        print("Wrong value! please try again")
cursor.close()
db.close()