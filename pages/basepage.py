jquery_url = "http://code.jquery.com/jquery-1.11.2.min.js"
# coding = utf-8
from context.config import settings
from context.driver import driver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from PIL import Image, ImageDraw


class BasePage:
    """Base class for all page objects in the Page Object Model"""

    def __init__(self):
        self.driver = driver.get_driver()

    def _execute_with_wait(self, condition):
        return WebDriverWait(self.driver, settings.driver_timeout).until(condition)

    def current_url(self):
        return self.current_url()

    def element_exists(self, locator):
        try:
            self._execute_with_wait(
                ec.presence_of_element_located(
                    (locator.l_type, locator.selector))
            )
            self._execute_with_wait(
                ec.presence_of_element_located(
                    (locator.l_type, locator.selector))
            )
            return True
        except TimeoutException:
            return False

    def get_element(self, locator):
        if not self.element_exists(locator):
            raise NoSuchElementException("Could not find {locator.selector}")

        return self.driver.find_element(locator.l_type, locator.selector)

    def do_click(self, locator):
        try:
            self._execute_with_wait(
                ec.presence_of_element_located(
                    (locator.l_type, locator.selector))
            ).click()
            return True
        except TimeoutException:
            return False

    def do_double_click(self, locator):
        source = self.get_element(locator)
        action = ActionChains(self.driver)
        action.double_click(source).perform()

    def do_send_keys(self, locator, text):
        try:
            self._execute_with_wait(
                ec.presence_of_element_located(
                    (locator.l_type, locator.selector))
            ).send_keys(text)
            return True
        except TimeoutException:
            return False

    def do_clear(self, locator):
        try:
            self._execute_with_wait(
                ec.presence_of_element_located(
                    (locator.l_type, locator.selector))
            ).clear()
            return True
        except TimeoutException:
            return False

    def get_text(self, locator):
        try:
            locator_text = self._execute_with_wait(
                ec.presence_of_element_located(
                    (locator.l_type, locator.selector))
            ).text
            return locator_text
        except TimeoutException:
            return False

    def switch_to_pop_up(self):
        self.switch_to_alert()

    def analyze(self, reference_screenshot, actual_screenshot, result_screenshot):
        screenshot_reference = Image.open(reference_screenshot + ".png")
        screenshot_actual = Image.open(actual_screenshot + ".png")
        columns = 60
        rows = 80
        control_variable = 0
        screen_width, screen_height = screenshot_reference.size
        block_width = ((screen_width - 1) // columns) + 1  # this is just a division ceiling
        block_height = ((screen_height - 1) // rows) + 1

        for y in range(0, screen_height, block_height + 1):
            for x in range(0, screen_width, block_width + 1):
                region_staging = self.process_region(screenshot_reference, x, y, block_width, block_height)
                region_production = self.process_region(screenshot_actual, x, y, block_width, block_height)

                if region_staging is not None and region_production is not None and region_production != region_staging:
                    draw = ImageDraw.Draw(screenshot_reference)
                    draw.rectangle((x, y, x + block_width, y + block_height), outline="red")
                    control_variable = control_variable + 1
        screenshot_reference.save(result_screenshot + ".png")
        assert (control_variable == 0) is True, (
            "Screenshots are different"
        )

    def process_region(self, image, x, y, width, height):
        region_total = 0

        # This can be used as the sensitivity factor, the larger it is the less sensitive the comparison
        factor = 20

        for coordinateY in range(y, y + height):
            for coordinateX in range(x, x + width):
                try:
                    pixel = image.getpixel((coordinateX, coordinateY))
                    region_total += sum(pixel) / 4
                except:
                    return

        return region_total / factor

    def drag_and_drop(self, s, d):
        action = ActionChains(self.driver)
        action.click_and_hold(s).pause(4).move_by_offset(-20, 10).perform()
        # time.sleep(2)
        # # load jQuery helper
        # with open(os.path.join(sys.path[0], "pages/Resources/jquery_load_helper.js")) as f:
        #     load_jquery_js = f.read()
        #
        # # load drag and drop helper
        # with open(os.path.join(sys.path[0], "pages/Resources/drag_and_drop_helper.js")) as f:
        #     drag_and_drop_js = f.read()
        #
        # # load jQuery
        # self.driver.execute_async_script(load_jquery_js, jquery_url)
        # self.driver.execute_script(drag_and_drop_js + "$('#AUTHRSC_PAGE_HOME_AUTHRSC_WIDGET_ASSETSSTATUS').simulateDragDrop({ dropTarget: '#content'});")
        # time.sleep(2)
        #

        # self.driver.execute_script(
        #     "function createEvent(typeOfEvent) {\n" + "var event =document.createEvent(\"CustomEvent\");\n"
        #     + "event.initCustomEvent(typeOfEvent,true, true, null);\n" + "event.dataTransfer = {\n" + "data: {},\n"
        #     + "setData: function (key, value) {\n" + "this.data[key] = value;\n" + "},\n"
        #     + "getData: function (key) {\n" + "return this.data[key];\n" + "}\n" + "};\n" + "return event;\n"
        #     + "}\n" + "\n" + "function dispatchEvent(element, event,transferData) {\n"
        #     + "if (transferData !== undefined) {\n" + "event.dataTransfer = transferData;\n" + "}\n"
        #     + "if (element.dispatchEvent) {\n" + "element.dispatchEvent(event);\n"
        #     + "} else if (element.fireEvent) {\n" + "element.fireEvent(\"on\" + event.type, event);\n" + "}\n"
        #     + "}\n" + "\n" + "function simulateHTML5DragAndDrop(element, destination) {\n"
        #     + "var dragStartEvent =createEvent('dragstart');\n" + "dispatchEvent(element, dragStartEvent);\n"
        #     + "var dropEvent = createEvent('drop');\n"
        #     + "dispatchEvent(destination, dropEvent,dragStartEvent.dataTransfer);\n"
        #     + "var dragEndEvent = createEvent('dragend');\n"
        #     + "dispatchEvent(element, dragEndEvent,dropEvent.dataTransfer);\n" + "}\n" + "\n"
        #     + "var source = arguments[0];\n" + "var destination = arguments[1];\n"
        #     + "simulateHTML5DragAndDrop(source,destination);", '#AUTHRSC_PAGE_HOME_AUTHRSC_WIDGET_ASSETSSTATUS', '#content')
