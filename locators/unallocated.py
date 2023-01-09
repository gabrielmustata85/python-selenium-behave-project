from selenium.webdriver.common.by import By
from locators.locator import Locator


class UnallocatedPageLocators(object):
    SAVE_BUTTON = Locator(By.XPATH, "//body[1]/div[2]/div[2]/div[1]/div[1]/div[1]/h4[1]/span[1]")
    UNALLOCATED_OPTIONS = Locator(By.XPATH, "//tbody/tr[1]/td[11]/div[1]/a[1]")
    UNALLOCATED_EDIT = Locator(By.XPATH, "//tbody/tr[1]/td[11]/div[1]/div[1]/a[1]")
