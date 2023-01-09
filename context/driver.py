import behave.configuration
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from context.config import settings


class Driver(object):
    instance = None

    class SeleniumDriverNotFound(Exception):
        pass

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Driver()
        return cls.instance

    def __init__(self):
        if settings.browser == "chrome":
            # behave_opt = behave.configuration.options
            # options = ChromeOptions()
            # options.add_argument("--start-maximized")  # open Browser in maximized mode
            # options.add_argument("--no-sandbox")  # bypass OS security model
            # options.add_argument("--disable-dev-shm-usage")  # overcome limited resource problems
            # options.add_argument("headless")
            # options.add_experimental_option('useAutomationExtension', False)
            self.driver = webdriver.Chrome(ChromeDriverManager().install())
            # self.driver.maximize_window()
            self.driver.set_window_size(1920,1080)
           
        elif settings.browser == "firefox":
            # opts = FirefoxOptions()
            # opts.add_argument("--headless")

            self.driver = webdriver.Firefox()
        # else:
        #     raise SeleniumDriverNotFound(
        #         "{settings.browser} not currently supported")

    def get_driver(self):
        return self.driver

    def stop_instance(self):
        self.driver.quit()
        instance = None

    def clear_cookies(self):
        self.driver.delete_all_cookies()

    def navigate(self, url):
        self.driver.get(url)


driver = Driver.get_instance()
