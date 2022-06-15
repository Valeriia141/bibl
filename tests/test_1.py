from fastapi.testclient import TestClient
from fastapi import status
import sys
sys.path.append('../bibl')
from main import app


client = TestClient(app)


def test_1():
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert isinstance(data, list)


def test_2(valid_body):
    response = client.post('/', json=valid_body)
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["title"] == valid_body["title"]
    assert data["author"] == valid_body["author"]


def test_3(invalid_body):
    response = client.post('/', json=invalid_body)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY