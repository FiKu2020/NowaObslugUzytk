import pytest
from src.app import app

def test_get_all_users(client):
    response = client.get('/users')
    assert response.status_code == 200

def test_get_single_user(client):
    response = client.get('/users/1')
    assert response.status_code == 200