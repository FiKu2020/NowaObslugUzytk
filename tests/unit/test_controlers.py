import pytest
from src.repositories import UserController

def test_get_single_user_not_found(Usercontroller):
    user = UserController.get_single_user(100)
    assert "error" in user