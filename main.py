from datetime import datetime

from fastapi import FastAPI, Request, status
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from storage import database as db

app = FastAPI()
templates = Jinja2Templates(directory='templates')
app.mount('/static', StaticFiles(directory='static'), name='static')


class NewBook(BaseModel):
    title: str
    author: str
    description: str = None
    price: float
    cover: str


class Book(NewBook):
    pk: int
    created_at: datetime


def _serialize_books(books: list[tuple]) -> list[Book]:
    books_serialized = [
        Book(
            pk=book[0],
            title=book[1],
            author=book[2],
            description=book[3],
            price=book[4],
            cover=book[5],
            created_at=book[6],
        ) for book in books
    ]
    return books_serialized


#  WEB

@app.get('/', tags=['web'])
def main(request: Request):
    context = {
        'title': 'First page',
        'request': request,
    }

    return templates.TemplateResponse('index.html', context=context)


@app.get('/all-books', tags=['web'])
def all_books(request: Request):
    context = {
        'title': 'Our books',
        'request': request,
        'books': db.get_books(),
    }

    return templates.TemplateResponse('all_books.html', context=context)


#  API



@app.post("/api/add_book", status_code=status.HTTP_201_CREATED, tags=['API'])
def add_book(book: NewBook):
    db.add_book(
        title=book.title,
        author=book.author,
        description=book.description,
        price=book.price,
        cover=book.cover,
    )
    return book


@app.get('/api/get_books', tags=['API'])
@app.post('/api/get_books', tags=['API'])
def get_books(limit: int = 10) -> list[Book]:
    books = db.get_books(limit=limit)
    return _serialize_books(books)


@app.get('/api/get_books_search', tags=['API'])
def get_books_search(query_str: str) -> list[Book]:
    books = db.get_book_by_title_or_other_str(query_str=query_str)
    return _serialize_books(books)













class RootUser(BaseModel):
    name: str
    hobbies: list[str]
    age: int = 10

    def get_age_plus_4(self):
        return self.age + 4


@app.get("/api/", tags=['trash'])
@app.post("/api/", tags=['trash'])
def read_root() -> RootUser:
    data = {"name": "Alex", 'hobbies': ['tennis', 'soccer']}
    return RootUser(**data)


@app.post("/api/get_user", tags=['trash'])
def read_root_user(user: RootUser) -> RootUser:
    print(user.get_age_plus_4(), 888888888888888)
    return user


items = [
    'item 0',
    'item 1',
    'item 2',
    'item 3',
]


@app.get("/api/items/{item_id}", tags=['trash'])
def read_item(item_id: int, limit: int | None = None) -> dict:
    print(item_id, type(item_id))
    print(f'{limit=}')
    return {"item_id": item_id, "limit": limit, 'items': items[:limit]}
