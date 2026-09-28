

import mysql.connector

class BookListCreateRetrieveUpdateDelete:

    def __init__(self):
        self.connection=mysql.connector.connect(user="root",password="root",host="localhost",database="blood_db")
        self.cursor=self.connection.cursor()
        print('Successfully connected to MySQL database')
    def list(self):
        query="select * from doner"
        self.cursor.execute(query)
        record=self.cursor.fetchall()
        if record:
            # for i in record:
            #     print(i)
            return record
        else:
            print("No found")

    def create(self ,name,blood_group,phone,city,last_donation):

        query="insert into doner(name,blood_group,phone,city,last_donation) values(%s,%s,%s,%s,%s)"

        data=(name,blood_group,phone,city,last_donation)
        self.cursor.execute(query,data)
        self.connection.commit()



        print('Data Inserted Successfully')
    #
    def retrieve(self,id):
        #for reading a specific record
        query="select * from doner where id=%s"
        data=(id,)
        self.cursor.execute(query,data)
        record=self.cursor.fetchone()
        self.close()
        if record:
            return record
            # for i in record:
            #     print(i)

        else:
            print("No data found")



    #
    # def update(self,id,name,blood_group,phone,city,last_donation):
    #     query='update doner set name=%s,blood_group=%s,phone=%s,city=%s,last_donation=%s where id=%s'
    #     data=(name,blood_group,phone,city,last_donation,id)
    #     self.cursor.execute(query,data)
    #     self.connection.commit()
    #     if self.cursor.rowcount>0:
    #     # print('Data Updated Successfully')
    #         return True
    #     else:
    #         return False
    def close(self):
        self.cursor.close()
        self.connection.close()
    #
    # def delete(self,id):
    #     query="delete from book where id=%s"
    #     data=(id,)
    #     self.cursor.execute(query,data)
    #     self.connection.commit()
    #     if self.cursor.rowcount>0:
    #         # print('Data Deleted Successfully')
    #         return True
    #     else:
    #         # print("No book found")
    #         return False

book_instance=BookListCreateRetrieveUpdateDelete()
# book_instance.list()
# book_instance.create('DEF','Jacob',1450,450,'Telugu')
# book_instance.retrieve()
# book_instance.update(id=2,title='PQR',author='Jabala',price=100,pages=50,language='konkini')
# book_instance.delete()


