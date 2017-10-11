"""
test loginaaaaa
"""
import unittest
import paramunittest

from time import sleep
import testSet.common.Log as Log
from testSet.common.common import Element
from testSet.bsns import bsnsCommon
from testSet.common.DRIVER import MyDriver

loginCls = bsnsCommon.get_login_cls()


@paramunittest.parametrized(*loginCls)
class TestLogin(unittest.TestCase):
    """
    case_name
    """

    def setParameters(self, case_name, email, password, results, message):
        """
        get the parameter for login
        :param case_name
        :param email
        :param password
        :param results
        :param message
        :return:
        """

        self.case_name = str(case_name)
        self.email = str(email)
        self.password = str(password)
        self.results = str(results)
        self.message = str(message)

    def get_description(self):
        return self.case_name

    def setUp(self):

        self.Begin = "../../result/image/1.png"
        self.CheckPoint = "../../result/image/1.png"
        self.End = "../../result/image/1.png"

        # get Driver
        self.driver = MyDriver.get_driver()
        self.caseNo = self.case_name

        # get Log
        self.log = Log.MyLog().get_log()
        self.logger = self.log.get_my_logger()

        # test Start
        self.log.build_start_line(self.caseNo)

        self.Begin = self.log.take_shot(self.driver, self.case_name)

        self.logger.info("Take shot, the picture path is " + self.Begin)

        # open app
        bsnsCommon.open_app()

        self.logger.info("Open app")

    def testLogin(self):
        """
        test login
        :return:
        """

        try:

            self.logger.info("Enter the profile")

            # find the bottom Navigation bar
            while not Element("BottomNavigation", "BottomNavigation").is_exist():
                sleep(1)
            else:
                # enter the profile
                Element("BottomNavigation", "profile").click()

            bsnsCommon.wait_loading()

            # login the app
            bsnsCommon.login(self.email, self.password)

            # check the result
            self.check_result()

        except Exception as ex:
            self.logger.error(str(ex))

    def tearDown(self):

        self.End = self.log.take_shot(self.driver, self.case_name)

        self.logger.info("Take shot, the picture path is " + self.End)

        # return the index
        bsnsCommon.return_index()

        # test Start
        self.log.build_end_line(self.caseNo)

    def check_result(self):
        """
        check the result
        :return:
        """

        self.CheckPoint = self.log.take_shot(self.driver, self.case_name)
        self.logger.info("Take shot, the picture path is " + self.CheckPoint)

        # login success
        if self.results == '1':

            bsnsCommon.wait_loading()

            value = Element("profile", "user").get_attribute("text")

            self.assertEqual(value, self.message)

        # login fail
        if self.results == '0':

            sleep(1)

            if Element("Alert", "layout").does_exist():

                value = Element("Alert", "message").get_attribute("text")

                self.assertEqual(value, self.message)

                sleep(1)
                Element("Alert", "confirm").click()

