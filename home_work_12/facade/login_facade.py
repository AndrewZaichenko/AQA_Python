from home_work_12.facade.base_facade import BaseFacade


class LoginFacade(BaseFacade):

    def __init__(self, driver):
        super().__init__(driver)

    def login_user(self, email, password):
        self._main_page.sign_in_button().click()
        self._login_form_page.email_field().send_keys(email)
        self._login_form_page.password_field().send_keys(password)
        self._login_form_page.login_button().click()

    def check_is_user_logged_in(self):
        return len(self._garage_page.user_photo()) != 0
