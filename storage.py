import sqlite3


class Storage:
    def __init__(self, database_name: str):
        self.database_name = database_name
        with sqlite3.connect(database_name) as connection:
            cursor = connection.cursor()
            query = """
                CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    author TEXT NOT NULL
            """
            cursor.execute(query)
            connection.commit()

    def get_first_ten_newest(self):
        return

    def get_book_by_title(self):
        pass

    def add_book(self):
        pass


database = Storage('database.sqlite3')
