from Base.BaseLog import myLog


class Element(object):
    find_element_by_id = "id"
    find_elements_by_xpath = "xpaths"
    find_element_by_xpath = "xpath"
    find_element_by_css_selector = "css"
    find_element_by_class_name = "class_name"
    CLICK = "click"
    TAP = "tap"
    SWIPELEFT = "swipeLeft"
    SET_VALUE = "set_value"
    GET_VALUE = "get_value"
    WAIT_TIME = 20

    # logTest = myLog().getLog() # 其他日志记录

    INFO = []
    SUM = {"appName": "", "appSize": "", "appVersion": "", "testDate": "", "sum": 0, "pass": 0,
            "fail": 0, "testSumDate": ""}