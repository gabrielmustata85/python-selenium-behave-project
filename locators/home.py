from selenium.webdriver.common.by import By
from locators.locator import Locator


class HomePageLocators(object):
    HOME_PAGE_TITLE = Locator(By.XPATH, "//body[1]/div[2]/div[2]/div[1]/div[1]/div[1]/h4[1]/span[1]")
    SHIPMENTS_MENU_BUTTON = Locator(By.XPATH, "//span[contains(.,'Shipments')]")
    CREATE_A_SHIPMENT_BUTTON = Locator(By.XPATH, "//a[contains(text(),'Create a Shipment')]")
    UNALLOCATED_MENU_BUTTON = Locator(By.XPATH, "//a[contains(text(),'Unallocated')]")
    MANAGE_SHIPMENT= Locator(By.XPATH, "//a[@id='manage-shipment']")