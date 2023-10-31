from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='templates')

#  WEB

@app.get('/')
def main(request: Request):
    context = {
        'title': 'First page',
        'request': request,
    }

    return templates.TemplateResponse('index.html', context=context)


@app.get('/web')
def root_web2(request: Request):
    context = {
        'title': 'First page on WEB',
        'request': request,
        'my_age': 'I am ten',
    }

    return templates.TemplateResponse('other.html', context=context)


#  API
class RootUser(BaseModel):
    name: str
    hobbies: list[str]
    age: int = 10

    def get_age_plus_4(self):
        return self.age + 4


@app.get("/api/")
@app.post("/api/")
def read_root() -> RootUser:
    data = {"name": "Alex", 'hobbies': ['tennis', 'soccer']}
    return RootUser(**data)


@app.post("/api/get_user")
def read_root_user(user: RootUser) -> RootUser:
    print(user.get_age_plus_4(), 888888888888888)
    return user


items = [
    'item 0',
    'item 1',
    'item 2',
    'item 3',
]


@app.get("/api/items/{item_id}")
def read_item(item_id: int, limit: int | None = None) -> dict:
    print(item_id, type(item_id))
    print(f'{limit=}')
    return {"item_id": item_id, "limit": limit, 'items': items[:limit]}
