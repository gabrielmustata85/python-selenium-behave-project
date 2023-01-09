import time

from behave import *
from pages.createShipmentPage import CreateShipment, createShipment_page


@step("User clicks on Shipments button")
def step_impl(self):
    createShipment_page.click_shipments()


@step("User clicks on Create a Shipment button")
def step_impl(self):
    createShipment_page.create_a_shipment()


@step("User clicks Carrier dropdown")
def step_impl(self):
    createShipment_page.click_carrier()


@step('User selects the "{carrier}"')
def step_impl(self, carrier):
    createShipment_page.add_carrier(carrier)


@step("User adds Reference one")
def step_impl(self):
    createShipment_page.add_reference("12345")


@step("User adds Business Name")
def step_impl(self):
    createShipment_page.add_business_name("Fresh Counselling")


@step("User adds Contact")
def step_impl(self):
    createShipment_page.add_contact("Contact")


@step("User adds Email")
def step_impl(self):
    createShipment_page.add_email("testtest@gmail.com")    


@step("User adds the Phone Number")
def step_impl(self):
    createShipment_page.add_phone("0123456789")


@step("User adds AddressLine1")
def step_impl(self):
    createShipment_page.add_address1("Unit 2 Agecroft")

@step("User adds AddressLine2")
def step_impl(self):
    createShipment_page.add_address2("Shearer Way")


@step("User adds City")
def step_impl(self):
    createShipment_page.add_city("Manchester")

@step("User adds County")
def step_impl(self):
    createShipment_page.add_county("Lancashire")


@step("User adds Zip Code")
def step_impl(self):
    createShipment_page.add_zipCode("M27 8WA")


@step("User adds the Weight")
def step_impl(self):
    createShipment_page.add_weight("5.0")


@step("User clicks on Create Shipment button")
def step_impl(self):
    createShipment_page.click_create_shipment_button()


@step("The green notification message should be visible")
def step_impl(self):
    createShipment_page.verify_manage_shipment_listing()
