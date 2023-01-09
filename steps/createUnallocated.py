from behave import *
from pages.createUnallocated import CreateUnallocated, createUnallocated_page
from pages.createShipmentPage import CreateShipment, createShipment_page


@when('User clicks on Save button')
def step_impl(self):
    createShipment_page.click_save_button()


@then('User clicks on Unallocated button')
def step_impl(self):
    createUnallocated_page.click_unallocated()


@then('Selects the last entry and click Edit')
def step_impl(self):
    createUnallocated_page.click_edit()
