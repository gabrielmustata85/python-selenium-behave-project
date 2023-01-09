from context.driver import driver, Driver


def after_all(self):
    driver.stop_instance()


def before_scenario(self, scenario):
    driver.clear_cookies()


# def after_step(self, step):
#     if step.status == 'failed' and 'check for UI inconsistencies in' not in step.name:
#         driver.screenshot_take()
#     if 'check for UI inconsistencies in' in step.name:
#         name = step.name
#         name = name.lstrip('check for UI inconsistencies in')
#         driver.attach_result_allure(name)
