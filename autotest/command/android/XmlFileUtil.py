# encoding=UTF-8
from appium import webdriver

from autotest.command.android.FileUtil import FileUtil
from autotest.command.android.XmlUtil import XmlUtil


class XmlFileUtil:

    @classmethod
    def handleXmlFile(cls, driver: webdriver, filePath: str, xmlHandler):
        capContent = FileUtil.pullFile(driver, filePath)
        tree = XmlUtil.toTree(capContent)

        xmlHandler(tree)

        FileUtil.pushFile(driver, filePath, XmlUtil.fromTreeWithHead(tree))
