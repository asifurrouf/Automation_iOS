from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from .exceptions import InvalidLocatorException

locator_to_by_map = {
    "id": By.ID,
    "xpath": By.XPATH,
    "link": By.LINK_TEXT,
    "partial_link": By.PARTIAL_LINK_TEXT,
    "name": By.NAME,
    "tag": By.TAG_NAME,
    "class": By.CLASS_NAME,
    "css": By.CSS_SELECTOR,
    "ios_predicate": MobileBy.IOS_PREDICATE,
    "ios_uiautomation": MobileBy.IOS_UIAUTOMATION,
    "android_uiautomator": MobileBy.ANDROID_UIAUTOMATOR,
    "accessibility_id": MobileBy.ACCESSIBILITY_ID
}


def locator_to_by_value(locator):
    separator_index = locator.find("=")
    if separator_index == -1:
        raise InvalidLocatorException("Separator '=' is not found.")
    by = locator[:separator_index]
    value = locator[separator_index + 1:]
    try:
        by = locator_to_by_map[by]
    except KeyError:
        raise InvalidLocatorException("The by <%s> of locator <%s> is not a valid By." % (by, locator))
    return by, value