"""
Написати тести на створювання користувача, та логін у систему.
Тест на перевірку профіля користувача
Написати параметризований тест, на перевірку реєстрації з правильними та неправильними паролями з перевіркою статус кодів
https://qauto2.forstudy.space/api-docs/ ( login:guest, password:welcome2qauto)
"""

import pytest
import user_api_methods as uam
import requests


def test_user_signup():
    signup_response = uam.user_signup_method()
    assert signup_response.status_code == 201


@pytest.mark.parametrize("user_email, user_password", [("cypress@hill.com", "Qwerty12345"), ("hill@cypress.com", "Qwerty12345"), ("cypress@hill.com", "Qwerty")])
def test_user_credentials(user_email, user_password):
    user_credentials = {"email": user_email, "password": user_password, "remember": False}
    user_signin_with_diff_creds = requests.post(url="https://qauto2.forstudy.space/api/auth/signin", json=user_credentials)
    assert user_signin_with_diff_creds.status_code == 200


def test_user_signin():
    signin_response = uam.user_signin_method()
    assert signin_response.status_code == 200


def test_user_profile_data():
    user_profile_data_response = uam.get_user_profile_data_method()
    assert user_profile_data_response.status_code == 200


def test_user_delete():
    user_delete_response = uam.delete_user_account_method()
    assert user_delete_response.status_code == 200
