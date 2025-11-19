import sqlite3

class DatabaseJoke:
    DB_FILE = "funny.db"

    def init_db(self):
        with sqlite3.connect(self.DB_FILE) as conn:
            c = conn.cursor()
            c.execute("""
            CREATE TABLE IF NOT EXISTS jokes(Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Joke_text TEXT, Data DATE DEFAULT (CURRENT_DATE))
            """)
            conn.commit()

    def save_to_db(self, jokes):
        with sqlite3.connect(self.DB_FILE, timeout=5) as conn:
            c  = conn.cursor()
            c.execute("INSERT INTO jokes (Joke_text) VALUES (?)",(jokes,))
            conn.commit()

