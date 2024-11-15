# encoding=UTF-8

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from autotest.command.android.WidgetName import WidgetName


class UIController:
    SELECTOR_TEXT = "new UiSelector().text(\"%s\")"
    SELECTOR_CLASS = "new UiSelector().className(\"%s\")"
    SELECTOR_ID = "new UiSelector().resourceId(\"%s:id/%s\")"

    def __init__(self, driver: WebDriver, waitTime: int, appId: str):
        self.driver = driver
        self.timeout = waitTime
        self.wait = WebDriverWait(driver=self.driver, timeout=30, poll_frequency=1)
        self.appId = appId

    def waitForActivity(self, activity: str):
        self.driver.wait_activity(activity, self.timeout)

    def getByText(self, text: str):
        return self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=self.SELECTOR_TEXT % text)

    def getByClz(self, clz: str):
        return self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=self.SELECTOR_CLASS % clz)

    def getById(self, appId: str, widgetId: str):
        return self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=self.SELECTOR_ID % (appId, widgetId))

    def waitForWidgetText(self, text: str):
        return self.wait.until(lambda x: self.getByText(text))

    def waitForWidgetClz(self, clz: str):
        return self.wait.until(lambda x: self.getByClz(clz))

    def waitForWidgetId(self, widgetId: str):
        return self.wait.until(lambda x: self.getById(self.appId, widgetId))

    def inputText(self, content: str):
        self.getByClz(WidgetName.EditText).send_keys(content)

    def focusEditText(self):
        self.getByClz(WidgetName.EditText).click()

    def clickText(self, text: str):
        self.getByText(text).click()

    def clickId(self, widgetId: str):
        self.getById(self.appId, widgetId).click()
