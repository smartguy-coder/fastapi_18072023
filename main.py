from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#  WEB







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
