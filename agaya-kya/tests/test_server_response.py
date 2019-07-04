import flask
import pytest
from aagaya import app

@pytest.fixture
def client():
    yield app

def test_book_my_show_api(client):
    app_instance = client.test_client()
    response = app_instance.post("/getdetailsbycity", json={
        'city': 'Trivandrum'
    })
    assert response.status_code == 200 