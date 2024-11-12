# encoding=UTF-8
from base64 import b64decode, b64encode

from appium import webdriver


class FileUtil:

    @classmethod
    def pullFile(cls, driver: webdriver, filePath: str) -> bytes:
        capContent = driver.pull_file(filePath)
        return b64decode(capContent)

    @classmethod
    def pushFile(cls, driver: webdriver, filePath: str, fileContent: bytes):
        driver.push_file(
            filePath,
            b64encode(fileContent).decode("utf-8")
        )
