
# Python with Mysql database  Connection insert,select & update  31.03.2022
import mysql.connector
try:
        connection = mysql.connector.connect(host='172.16.34.105',database='mca001',user='mca001',password='mca001',auth_plugin='mysql_native_password')
        cursor = connection.cursor()

#Record  Inserting....."
        query1="insert into Staff(sapid,name) values ('100000','santhosh')"
        cursor.execute(query1)
#       connection.commit()
        print(cursor.rowcount, "Record inserted successfully into staff table")

#Record Listing......."
        query2="select * from Staff";
        cursor.execute(query2);
        myresult = cursor.fetchall()
        print(myresult)

#Record Updating......"
        query3="update Staff set sapid='5000' where name='Ganesh'"
        cursor.execute(query3);
        connection.commit()
        cursor.close()

except mysql.connector.Error as error:
        print("Failed to insert record into Staff table {}".format(error))

finally:
        if connection.is_connected():
                connection.close()
        print("MySQL connection is closed")



