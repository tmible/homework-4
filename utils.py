from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

from constants import TIMEOUT, PERIOD, SUCCESS_POP_UP_CSS_SELECTOR, ERROR_POP_UP_CSS_SELECTOR

def wait_for_element_by_selector(driver, selector, visible=True):
    if visible:
        return WebDriverWait(driver, TIMEOUT, PERIOD).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, selector))
        )
    else:
        return WebDriverWait(driver, TIMEOUT, PERIOD).until(
            expected_conditions.invisibility_of_element_located((By.CSS_SELECTOR, selector))
        )

def wait_for_element_by_xpath(driver, selector, visible=True):
    return WebDriverWait(driver, TIMEOUT, PERIOD).until(
        expected_conditions.visibility_of_element_located((By.XPATH, selector))
    ) if visible else WebDriverWait(driver, TIMEOUT, PERIOD).until(
        expected_conditions.invisibility_of_element_located((By.XPATH, selector))
    )

def wait_for_element_to_be_clickable_by_selector(driver, selector):
    return WebDriverWait(driver, TIMEOUT, PERIOD).until(
        expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, selector))
    )

def wait_for_url(driver, url):
    return WebDriverWait(driver, TIMEOUT, PERIOD).until(
        expected_conditions.url_to_be(url)
    )

def wait_for_url_to_match(driver, pattern):
    return WebDriverWait(driver, TIMEOUT, PERIOD).until(
        expected_conditions.url_matches(pattern)
    )

def wait_for_new_window(driver, current_handles):
    return WebDriverWait(driver, TIMEOUT, PERIOD).until(
        expected_conditions.new_window_is_opened(current_handles)
    )

def wait_for_no_alert(driver):
    try:
        WebDriverWait(driver, 3).until(expected_conditions.alert_is_present())
        raise 'Alert'
    except TimeoutException:
        pass

def wait_for_pop_up(driver, success = True):
    return WebDriverWait(driver, TIMEOUT, PERIOD).until(
        expected_conditions.visibility_of_element_located((
            By.CSS_SELECTOR,
            (SUCCESS_POP_UP_CSS_SELECTOR if success else ERROR_POP_UP_CSS_SELECTOR)
        ))
    )

def wait_for_element_value(driver, selector):
    return WebDriverWait(driver, TIMEOUT, PERIOD).until(lambda driver:
        driver.find_element_by_css_selector(selector).get_attribute('value') != ''
    )

def wait_for_element_attribute_change(driver, selector, attribute, value):
    return WebDriverWait(driver, TIMEOUT, PERIOD).until(lambda driver:
        driver.find_element_by_css_selector(selector)
            .get_attribute(attribute) == value
    )
