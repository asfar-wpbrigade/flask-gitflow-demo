def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    body = response.data.decode("utf-8")
    assert "Hello, World!" in body
    assert "This is my Flask GitFlow demo." in body
