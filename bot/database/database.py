import sqlite3

class Database:
    def __init__(self):
        self.db = sqlite3.connect("database.db")
        self.cur = self.db.cursor()
        self.table_name = "users"

    def initTable(self):
        q = """
        CREATE TABLE IF NOT EXISTS %s (
            id INTEGER PRIMARY KEY NOT NULL,
            name VARCHAR(60),
        )
        """
        self.cur.execute(q.format(self.table_name))
        self.db.commit()

    def insert(self, id: int):
        q = """
        INSERT INTO %s VALUES (
            %d, %s
        )
        """
        self.cur.execute(q.format(self.table_name, id))
        self.db.commit()

    def fetchAll(self):
        return self.cur.execute("SELECT * FROM %s" % self.table_name).fetchall()

    
        
db = Database()