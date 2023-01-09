from selenium.webdriver.common.by import By
from locators.locator import Locator

class ManagePageLocators(object):
    RESET_FILTER = Locator(By.XPATH, "//body/div[2]/div[2]/div[2]/div[1]/form[1]/div[3]/div[1]/a[1]")
    FIRST_SHIPMENT_OPTIONS_BUTTON = Locator(By.XPATH, "//tbody/tr[1]/td[11]/div[1]/a[1]")
    CANCEL_BUTTON = Locator(By.XPATH, "//a[contains(.,'Cancel')]")
    CONFIRM_CANCEL_SHIPMENT = Locator(By.XPATH, "//body/div[2]/div[2]/div[2]/div[1]/div[2]/form[1]/div[2]/button[1]")
    SHIPMENT_STATUS= Locator(By.XPATH, "//tbody/tr[1]/td[10]")

