import os
import sys
import pytest

# Add the parent directory (project root) to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    # Match the current app.py output
    assert b"Hello, World! This is my Flask GitFlow demo. First change in main branch." in response.data
