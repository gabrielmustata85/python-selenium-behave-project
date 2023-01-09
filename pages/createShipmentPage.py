import time

from locators.home import HomePageLocators
from pages.basepage import BasePage
from locators.shipment import ShipmentPageLocators
from selenium.webdriver.common.by import By
from locators.locator import Locator


class CreateShipment(BasePage):
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = CreateShipment()
        return cls.instance

    def __init__(self):
        super().__init__()

    def click_shipments(self):
        super().do_click(HomePageLocators.SHIPMENTS_MENU_BUTTON)
        time.sleep(1)

    def create_a_shipment(self):
        super().do_click(HomePageLocators.CREATE_A_SHIPMENT_BUTTON)
        time.sleep(1)

    def add_reference(self, reference):
        super().do_send_keys(ShipmentPageLocators.REFERENCE, reference)

    def add_business_name(self, business_name):
        super().do_send_keys(ShipmentPageLocators.BUSINESS_NAME, business_name)

    def add_contact(self, contact):
        super().do_send_keys(ShipmentPageLocators.CONTACT, contact)

    def add_email(self, email):
        super().do_send_keys(ShipmentPageLocators.EMAIL, email)

    def add_address1(self, address1):
        super().do_send_keys(ShipmentPageLocators.ADDRESS_LINE1, address1)

    def add_address2(self, address2):
        super().do_send_keys(ShipmentPageLocators.ADDRESS_LINE2, address2)

    def add_city(self, city):
        super().do_send_keys(ShipmentPageLocators.CITY, city)

    def add_county(self, county):
        super().do_send_keys(ShipmentPageLocators.COUNTY, county)

    def add_zipCode(self, zipCode):
        super().do_send_keys(ShipmentPageLocators.ZIP_CODE, zipCode)

    def click_carrier(self):
        super().do_click(ShipmentPageLocators.CARRIER)
        time.sleep(1)

    def add_carrier(self, carrier):
        CARRIER_XPATH = Locator(By.XPATH, "//option[contains(text(),'" + carrier + "')]")
        super().do_click(CARRIER_XPATH)
        print(CARRIER_XPATH)
        time.sleep(1)

    def add_phone(self, phoneNumber):
        super().do_send_keys(ShipmentPageLocators.PHONE_NUMBER, phoneNumber)

    def add_weight(self, weight):
        super().do_clear(ShipmentPageLocators.WEIGHT)
        super().do_send_keys(ShipmentPageLocators.WEIGHT, weight)
        time.sleep(1)

    def click_create_shipment_button(self):
        super().do_double_click(ShipmentPageLocators.CREATE_SHIPMENT_BUTTON)
        time.sleep(1)

    def click_save_button(self):
        super().do_click(ShipmentPageLocators.SAVE_BUTTON)
        time.sleep(1)

    def verify_manage_shipment_listing(self):
        assert super().element_exists(ShipmentPageLocators.GREEN_SUCCESS_NOTIFICATION) is True, (
            "Shipments listing is not displayed and the shipment was not created"
        )


createShipment_page = CreateShipment.get_instance()
