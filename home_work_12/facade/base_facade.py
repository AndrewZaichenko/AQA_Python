from home_work_12.pages.garage_page import GaragePage
from home_work_12.pages.main_page import MainPage
from home_work_12.pages.registration_form_page import RegistrationForm


class BaseFacade:

    def __init__(self, driver):
        self._driver = driver
        self._main_page = MainPage(self._driver)
        self._registration_form_page = RegistrationForm(self._driver)
        self._garage_page = GaragePage(self._driver)
