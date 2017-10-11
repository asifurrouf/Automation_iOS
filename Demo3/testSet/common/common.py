
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import readConfig as readConfig
import os
from testSet.common.DRIVER import MyDriver
import testSet.common.Log as Log
from xml.etree import ElementTree as elementTree
import xlrd

readConfigLocal = readConfig.ReadConfig


log = Log.MyLog.get_log()
logger = log.get_my_logger()


def get_window_size():
    """
    get current windows size mnn
    :return:windowSize
    """
    global windowSize
    windowSize = driver.get_window_size()
    return windowSize


def my_swipe_to_up(during=None):
    """
    swipe UP
    :param during:
    :return:
    """
    # if windowSize == None:
    window_size = get_window_size()

    width = window_size.get("width")
    height = window_size.get("height")
    driver.swipe(width/2, height*3/4, width/2, height/4, during)


def my_swipe_to_down(during=None):
    """
    swipe down
    :param during:
    :return:
    """
    window_size = get_window_size()
    width = window_size.get("width")
    height = window_size.get("height")
    driver.swipe(width/2, height/4, width/2, height*3/4, during)


def my_swipe_to_left(during=None):
    """
    swipe left
    :param during:
    :return:
    """
    window_size = get_window_size()
    width = window_size.get("width")
    height = window_size.get("height")
    driver.swipe(width/4, height/2, width*3/4, height/2, during)


def my_swipe_to_right(during=None):
    """
    swipe right
    :param during:
    :return:
    """
    window_size = get_window_size()
    width = window_size.get("width")
    height = window_size.get("height")
    driver.swipe(width*4/5, height/2, width/5, height/2, during)


def back():
    os.popen("adb shell input keyevent 4")


activity = {}


def set_xml():
    """
    get the xml file's value
    :use:
    a = getXml(path)

    print(a.get(".module.GuideActivity").get("skip").get("type"))
    :param: xmlPath
    :return:activity
    """
    if len(activity) == 0:
        xml_path = os.path.join(readConfig.prjDir, "testSet","bsns", "element.xml")
        # open the xml file
        per = elementTree.parse(xml_path)
        all_element = per.findall('activity')

        for firstElement in all_element:
            activity_name = firstElement.get("name")

            element = {}

            for secondElement in firstElement.getchildren():
                element_name = secondElement.get("name")

                element_child = {}
                for thirdElement in secondElement.getchildren():

                    element_child[thirdElement.tag] = thirdElement.text

                element[element_name] = element_child
            activity[activity_name] = element


def get_el__dict(activity_name, element_name):
    """
    According to the activityName and elementName get element
    :param activity_name:
    :param element_name:
    :return:
    """
    set_xml()
    element_dict = activity.get(activity_name).get(element_name)
    return element_dict


def get_xls(sheet_name):
    """
    get the value in excel
    :param sheet_name
    :return:cls
    """
    cls = []

    xls_path = os.path.join(readConfig.prjDir, "testSet", "bsns", "TestCase.xls")

    # read the excel
    data = xlrd.open_workbook(xls_path)

    # get the sheet
    table = data.sheet_by_name(sheet_name)

    nrows = table.nrows

    for i in range(nrows):

        if table.row_values(i)[0] != u'case_name':
            cls.append(table.row_values(i))

    return cls


class Element:

    def __init__(self, activity_name, element_name):

        global driver
        driver = MyDriver.get_driver()
        self.activity_name = activity_name
        self.element_name = element_name
        element_dict = get_el__dict(self.activity_name, self.element_name)
        self.path_type = element_dict.get("pathtype")
        self.path_value = element_dict.get("pathvalue")

    def is_exist(self):
        """
        To determine whether an element is exits
        :return: TRUE or FALSE
        """
        try:
            if self.path_type == "ID":
                driver.find_element_by_id(self.path_value)
                return True
            if self.path_type == "CLASSNAME":
                driver.find_element_by_class_name(self.path_value)
                return True
            if self.path_type == "XPATH":
                driver.find_element_by_xpath(self.path_value)
                return True
            if self.path_type == "NAME":
                driver.find_element_by_name(self.path_value)
                return True
            return False
        except NoSuchElementException:
            return False

    def does_exist(self):
        """
        To determine whether an element is exits
        :return:
        """
        i = 1
        while not self.is_exist():
            sleep(1)
            i += 1
            if i >= 10:
                return False
        else:
            return True

    def get(self):
        """
        get one element
        :return:
        """
        if self.does_exist():
            if self.path_type == "ID":
                element = driver.find_element_by_id(self.path_value)
                return element
            if self.path_type == "CLASSNAME":
                element = driver.find_element_by_class_name(self.path_value)
                return element
            if self.path_type == "XPATH":
                element = driver.find_element_by_xpath(self.path_value)
                return element
            if self.path_type == "NAME":
                element = driver.find_element_by_name(self.path_value)
                return element
            return None
        else:
            return None

    def gets(self, index):
        """
        get one element in elementList
        :param index
        :return:elements[index]
        """
        if self.does_exist():
            if self.path_type == "ID":
                elements = driver.find_elements_by_id(self.path_value)
                return elements[index]
            if self.path_type == "CLASSNAME":
                elements = driver.find_elements_by_class_name(self.path_value)
                return elements[index]
            if self.path_type == "XPATH":
                elements = driver.find_elements_by_xpath(self.path_value)
                return elements[index]
            if self.path_type == "NAME":
                elements = driver.find_elements_by_name(self.path_value)
                return elements[index]
            return None
        else:
            return None

    def get_element_list(self):
        """
        get elementList
        :return:elements
        """
        if self.does_exist():
            if self.path_type == "ID":
                element_list = driver.find_elements_by_id(self.path_value)
                return element_list
            if self.path_type == "CLASSNAME":
                element_list = driver.find_elements_by_class_name(self.path_value)
                return element_list
            if self.path_type == "XPATH":
                element_list = driver.find_elements_by_xpath(self.path_value)
                return element_list
            if self.path_type == "NAME":
                element_list = driver.find_elements_by_name(self.path_value)
                return element_list
            return None
        else:
            return None

    def click(self):
        """
        click element
        :return:
        """
        try:
            element = self.get()
            element.click()
        except AttributeError:
            raise

    def clicks(self, index):
        """
        click element
        :return:
        """
        try:
            element = self.gets(index)
            element.click()
        except AttributeError:
            raise

    def send_key(self, values):
        """
        input the key
        :param values
        :return:
        """
        try:
            element = self.get()
            element.clear()

            logger.debug("input %s" % (values))
            element.send_keys(values)
        except AttributeError:
            raise

    def send_keys(self, index, values):
        """
        input the key
        :param index
        :param values
        :return:
        """
        try:
            element = self.gets(index)
            element.clear()
            logger.debug("input %s" % (values))
            element.send_keys(values)

        except AttributeError:
            raise

    def get_attribute(self, attribute):
        """
        get the element attribute
        :param attribute:
        :return:value
        """
        try:
            element = self.get()
            value = element.get_attribute(attribute)
            return value
        except AttributeError:
            raise

if __name__ == "__main__":
    print(get_xls("login"))
