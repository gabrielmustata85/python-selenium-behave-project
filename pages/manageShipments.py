import time
from pages.basepage import BasePage
from locators.manage import ManagePageLocators
from locators.home import HomePageLocators


class ManageShipemnt(BasePage):
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = ManageShipemnt()
        return cls.instance

    def __init__(self):
        super().__init__()

    def click_manage_button(self):
        super().do_click(HomePageLocators.MANAGE_SHIPMENT)

    def click_reset_filters(self):
        super().do_click(ManagePageLocators.RESET_FILTER)

    def click_cancel_shipment(self):
        super().do_click(ManagePageLocators.FIRST_SHIPMENT_OPTIONS_BUTTON)
        time.sleep(1)
        super().do_click(ManagePageLocators.CANCEL_BUTTON)
        time.sleep(1)
        super().do_click(ManagePageLocators.CONFIRM_CANCEL_SHIPMENT)

    def verify_status(self):
        assert super().element_exists(ManagePageLocators.SHIPMENT_STATUS) is True, (
            "Cancel"
        )


manageShipment_page = ManageShipemnt.get_instance()
