from operator import truediv

import mysql.connector

class BookListCreateRetrieveUpdateDelete:

    def _init_(self):
        self.connection=mysql.connector.connect(user="root",password="root",host="localhost",database="library_db")
        self.cursor=self.connection.cursor()
        print('Successfully connected to MySQL database')
    def list(self):
        query="select * from book"
        self.cursor.execute(query)
        record=self.cursor.fetchall()
        if record:
            # for i in record:
            #     print(i)
            return record
        else:
            print("No books found")

    def create(self,title,author,price,pages,language):

        query="insert into book(title,author,price,pages,language) values(%s,%s,%s,%s,%s)"

        data=(title,author,price,pages,language)
        self.cursor.execute(query,data)
        self.connection.commit()
        print('Data Inserted Successfully')

    def retrieve(self,id):
        #for reading a specific record
        query="select * from book where id=%s"
        data=(id,)
        self.cursor.execute(query,data)
        record=self.cursor.fetchone()
        if record:
            for i in record:
                print(i)

        else:
            print("No book found")

    def update(self,id,title,author,price,pages,language):
        query='update book set title=%s,author=%s,price=%s,pages=%s,language=%s where id=%s'
        data=(title,author,price,pages,language,id)
        self.cursor.execute(query,data)
        self.connection.commit()
        if self.cursor.rowcount>0:
        # print('Data Updated Successfully')
            return True
        else:
            return False


    def delete(self,id):
        query="delete from book where id=%s"
        data=(id,)
        self.cursor.execute(query,data)
        self.connection.commit()
        if self.cursor.rowcount>0:
            # print('Data Deleted Successfully')
            return True
        else:
            # print("No book found")
            return False

book_instance=BookListCreateRetrieveUpdateDelete()
# book_instance.list()
# book_instance.create('DEF','Jacob',1450,450,'Telugu')
# book_instance.retrieve()
# book_instance.update(id=2,title='PQR',author='Jabala',price=100,pages=50,language='konkini')
# book_instance.delete()


