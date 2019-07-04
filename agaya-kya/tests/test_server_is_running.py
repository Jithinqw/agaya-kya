import flask
import pytest
from aagaya import app

@pytest.fixture
def client():
    yield app

def test_ping_api(client):
    app_instance = client.test_client()
    response = app_instance.get("/ping")
    assert response.status_code == 200

def test_app_response(client):
    app_instance = client.test_client()
    response = app_instance.get("/ping")
    assert response.get_json() == "Agaya is alive"
    
