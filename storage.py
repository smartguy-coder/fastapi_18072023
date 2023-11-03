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
                    cover TEXT NOT NULL,
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
                ORDER BY id DESC
                LIMIT :Limit_last
            """
            result = cursor.execute(query, {'Limit_last': limit})
            return result.fetchall()


    def get_book_by_title_or_other_str(self, query_str: str):
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            query = """
                SELECT *
                FROM books
                WHERE 
                    title LIKE :query_str 
                OR 
                    author LIKE :query_str
                OR
                    description LIKE :query_str
                ORDER BY id DESC
            """
            result = cursor.execute(query, {'query_str': query_str})
            return result.fetchall()

    def add_book(self, *, title: str, author: str, description: str, price: float, cover: str):
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            query = """
                INSERT INTO books (title, author, description, price, cover)
                VALUES (?,?,?,?,?)
            """
            cursor.execute(query, (title, author, description, price, cover))
            connection.commit()


database = StorageSQLite('database_prod.sqlite3')
