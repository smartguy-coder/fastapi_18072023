import sqlite3


class StorageSQLite:
    def __init__(self, database_name: str):
        self.database_name = database_name
        with sqlite3.connect(database_name) as connection:
            cursor = connection.cursor()
            query = """
                CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    author TEXT NOT NULL,
                    description TEXT,
                    price REAL NOT NULL,
                    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
            )"""
            cursor.execute(query)
            connection.commit()

    def get_books(self, limit: int = 10):

        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            query = """
                SELECT *
                FROM books
                ORDER BY id
                LIMIT :Limit_last
            """
            result = cursor.execute(query, {'Limit_last': limit})
            return result.fetchall()


    def get_book_by_title(self):
        pass

    def add_book(self, *, title: str, author: str, description: str, price: float):
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            query = """
                INSERT INTO books (title, author, description, price)
                VALUES (?,?,?,?)
            """
            cursor.execute(query, (title, author, description, price))
            connection.commit()


database = StorageSQLite('database.sqlite3')
