
import time
from pages.basepage import BasePage
from locators.unallocated import UnallocatedPageLocators
from locators.home import HomePageLocators


class CreateUnallocated(BasePage):
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = CreateUnallocated()
        return cls.instance

    def __init__(self):
        super().__init__()


    def click_unallocated(self):
        super().do_click(HomePageLocators.UNALLOCATED_MENU_BUTTON)
        time.sleep(1)

    def click_edit(self):
        super().do_click(UnallocatedPageLocators.UNALLOCATED_OPTIONS)
        super().do_click(UnallocatedPageLocators.UNALLOCATED_EDIT)
        time.sleep(2)


createUnallocated_page = CreateUnallocated.get_instance()
