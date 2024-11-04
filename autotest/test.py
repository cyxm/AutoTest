# encoding=UTF-8
import unittest

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait

from autotest.command.android.android_command_util import AndroidCommandUtil

capabilities = {
    "platformName": "Android",
    "automationName": 'uiautomator2',
    "deviceName": 'Android',
    "appPackage": 'com.pax.us.pay.std.evertec',
    "appActivity": 'com.pax.pay.ui.SplashActivity',
    "noReset": True
}

appium_server_url = 'http://localhost:4723'


class TestAppium(unittest.TestCase):
    caseCount = 0

    def setUp(self):
        print(f'Test Case{TestAppium.caseCount} Start')
        pass

    def tearDown(self):
        print(f'Test Case{TestAppium.caseCount} Finish')
        TestAppium.caseCount += 1
        pass

    @classmethod
    def setUpClass(cls):
        print('All Test Case Start')
        cls.caseCount = 0
        cls.driver = webdriver.Remote(appium_server_url,
                                      options=UiAutomator2Options().load_capabilities(caps=capabilities))
        cls.wait = WebDriverWait(driver=cls.driver, timeout=30, poll_frequency=1)
        pass

    @classmethod
    def tearDownClass(cls):
        # if cls.driver:
        #     cls.driver.quit()
        pass

    def test_find_battery(self) -> None:
        AndroidCommandUtil.wait_widget_text(self.wait, "CREDIT").click()
        pass

    def test_find2(self) -> None:
        # self.driver.pull_file()
        # open()
        print('222')
        pass


if __name__ == '__main__':
    unittest.main()
