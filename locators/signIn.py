from selenium.webdriver.common.by import By
from locators.locator import Locator


class SignInLocators:
    EMAIL_INPUT = Locator(By.XPATH, "//input[@id='username']")
    PASSWORD_INPUT = Locator(By.XPATH, "//input[@id='password']")
    CONTINUE_BUTTON = Locator(By.XPATH, "//button[contains(text(),'Continue')]")
