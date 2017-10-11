
from selenium.common.exceptions import WebDriverException
import readConfig as readConfig
from testSet.common import init
import threading
from appium import webdriver
from urllib.error import URLError
readConfigLocal = readConfig.ReadConfig()


class MyDriver:

    driver = None
    mutex = threading.Lock()
    myInit = init.Init()
    platformName = readConfigLocal.getConfigValue("platformName")
    platformVersion = myInit.get_android_version()
    appPackage = readConfigLocal.getConfigValue("appPackage")
    appActivity = readConfigLocal.getConfigValue("appActivity")
    deviceName = myInit.get_deviceName()
    baseUrl = readConfigLocal.getConfigValue("baseUrl")
    desired_caps = {"platformName": platformName, "platformVersion": platformVersion, "appPackage": appPackage,
                    "appActivity": appActivity, "deviceName": deviceName}

    def _init__(self):
        pass

    @staticmethod
    def get_driver():

        try:
            if MyDriver.driver is None:
                MyDriver.mutex.acquire()
                if MyDriver.driver is None:

                    try:
                        MyDriver.driver = webdriver.Remote(MyDriver.baseUrl, MyDriver.desired_caps)
                    except URLError:
                        MyDriver.driver = None

                MyDriver.mutex.release()

            return MyDriver.driver
        except WebDriverException:
            raise
