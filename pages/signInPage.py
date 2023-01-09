import time

from locators.home import HomePageLocators
from locators.signIn import SignInLocators
from pages.basepage import BasePage


class SignIn(BasePage):
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = SignIn()
        return cls.instance

    def __init__(self):
        super().__init__()

    def add_email(self, email):
        super().do_clear(SignInLocators.EMAIL_INPUT)
        super().do_send_keys(SignInLocators.EMAIL_INPUT, email)

    def add_password(self, password):
        super().do_clear(SignInLocators.PASSWORD_INPUT)
        super().do_send_keys(SignInLocators.PASSWORD_INPUT, password)
        time.sleep(2)

    def click_signIn(self):
        super().do_click(SignInLocators.CONTINUE_BUTTON)
        time.sleep(2)

    def verify_homepage(self):
        assert super().element_exists(HomePageLocators.HOME_PAGE_TITLE) is True, (
            "HomePage is not displayed" 
        )
        time.sleep(2)


signIn_page = SignIn.get_instance()
