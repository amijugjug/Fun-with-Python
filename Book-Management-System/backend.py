import sqlite3

class Database:
    def __init__(self,db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY, title text,author text,year INTEGER,isbn INTEGER)")
        self.con.commit()

    def insert(self,title,author,year,isbn):
        self.cur.execute("INSERT INTO books VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
        self.con.commit()

    def view(self):
        self.cur.execute("SELECT * FROM books")
        rows = self.cur.fetchall()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM books WHERE id = ?",(id,))
        self.con.commit()

    def update(self,id,title,author,year,isbn):
        self.cur.execute("UPDATE books SET title = ?,author = ?, year = ?,isbn = ? WHERE id = ?",(title,author,year,isbn,id))
        self.con.commit()

    def search(self,title="",author="",year="",isbn=""):
        self.cur.execute("SELECT * FROM books WHERE title = ? OR author = ? OR year = ? OR isbn = ?",(title,author,year,isbn))
        rows = self.cur.fetchall()
        return rows

    def __del__(self): #Desturcter in python
        self.con.close()