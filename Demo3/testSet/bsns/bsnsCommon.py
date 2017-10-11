
from time import sleep
from testSet.common import common as common
from testSet.common.common import Element
import testSet.common.Log as Log
log = Log.MyLog.get_log()
logger = log.get_my_logger()


def open_app():
    """
    open the app,enter the index
    :return:
    """

    logger.info("Begin open the app")
    # skip
    if Element("GuideActivity", "Guide").is_exist():

        logger.info("Click skin button")
        Element("GuideActivity", "skip").click()

    # welcome
    if Element("GuideActivity", "welcome").is_exist():

        logger.info("Gide page--swip right")
        while not Element("GuideActivity", "goShop").is_exist():

            # swip right
            common.my_swipe_to_right()
            sleep(1)
        else:
            Element("GuideActivity", "goShop").click()

    # loading
    wait_loading()

    # update
    if Element("Alert", "cancel").is_exist():
        Element("Alert", "cancel").click()

    # loading
    wait_loading()

    logger.info("End open the app")


def login(email, password):
    """
    login app
    :param email:
    :param password:
    :return:
    """

    logger.info("Begin login the app")
    if not Element("profile", "SignIn").is_exist():

        logger.debug("Current is already login, first logout")

        logout()

    logger.debug("Begin login")
    Element("profile", "SignIn").click()
    wait_loading()

    if Element("login", "title").does_exist():
        # input email
        Element("login", "mailAndPass").send_keys(0, email)

        # input password
        Element("login", "mailAndPass").send_keys(1, password)

        # click sign in button
        Element("login", "signIn").click()

    else:
        pass

    logger.info("End login the app")


def logout():
    """
    logout the app
    :return:
    """
    # if already sign in , first sign out
    while not Element("profile", "SignOut").is_exist():

        # swipe up
        common.my_swipe_to_up()
    else:

        logger.debug("Begin logout")
        Element("profile", "SignOut").click()

        if Element("Alert", "confirm").is_exist():
            Element("Alert", "confirm").click()

        wait_loading()
        logger.debug("End logout")


def return_index():
    """
    return then index
    :return:
    """

    # Determine whether there is BottomNavigation
    logger.info("Determine whether there is BottomNavigation")
    while not Element("BottomNavigation", "BottomNavigation").is_exist():

        # key event:back
        logger.info("Key event:back")
        common.back()

        sleep(1)
        if Element("BottomNavigation", "BottomNavigation").is_exist():
                break

        logger.info("Swipe down")
        common.my_swipe_to_down()

        sleep(1)
        if Element("BottomNavigation", "BottomNavigation").is_exist():
                break

    # click the shop button
    Element("BottomNavigation", "shop").click()

    wait_loading()


def enter_cart():
    """
    enter the shopping cart
    :return:
    """
    logger.info("Enter add cart page")
    Element("Good_details", "add").click()


def add_goods_in_cart(num):
    """
     add goods to cart
    :param num: goods number
    :return:
    """

    if num == 0:
        return

    goods_name_list = []

    for i in range(num):

        if Element("BottomNavigation", "BottomNavigation").is_exist():
            common.my_swipe_to_up()

        while not Element("Shop", "goods").is_exist():
                common.my_swipe_to_up()
        else:
            Element("Shop", "goods").clicks(i)

            goods_name = Element("title", "title").get_attribute("text")

            goods_name_list.append(goods_name)

            enter_cart()

            if Element("add_cart", "add_cart").does_exist():

                logger.info("Select size")
                Element("add_cart", "size").clicks(0)

            Element("add_cart", "buy").click()
        logger.info("Return index")
        return_index()
    return goods_name_list


def delete_goods_in_cart(goods_name):
    """
    delete goods in shopping cart
    :param goods_name: you need delete goods's name
    :return:
    """
    logger.info("Delete the goods which we choose")
    goods_list = []

    logger.info("Determine whether there is a goods")
    while Element("Shopping_cart", "goods_name").is_exist():

        logger.info("Get the goods name")
        element_list = Element("Shopping_cart", "goods_name").get_element_list()

        if element_list is not None:

            logger.info("Get the last goods name")
            last_goods_name = element_list[-1].get_attribute("text")

            for i in range(len(element_list)):

                value = element_list[i].get_attribute("text")

                if value == goods_name:

                    logger.info("Delete goods")

                    Element("Shopping_cart", "delete_goods").clicks(i)

                    Element("Alert", "confirm").click()

                    wait_loading()

                    return

        if last_goods_name not in goods_list:

            logger.info("Goods is not end")

            logger.info("Swipe up, if not end")

            common.my_swipe_to_up()

            goods_list.append(last_goods_name)
        else:
            logger.info("Goods is end")
            return


def clear_cart():
    """
    clear the shopping cart
    :return:
    """
    logger.info("Clear the shopping cart")
    goods_list = []
    while Element("Shopping_cart", "goods_name").is_exist():
        logger.info("Get the goods name")
        element_list = Element("Shopping_cart", "goods_name").get_element_list()

        if element_list is not None:
            last_goods_name = element_list[-1].get_attribute("text")

            for i in range(len(element_list)):
                logger.info("Delete goods")

                Element("Shopping_cart", "delete_goods").clicks(i)

                Element("Alert", "confirm").click()

                wait_loading()
        if last_goods_name not in goods_list:

            logger.info("Goods is not end")

            logger.info("Swipe up, if not end")

            common.my_swipe_to_up()

            goods_list.append(last_goods_name)
        else:
            logger.info("Goods is end")
            break


def get_total_price_in_cart():
    """
    get the all goods price in shopping cart
    :return:
    """
    logger.info("Determine whether there is a goods")
    goods_list = []
    total_price = 0
    while Element("Shopping_cart", "goods_name").is_exist():
        logger.info("Get the goods name")
        element_list = Element("Shopping_cart", "goods_name").get_element_list()

        if element_list is not None:

            logger.info("Get the last goods name")
            last_goods_name = element_list[-1].get_attribute("text")

            for i in range(len(element_list)):

                goods_name = element_list[i].get_attribute("text")

                if goods_name not in goods_list:
                    goods_list.append(goods_name)

                    goods_price_text = Element("Shopping_cart", "goods_price").gets(i).get_attribute("text")
                    goods_price = goods_price_text[goods_price_text.find("$")+1:]
                    goods_num = Element("Shopping_cart", "goods_num").gets(i).get_attribute("text")

                    one_goods_price = float(goods_price)*int(goods_num)
                    total_price += one_goods_price

            if last_goods_name not in goods_list:

                logger.info("Goods is not end")

                logger.info("Swipe up, if not end")

                common.my_swipe_to_up()

                goods_list.append(last_goods_name)
            else:
                logger.info("Goods is end")
                break
    return str(total_price)




def wait_loading():
    """
    Waiting for the end of the page load
    :return:
    """
    # loading img
    while Element("Alert", "loading").is_exist():
        sleep(1)
    else:
        # time out
        if Element("Alert", "confirm").is_exist():
            Element("Alert", "confirm").click()


def get_login_cls():
    """
    get login cls
    :return: login_cls

    login_cls : [[case_name,user_name,password,result,message],]
    """

    login_cls = common.get_xls("login")

    return login_cls


def get_register_cls():

    register_cls = common.get_xls("register")

    return register_cls


def get_address_cls():

    address_cls = common.get_xls("address")

    return address_cls


def get_change_password_cls():
    change_password_cls = common.get_xls("add_cart")

    return change_password_cls


def get_add_cart_cls():
    add_cart_cls = common.get_xls("add_cart")

    return add_cart_cls


def get_write_review_cls():
    write_review_cls = common.get_xls("add_cart")

    return write_review_cls


def get_feed_back_cls():
    feed_back_cls = common.get_xls("add_cart")

    return feed_back_cls

if __name__ == '__main__':
    print(get_login_cls())