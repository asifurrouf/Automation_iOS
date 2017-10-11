
import os
import urllib.request
from urllib.error import URLError
from multiprocessing import Process
import readConfig as readConfig
import threading
readConfigLocal = readConfig.ReadConfig()


class AppiumServer:

    def __init__(self):
        global openAppium, baseUrl
        openAppium = readConfigLocal.getcmdValue("openAppium")
        baseUrl = readConfigLocal.getConfigValue("baseUrl")

    def start_server(self):
        """start the appium server
        :return:
        """
        t1 = RunServer(openAppium)
        p = Process(target=t1.start())
        p.start()

    def stop_server(self):
        """stop the appium server
        :return:
        """
        # kill myServer
        os.popen('pkill node')

    def re_start_server(self):
        """reStart the appium server
        """
        self.stop_server()
        self.start_server()

    def is_runnnig(self):
        """Determine whether server is running
        :return:True or False
        """
        response = None
        url = baseUrl+"/status"
        try:
            response = urllib.request.urlopen(url, timeout=5)

            if str(response.getcode()).startswith("2"):
                return True
            else:
                return False
        except URLError:
            return False
        finally:
            if response:
                response.close()


class RunServer(threading.Thread):

    def __init__(self, cmd):
        threading.Thread.__init__(self)
        self.cmd = cmd

    def run(self):
        os.system(self.cmd)


if __name__ == "__main__":

    oo = AppiumServer()
    oo.start_server()
    print("strart server")
    print("running server")
    oo.stop_server()
    print("stop server")