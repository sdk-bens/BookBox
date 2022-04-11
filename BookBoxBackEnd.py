import sqlite3

class Database:


    def __init__(self, db):
        cnx = sqlite3.connect(db)
        cur = cnx.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY,title text, author text, year integer, isbn integer)")
        cnx.commit()
        cnx.close()

    # A function for inserting a row in the table
    def insert(title, author, year, isbn):
        cnx = sqlite3.connect("books.db")
        cur = cnx.cursor()
        cur.execute("INSERT INTO book VALUES (NULL, ?,?,?,?)", (title, author, year, isbn))
        cnx.commit()
        cnx.close()

    # A function for displaying a book details
    def view(self):
        cnx = sqlite3.connect("books.db")
        cur = cnx.cursor()
        cur.execute("SELECT * FROM book")
        rows = cur.fetchall()
        cnx.close()
        return rows

    # we pass empty string to the parameters as a default value to avoid error when calling the function with only one or two paramters

    # a function for searching for a book in the database
    def search(self, title="", author="", year="", isbn=""):
        cnx = sqlite3.connect("books.db")
        cur = cnx.cursor()
        cur.execute("SELECT * FROM book WHERE title = ? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
        rows = cur.fetchall()
        cnx.close()
        return rows

    # A function for deleting a book from the database
    def delete(self, id):
        cnx = sqlite3.connect("books.db")
        cur = cnx.cursor()
        cur.execute("DELETE FROM book WHERE id = ?", (id,))
        cnx.commit()
        cnx.close()

    # A function for updating a book
    def update(self, _id, title, author, year, isbn):
        cnx = sqlite3.connect("books.db")
        cur = cnx.cursor()

        # id should be at the end of the tuple in order to match the row
        cur.execute("UPDATE book SET title= ?, author = ?,  year = ?, isbn = ?  WHERE id= ?",
                    (title, author, year, isbn, _id))
        cnx.commit()
        cnx.close()


