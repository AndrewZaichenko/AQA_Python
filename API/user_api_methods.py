"""
Написати тести на створювання користувача, та логін у систему.
Тест на перевірку профіля користувача
Написати параметризований тест, на перевірку реєстрації з правильними та неправильними паролями з перевіркою статус кодів
https://qauto2.forstudy.space/api-docs/ ( login:guest, password:welcome2qauto)
"""

import requests


class UserSignUpModel:

    def __init__(self, name, last_name, email, password, repeat_password):
        self.name = name
        self.lastName = last_name
        self.email = email
        self.password = password
        self.repeatPassword = repeat_password


class UserSignInModel:

    def __init__(self, email, password, remember=False):
        self.email = email
        self.password = password
        self.remember = remember


user_session = requests.session()


# Creating a new User (Registers users in the system)
def user_signup_method():
    user_signup_data = UserSignUpModel("Lawrence", "Muggerud", "cypress@hill.com", "Qwerty12345", "Qwerty12345")
    user_signup = requests.post(url="https://qauto2.forstudy.space/api/auth/signup", json=user_signup_data.__dict__)
    print(user_signup, user_signup.text)
    return user_signup


# Sign in to System
def user_signin_method():
    user_signin_data = UserSignInModel("cypress@hill.com", "Qwerty12345")
    user_signin = user_session.post(url="https://qauto2.forstudy.space/api/auth/signin", json=user_signin_data.__dict__)
    print(user_signin, user_signin.text)
    return user_signin


# Check a User Profile (Gets authenticated user profile data)
def get_user_profile_data_method():
    get_user_profile_data = user_session.get(url="https://qauto2.forstudy.space/api/users/profile")
    print(get_user_profile_data, get_user_profile_data.text)
    return get_user_profile_data


# Deletes user's account and current user session
def delete_user_account_method():
    delete_user_account = user_session.delete(url="https://qauto2.forstudy.space/api/users")
    print(delete_user_account, delete_user_account.text)
    return delete_user_account
