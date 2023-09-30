"""
Write test for user registration, using pytest(with setup\teardowns), and selenium

https://qauto2.forstudy.space
https://guest:welcome2qauto@qauto2.forstudy.space/
//button[text()='Sign In']
//button[contains(text(), 'Sign ') and @class]
//label[text()='Password']/ancestor::div[@class='form-group']//input]
//button[text()='Sign up']
//p[text()='You don’t have any cars in your garage']
//a[@routerlink='settings']
//a[consist(@href, 'panel/settings']
//button[text()='Remove my account']
//button[text()='Remove']
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestRegistration:

    def setup_class(self):
        self.driver = webdriver.Chrome()
        # self.driver.implicitly_wait(3)
        self.user_session = requests.session()

    def test_empty_garage_after_registration(self):
        self.driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")
        sign_up_button = self.driver.find_element(By.XPATH, "//button[text()='Sign up']")
        sign_up_button.click()
        first_name_field = self.driver.find_element(By.ID, "signupName")
        first_name_field.send_keys("Erik")
        last_name_field = self.driver.find_element(By.ID, "signupLastName")
        last_name_field.send_keys("Schrody")
        email_field = self.driver.find_element(By.ID, "signupEmail")
        email_field.send_keys("blackjesus@email.com")
        password_field = self.driver.find_element(By.ID, "signupPassword")
        password_field.send_keys("Qwerty123")
        repeat_password_field = self.driver.find_element(By.ID, "signupRepeatPassword")
        repeat_password_field.send_keys("Qwerty123")
        register_button = self.driver.find_element(By.XPATH, "//button[text()='Register']")
        register_button.click()
        # empty_garage = self.driver.find_elements(By.XPATH, "//p[text()='You don’t have any cars in your garage']")
        empty_garage = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//p[text()='You don’t have any cars in your garage']")))
        # assert len(empty_garage) == 1
        assert empty_garage is not None

    def teardown_class(self):
        self.user_session.post(url="https://qauto2.forstudy.space/api/auth/signin",
                               json={"email": "blackjesus@email.com", "password": "Qwerty123"})
        self.user_session.delete(url="https://qauto2.forstudy.space/api/users")
