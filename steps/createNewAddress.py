import time

from behave import *
from pages.createNewAddressPage import CreateAddressPage, createNewAddress_page


@step("User clicks on Addresses")
def step_impl(self):
    createNewAddress_page.click_addresses()


@step("User clicks on Manage Addresses")
def step_impl(self):
    createNewAddress_page.click_manage_addresses()


@step("User clicks on New Address")
def step_impl(self):
    createNewAddress_page.click_new_address()


@step("User adds Address Business Name")
def step_impl(self):
    createNewAddress_page.add_address_business_name("Automated Tests")


@step("User adds Address Line1")
def step_impl(self):
    createNewAddress_page.add_address1("Long Street Of Automated Tests")


@step("User adds Address Line2")
def step_impl(self):
    createNewAddress_page.add_address2("Without end")


@step("User adds Address County")
def step_impl(self):
    createNewAddress_page.add_address_county("Manchester")


@step("User adds Address City")
def step_impl(self):
    createNewAddress_page.add_address_city("Manchester")


@step("User adds First Name")
def step_impl(self):
    createNewAddress_page.add_first_name("Automation")


@step("User adds Last Name")
def step_impl(self):
    createNewAddress_page.add_last_name("Forever")


@step("User adds Phone Area Prefix")
def step_impl(self):
    createNewAddress_page.add_phone_area_prefix("+44")


@step("User adds Contact Phone Number")
def step_impl(self):
    createNewAddress_page.add_phone("09876253647")


@step("User adds Address Email")
def step_impl(self):
    createNewAddress_page.add_address_email("test@test_automation.com")


@then("User adds Post Zip Code")
def step_impl(self):
    createNewAddress_page.add_post_zip_code("M27 8WA")


@step("User clicks on Create Address button")
def step_impl(self):
    createNewAddress_page.click_create_address()


@then("The new address is created")
def step_impl(self):
    createNewAddress_page.verifying_url()
