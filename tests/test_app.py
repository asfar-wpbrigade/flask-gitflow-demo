from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    # Updated assertion to match the current app response
    assert b"Hello, World! This is my Flask GitFlow demo. First change in main branch." in response.data
