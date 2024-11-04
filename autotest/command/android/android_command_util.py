# encoding=UTF-8
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait


class AndroidCommandUtil:
    SELECTOR_TEXT = "new UiSelector().text(\"%s\")"

    @classmethod
    def wait_widget_text(cls, wait: WebDriverWait, text: str):
        return wait.until(
            lambda x: x.find_element(
                by=AppiumBy.ANDROID_UIAUTOMATOR, value=cls.SELECTOR_TEXT % text
            )
        )
