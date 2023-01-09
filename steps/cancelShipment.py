import time

from behave import *
from pages.manageShipments import ManageShipemnt, manageShipment_page


@then('User clicks on Manage Shipments button')
def step_impl(self):
    manageShipment_page.click_manage_button()


@then('User resets the filters')
def step_impl(self):
    manageShipment_page.click_reset_filters()


@when('User clicks on Cancel button')
def step_impl(self):
    manageShipment_page.click_cancel_shipment()


@then('The shipment is canceled')
def step_impl(self):
    manageShipment_page.verify_status()
