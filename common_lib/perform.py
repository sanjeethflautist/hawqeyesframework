from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from common_lib.global_data import GlobalData

def click(driver,by_locator):
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(by_locator)).click()

# this function asserts comparison of a web element's text with passed in text.
def get_element_text(driver,by_locator):
    web_element = WebDriverWait(driver, GlobalData.MAX_EXPLICIT_SYNC_TIME).until(expected_conditions.visibility_of_element_located(by_locator))
    return web_element.text

# this function performs text entry of the passed in text, in a web element whose locator is passed to it.
def enter_text(driver,by_locator, text):
    return WebDriverWait(driver, GlobalData.MAX_EXPLICIT_SYNC_TIME).until(expected_conditions.visibility_of_element_located(by_locator)).send_keys(text)

# this function checks if the web element whose locator has been passed to it, is enabled or not and returns
# web element if it is enabled.
def is_enabled(driver,by_locator):
    return WebDriverWait(driver, GlobalData.MAX_EXPLICIT_SYNC_TIME).until(expected_conditions.visibility_of_element_located(by_locator))

# this function checks if the web element whose locator has been passed to it, is visible or not and returns
# true or false depending upon its visibility.
def is_visible(driver,by_locator):
    element = WebDriverWait(driver, GlobalData.MAX_EXPLICIT_SYNC_TIME).until(expected_conditions.visibility_of_element_located(by_locator))
    return bool(element)

# this function moves the mouse pointer over a web element whose locator has been passed to it.
def hover_to(driver,by_locator):
    element = WebDriverWait(driver, GlobalData.MAX_EXPLICIT_SYNC_TIME).until(expected_conditions.visibility_of_element_located(by_locator))
    ActionChains(driver).move_to_element(element).perform()
