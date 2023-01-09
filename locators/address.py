from selenium.webdriver.common.by import By
from locators.locator import Locator

class AddressLocators(object):
    ADDRESSES = Locator(By.XPATH, "//span[contains(text(),'Addresses')]")
    MANAGE_ADDRESSES = Locator(By.XPATH, "//a[@id='manage-address']")
    NEW_ADDRESS = Locator(By.XPATH, "//span[contains(text(),'New Address')]")
    ADDRESS_BUSINESS_NAME = Locator(By.XPATH, "//input[@id='BusinessName']")
    ADDRESS_LINE1 = Locator(By.XPATH, "//input[@id='AddressLine1']")
    ADDRESS_LINE2 = Locator(By.XPATH, "//input[@id='AddressLine2']")
    ADDRESS_COUNTY = Locator(By.XPATH, "//input[@id='County']")
    ADDRESS_CITY = Locator(By.XPATH, "//input[@id='City']")
    FIRST_NAME = Locator(By.XPATH, "//input[@id='FirstName']")
    LAST_NAME = Locator(By.XPATH, "//input[@id='LastName']")
    PHONE_AREA_PREFIX = Locator(By.XPATH, "//input[@id='PhoneAreaPrefix']")
    CONTACT_PHONE_NUMBER = Locator(By.XPATH, "//input[@id='ContactPhoneNumber']")
    ADDRESS_EMAIL = Locator(By.XPATH, "//input[@id='Email']")
    ZIP_CODE = Locator(By.XPATH, "//input[@id='PostZipCode']")
    
    CREATE_ADDRESS = Locator(By.XPATH, "//body/div[2]/div[2]/div[2]/div[1]/div[2]/form[1]/button[1]")
