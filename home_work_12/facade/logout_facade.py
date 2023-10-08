from home_work_12.facade.base_facade import BaseFacade


class LogoutFacade(BaseFacade):

    def __init__(self, driver):
        super().__init__(driver)

    def logout_user(self):
        self._garage_page.profile_dropdown().click()
        self._garage_page.user_logout().click()

    def check_is_user_logged_out(self):
        return len(self._main_page.sign_in_button()) != 0
