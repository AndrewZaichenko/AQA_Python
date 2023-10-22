from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class GaragePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.empty_garage = lambda: self._driver.find_elements(By.XPATH, "//p[text()='You don’t have any cars in your garage']")
        self.user_photo = lambda: self._driver.find_elements(By.XPATH, "//*[@id='userNavDropdown']/img")
        self.profile_dropdown = lambda: self._driver.find_element(By.ID, "userNavDropdown")
        self.user_logout = lambda: self._driver.find_element(By.XPATH, "//button[text()='Logout']")

