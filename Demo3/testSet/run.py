
import os
import readConfig as readConfig
import unittest
from testSet.common.DRIVER import MyDriver
from testSet.common.AppiumServer import AppiumServer
import testSet.common.Log as Log
from time import sleep
from testSet.common import HTMLTestRunner
from urllib.error import URLError

readConfigLocal = readConfig.ReadConfig()

baseUrl = readConfigLocal.getConfigValue("baseUrl")


class Alltest():

    def __init__(self):
        global log, logger, resultPath
        self.caseListPath = os.path.join(readConfig.prjDir, "caseList.txt")
        self.casePath = os.path.join(readConfig.prjDir, "testSet")
        self.caseList = []
        self.myServer = AppiumServer()
        log = Log.MyLog.get_log()
        logger = log.get_my_logger()
        resultPath = log.get_result_path()

    def driver_on(self):
        """open the driver
        :return:
        """
        MyDriver.get_driver()

    def driver_off(self):
        """close the driver
        :return:
        """
        MyDriver.get_driver().quit()

    def set_case_list(self):
        """from the caseList get the caseName,set in caseList
        :return:
        """
        fp = open(self.caseListPath)

        for data in fp.readlines():

            s_data = str(data)
            if s_data != '' and not s_data.startswith("#"):
                self.caseList.append(s_data.replace("\n", ""))
        fp.close()

    def create_suite(self):
        """from the caseList,get caseName,According to the caseName to search the testSuite
        :return:test_suite
        """
        self.set_case_list()
        test_suite = unittest.TestSuite()
        suite_module_list = []

        if len(self.caseList) > 0:

            for case_name in self.caseList:

                discover = unittest.defaultTestLoader.discover(self.casePath, pattern=case_name+'.py', top_level_dir=None)
                suite_module_list.append(discover)

        if len(suite_module_list) > 0:

            for suite in suite_module_list:
                for test_name in suite:
                    test_suite.addTest(test_name)
        else:
            return None

        return test_suite

    def run(self):
        """run test
        :return:
        """
        try:
            suit = self.create_suite()
            if suit is not None:

                logger.info("Begin to start Appium Server")

                self.myServer.start_server()

                while not self.myServer.is_runnnig():
                    sleep(1)

                else:
                    logger.info("End to start Appium Server")
                    logger.info("Open Driver")
                    self.driver_on()
                    logger.info("Start to test")
                    fp = open(resultPath, 'wb')
                    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='testReport', description='Report_description')
                    runner.run(suit)
                    logger.info("End to test")

            else:
                logger.info("Have no test to run")
        except Exception as ex:
            logger.error(str(ex))

        finally:
            try:
                logger.info("Close to Driver")
                self.driver_off()
                logger.info("Begin stop Appium Server")
                self.myServer.stop_server()
                logger.info("End stop Appium Server")
            except URLError as ex:
                logger.error(str(ex))
            except ConnectionRefusedError as ex:
                logger.error(str(ex))
            except KeyError as ex:
                logger.error(str(ex))

if __name__ == '__main__':
    ojb = Alltest()
    ojb.run()

