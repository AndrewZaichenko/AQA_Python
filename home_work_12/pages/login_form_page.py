from selenium.webdriver.common.by import By
from home_work_12.pages.base_page import BasePage


class LoginForm(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.email_field = lambda: self._driver.find_element(By.ID, "signinEmail")
        self.password_field = lambda: self._driver.find_element(By.ID, "signinPassword")
        self.login_button = lambda: self._driver.find_element(By.XPATH, "//button[text()='Login']")
