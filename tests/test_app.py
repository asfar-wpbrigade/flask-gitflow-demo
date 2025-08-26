from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    
    # Decode bytes → string for easier matching
    body = response.data.decode("utf-8")
    
    # Check key parts instead of full exact string
    assert "Hello, World!" in body
    assert "This is my Flask GitFlow demo." in body
