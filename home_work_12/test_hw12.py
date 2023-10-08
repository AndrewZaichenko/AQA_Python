"""
Write test for user registration, using pytest(with setup\teardowns), and selenium
+
Add classes for driver, pages, facades for previous homework
"""
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
from home_work_12.facade.registration_facade import RegistrationFacade


class TestBase:

    def setup_method(self):
        self._driver = webdriver.Chrome()
        self._user_session = requests.session()
        self._registration_facade = RegistrationFacade(self._driver)
        self._driver.implicitly_wait(3)
        self._driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")


class TestRegistration(TestBase):

    def setup_class(self):
        self.user_first_name = "Erik"
        self.user_last_name = "Schrody"
        self.user_email = "blackjesus@email.com"
        self.user_password = "Qwerty123"

    def teardown_method(self):
        self._user_session.post(url="https://qauto2.forstudy.space/api/auth/signin",
                               json={"email": self.user_email, "password": self.user_password})
        self._user_session.delete(url="https://qauto2.forstudy.space/api/users")
        self._driver.close()

    def test_empty_garage_after_registration(self):
        self._registration_facade.register_user(self.user_first_name, self.user_last_name, self.user_email, self.user_password, self.user_password)
        assert self._registration_facade.check_is_user_logged_in()

    def test_empty_garage_after_registration_2(self):
        # self._driver.implicitly_wait(3)
        # self._driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")
        sign_up_button = self._driver.find_element(By.XPATH, "//button[text()='Sign up']")
        sign_up_button.click()
        first_name_field = self._driver.find_element(By.ID, "signupName")
        first_name_field.send_keys(self.user_first_name)
        last_name_field = self._driver.find_element(By.ID, "signupLastName")
        last_name_field.send_keys(self.user_last_name)
        email_field = self._driver.find_element(By.ID, "signupEmail")
        email_field.send_keys(self.user_email)
        password_field = self._driver.find_element(By.ID, "signupPassword")
        password_field.send_keys(self.user_password)
        repeat_password_field = self._driver.find_element(By.ID, "signupRepeatPassword")
        repeat_password_field.send_keys(self.user_password)
        register_button = self._driver.find_element(By.XPATH, "//button[text()='Register']")
        register_button.click()
        empty_garage = self._driver.find_elements(By.XPATH, "//p[text()='You don’t have any cars in your garage']")
        # empty_garage = WebDriverWait(self._driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//p[text()='You don’t have any cars in your garage']")))
        assert empty_garage is not None
