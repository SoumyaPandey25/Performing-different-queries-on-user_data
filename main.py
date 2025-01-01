import mysql.connector
if __name__ == '__main__':
    mycon=mysql.connector.connect(
        user="root",
        password="root",
        database="demo",
        host="localhost"
    )

    print(mycon)
cursor = mycon.cursor()
def show():

    query = "select * from user_data"
    cursor.execute(query)

    results = cursor.fetchall()  # fetches all the data from the cursor
    for i in results:
        print("USER ID:", i[0])
        print("User Name:", i[1])
        print("User Phone:", i[2])
        print("User Email:",i[3])
        print("----------------------------------------------------------------------------------------------------------------------")
    main()


def add_user():
    a=int(input("Enter User Id:"))
    b=input("Enter User Name:")
    c=int(input("Enter User Phone_number:"))
    d=input("Enter User Email_id:")
    data=(a,b,c,d)
    q="INSERT INTO user_data(user_id , user_name , phone , email ) values (%s,%s,%s,%s)"
    cursor=mycon.cursor()
    cursor.execute(q,data)
    mycon.commit()
    print("---------------------------------------------------------------------------------------------------------------------------------------")
    print("Data Entered Successfully")

    main()
    
def del_user():
    u_id= int(input("Enter User ID: "))
    data = (u_id,)
    sql = "DELETE FROM user_data WHERE user_id = %s"
    cursor = mycon.cursor()
    cursor.execute(sql,data)
    mycon.commit()
    print("User deleted successfully")

    main()

def update_user():
    r = int(input("Enter user_id:"))
    print("-----------------------------------------------------------------------------------------------")
    print("1. Name")
    print("2. Phone")
    print("3. Email")
    
    x = int(input("What do you want to update?:"))

    if x==1:
        q1= "UPDATE user_data SET user_name =%s WHERE user_id=%s"
        cursor.execute(q1, (input("Enter New Name :"), r,))

    elif x==2:
        q2="UPDATE user_data SET phone = %s WHERE user_id = %s"
        cursor.execute(q2, (input("Enter New Phone_Number :"), r,))

    else:
        q3="UPDATE user_data SET email =%s WHERE user_id = %s"
        cursor.execute(q3, (input("Enter New Email :"), r,))

    sql="select * from user_data"
    cursor.execute(sql)
    result=cursor.fetchall()
    for i in result:
        print(i)
    main()

def main():
    print("*******************************************************************************************")
    print("Choose your option:")
    print("1. Show Data")
    print("2. Insert Data")
    print("3. Delete Data")
    print("4. Update Data")
    print("5. EXIT")
    print("*******************************************************************************************")
    x=int(input("Enter your choice:"))
    if x==1:
        show()
    elif x==2:
        add_user()
    elif x == 3:
        del_user()
    elif x == 4:
        update_user()
    else:
        print("OK! Data Processing successfully done.")

main()



