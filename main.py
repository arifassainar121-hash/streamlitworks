import mysql.connector
#
# con=mysql.connector.connect(user='root',password='root',host='localhost')
# # # print(con)
# #
# # c=con.cursor()
# #
# c.execute('create database schooldb')
# print('database file created')

# #
# con=mysql.connector.connect(user='root',password='root',host='localhost',database='schooldb')
# c=con.cursor()

# c.execute('''
# create table student(rollno int not null primary key,
#                      name varchar(30),
#                      age int,
#                      place varchar(30),
#                       phone varchar(30),
#                      total_mark int)''')

# print('table created successfully')
#



# c.execute('''
#     INSERT INTO student (rollno, name, age, place, phone, total_mark)
#     VALUES (101, 'arun', 11, 'ekm', '983', 145),
#            (102, 'amal', 12, 'ekm', '7878', 140),
#            (103, 'anu', 11, 'tvm', '77', 147),
#            (104, 'hari', 12, 'tcr', '87', 144),
#            (105, 'manu', 11, 'ekm', '989', 141)
# ''')
#
# con.commit()
# print('Data inserted successfully')
# query='INSERT INTO student (rollno, name, age, place, phone, total_mark)values(%s,%s,%s,%s,%s,%s)'
#
# data=110,'siva',12,'ekm',374,123
# c.execute(query,data)
# con.commit()
# print('data insert')
#
# c.close()
# con.close()

#read operation

# query='select * from student'
# c.execute(query)
# records=c.fetchall()
# if records:
#     for raw in records:
#         print(raw)
#     else:
#         print(' no records')

        #read all attribute of student with roll number =roll nimber entered by user


# number=int(input('enter roll  number: '))
# query='select * from student where rollno=%s'
# data=(number,)
# c.execute(query,data)
# record=c.fetchone()
# if record:
#     print(record)
# else:
#     print('no records')

#update mark a student with roll number =roll number entered by user
# number=int(input('enter the roll number'))
# mark= int(input('enter new mark'))
# query='update student set total_mark=%s where rollno=%s '
# data=(mark,number)
# c.execute(query,data)
# con.commit()
# print('updated')
