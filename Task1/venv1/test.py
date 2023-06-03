from sum import sum_xy
from fastapi.testclient import TestClient
from main import app


def test_sum_xy():
    assert 2 == sum_xy(1, 1)
    assert 4 == sum_xy(3,1 )


client = TestClient(app)

def test_hello():
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_add():
    response = client.post("/add", json={"x": 2, "y": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 5}