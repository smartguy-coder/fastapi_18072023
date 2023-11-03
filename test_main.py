from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_add_book_api():
    params = {
        'title': 'test',
        'author': 'test',
        'description': 'test',
        'price': 100.0,
    }
    response = client.post('/api/add_book', json=params)
    assert response.status_code == 201
    assert "title" in response.json()
