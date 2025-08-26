# tests/test_app.py
from app import app

def test_home():
    # Create a test client from Flask
    client = app.test_client()
    response = client.get("/")

    # Check that the response is OK
    assert response.status_code == 200

    # Check that the returned text contains our message
    assert b"Hello, World! This is my Flask GitFlow demo." in response.data
