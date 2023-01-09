import time


from pages.basepage import BasePage
from locators.address import AddressLocators

class CreateAddressPage(BasePage):
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = CreateAddressPage()
        return cls.instance

    def __init__(self):
        super().__init__()

    def click_addresses(self):
        super().do_click(AddressLocators.ADDRESSES)
        time.sleep(1)

    def click_manage_addresses(self):
            super().do_click(AddressLocators.MANAGE_ADDRESSES)
            time.sleep(1)

    def click_new_address(self):
            super().do_click(AddressLocators.NEW_ADDRESS)
            time.sleep(1)

    def add_address_business_name(self, address_business_name):
        super().do_send_keys(AddressLocators.ADDRESS_BUSINESS_NAME, address_business_name)

    def add_address1(self, address1):
        super().do_send_keys(AddressLocators.ADDRESS_LINE1, address1)

    def add_address2(self, address2):
            super().do_send_keys(AddressLocators.ADDRESS_LINE2, address2)

    def add_address_county(self, address_county):
        super().do_send_keys(AddressLocators.ADDRESS_COUNTY, address_county)

    def add_address_city(self, address_city):
        super().do_send_keys(AddressLocators.ADDRESS_CITY, address_city)

    def add_first_name(self, first_name):
        super().do_send_keys(AddressLocators.FIRST_NAME, first_name)

    def add_last_name(self, last_name):
        super().do_send_keys(AddressLocators.LAST_NAME, last_name)

    def add_phone_area_prefix(self, phone_area_prefix):
        super().do_send_keys(AddressLocators.PHONE_AREA_PREFIX, phone_area_prefix)

    def add_phone(self, phoneNumber):
        super().do_send_keys(AddressLocators.CONTACT_PHONE_NUMBER, phoneNumber)

    def add_address_email(self, address_email):
        super().do_send_keys(AddressLocators.ADDRESS_EMAIL, address_email)
        time.sleep(2)

    def click_create_address(self):
        super().do_click(AddressLocators.CREATE_ADDRESS)
        time.sleep(2)

    def add_post_zip_code(self, zip_code):
        super().do_send_keys(AddressLocators.ZIP_CODE, zip_code)

    def verifying_url(self):
        # super().current_url() is True, (
        #     "https://test-app.smartconsign.io/Address" 
        # )
        print(super().current_url)
        
createNewAddress_page = CreateAddressPage.get_instance()