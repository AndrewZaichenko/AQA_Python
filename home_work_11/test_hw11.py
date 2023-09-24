"""
Write test for user registration, using pytest(with setup\teardowns), and selenium

https://qauto2.forstudy.space
https://guest:welcome2qauto@qauto2.forstudy.space/
//button[text()='Sign In']
//button[contains(text(), 'Sign ') and @class]
//label[text()='Password']/ancestor::div[@class='form-group']//input]
//button[text()='Sign up']
//p[text()='You don’t have any cars in your garage']
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

driver = webdriver.Chrome()

driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")
sign_up_button = driver.find_element(By.XPATH, "//button[text()='Sign up']")
sign_up_button.click()
first_name_field = driver.find_element(By.ID, "signupName")
first_name_field.send_keys("Erik")
last_name_field = driver.find_element(By.ID, "signupLastName")
last_name_field.send_keys("Schrody")
email_field = driver.find_element(By.ID, "signupEmail")
email_field.send_keys("everlastgrgefyth@email.com")
password_field = driver.find_element(By.ID, "signupPassword")
password_field.send_keys("Qwerty123")
repeat_password_field = driver.find_element(By.ID, "signupRepeatPassword")
repeat_password_field.send_keys("Qwerty123")
register_button = driver.find_element(By.XPATH, "//button[text()='Register']")
register_button.click()


def test_empty_garage_after_registration():
    empty_garage = driver.find_elements(By.XPATH, "//p[text()='You don’t have any cars in your garage']")
    assert len(empty_garage) == 1



a = 0

