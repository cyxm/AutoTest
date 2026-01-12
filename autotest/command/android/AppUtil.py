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

# appium_server_url = 'http://172.17.0.2:4723'
appium_server_url = 'http://localhost:4723'


class AppUtil:

    @classmethod
    def getInstance(cls) -> WebDriver:
        appiumOptions = AppiumOptions().load_capabilities(caps=capabilities)
        return webdriver.Remote(
            appium_server_url,
            options=appiumOptions
        )

    @classmethod
    def restartApp(cls, driver: webdriver, appId: str, startActivity: str):
        driver.terminate_app(appId)
        cap = capabilities.copy()
        cap["appPackage"] = appId
        cap["appActivity"] = startActivity
        driver.start_session(cap)
