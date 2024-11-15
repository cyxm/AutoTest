# encoding=UTF-8
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.webdriver import WebDriver

capabilities = {
    "platformName": "Android",
    "automationName": 'uiautomator2',
    "deviceName": 'Android',
    "noReset": True,
    "fullReset": False
}

appium_server_url = 'http://localhost:4723'


class AppUtil:

    @classmethod
    def getInstance(cls) -> WebDriver:
        return webdriver.Remote(
            appium_server_url,
            options=AppiumOptions().load_capabilities(caps=capabilities)
        )

    @classmethod
    def startApp(cls, driver: webdriver, appId: str, startActivity: str):
        appState = driver.query_app_state(appId)
        if appState != 1:
            driver.terminate_app(appId)

        cap = capabilities.copy()
        cap["appPackage"] = appId
        cap["appActivity"] = startActivity
        driver.start_session(cap)
