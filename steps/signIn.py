from behave import *

from context.config import settings
from context.driver import driver
from pages.signInPage import SignIn, signIn_page


@given("User starts the app")
def step_impl(self):
    driver.navigate(settings.url)


@step("User enter the email")
def step_impl(self):
    signIn_page.add_email(settings.email)


@step("User enter the password")
def step_impl(self):
    signIn_page.add_password(settings.password)


@when("User clicks on the Login button")
def step_impl(self):
    signIn_page.click_signIn()


@then("The homepage should be displayed")
def step_impl(self):
    signIn_page.verify_homepage()


@given('User enter role email "{email}"')
def step_impl(self, email):
   signIn_page.add_email(email)


@given('User enter role password "{password}"')
def step_impl(self, password):
     signIn_page.add_password(password)