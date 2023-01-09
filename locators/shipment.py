from selenium.webdriver.common.by import By
from locators.locator import Locator


class ShipmentPageLocators(object):
    REFERENCE = Locator(By.XPATH, "//input[@id='ShippingDetail_ReferenceOne']")
    BUSINESS_NAME = Locator(By.XPATH, "//input[@id='businessName']")
    CONTACT = Locator(By.XPATH, "//input[@id='DeliveryAddress_FullName']")
    ADDRESS_LINE1 = Locator(By.XPATH, "//input[@id='addressLine1']")
    ADDRESS_LINE2 = Locator(By.XPATH, "//input[@id='addressLine2']")
    COUNTY = Locator(By.XPATH, "//input[@id='county']")
    CITY = Locator(By.XPATH, "//input[@id='city']")
    ZIP_CODE = Locator(By.XPATH, "//input[@id='DeliveryAddress_PostZipCode']")
    CREATE_SHIPMENT_BUTTON = Locator(By.XPATH, "//button[contains(.,'Create Shipment')]")
    GREEN_SUCCESS_NOTIFICATION = Locator(By.CSS_SELECTOR, ".shipment-confirmation")

    CARRIER = Locator(By.XPATH, "//body[1]/div[2]/div[2]/div[2]/div[1]/form[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/span[1]/span[1]/span[1]/span[1]")
    # CARRIER_OPTION = Locator(By.XPATH, "//option[contains(text(),'"+carrier+"')]")

    PHONE_NUMBER = Locator(By.XPATH, "//input[@id='DeliveryAddress_PhoneNumber']")
    WEIGHT = Locator(By.XPATH, "//body[1]/div[2]/div[2]/div[2]/div[1]/form[1]/div[2]/div[3]/div[1]/div[1]/div["
                               "2]/table[1]/tbody[1]/tr[1]/td[3]/input[1]")

    EMAIL = Locator(By.XPATH, "//input[@id='DeliveryAddress_EmailAddress']")

    SAVE_BUTTON = Locator(By.XPATH, "//body/div[2]/div[2]/div[2]/div[1]/form[1]/div[2]/button[3]")
    




