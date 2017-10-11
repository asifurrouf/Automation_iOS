
import os
import readConfig as readConfig
readConfigLocal = readConfig.ReadConfig()


class Init:

    def __init__(self):
        global viewPhone, viewAndroid, startServer, closeServer, checkPhone, installSoftware, uninstallSoftware, prjDir
        viewPhone = readConfigLocal.getcmdValue("viewPhone")
        viewAndroid = readConfigLocal.getcmdValue("viewAndroid")
        startServer = readConfigLocal.getcmdValue("startServer")
        closeServer = readConfigLocal.getcmdValue("closeServer")
        checkPhone = readConfigLocal.getcmdValue("checkPhone")
        installSoftware = readConfigLocal.getcmdValue("installSoftware")
        uninstallSoftware = readConfigLocal.getcmdValue("uninstallSoftware")
        prjDir = readConfig.prjDir

    def connect_phone(self):
        """
        check the phone is connect
        """
        value = os.popen(checkPhone)

        for data in value.readline():
            s_date = str(data)
            if s_date.find("device"):
                return True
        return False

    def get_deviceName(self):
        """get deviceName
        :return:deviceName
        """
        device_list = []

        return_value = os.popen(viewPhone)
        for value in return_value.readlines():
            s_value = str(value)
            if s_value.rfind('device'):
                if not s_value.startswith("List"):
                    device_list.append(s_value[:s_value.find('device')].strip())
        if len(device_list) != 0:
            return device_list[0]
        else:
            return None

    def get_android_version(self):
        """get androidVersion
        :return:androidVersion
        """
        return_value = str(os.popen(viewAndroid).read())

        if return_value != '':
            pop = return_value.rfind(str('='))
            return return_value[pop+1:]
        else:
            return None

    def start_server(self):
        """start the adb server
        :return:
        """
        os.system(startServer)

    def close_server(self):
        """close the adb server
        :return:
        """
        os.popen(closeServer)

    def re_start(self):
        """reStart the adb server
        :return:
        """
        self.close_server()
        self.start_server()

    def install(self):

        """
        install software in mobile

        :return: True or False
        """

        apk = self.get_apk()

        print(apk)
        if apk != '':
            value = os.popen(installSoftware+" "+apk)
            s_value = str(value.read())
            if s_value.find("Success"):
                return True
        else:
            return False

    def uninstall(self):
        """uninstall software in mobile

        :return: True or False
        """
        os.system(uninstallSoftware)


    def get_apk(self):
        """
        get test APK in prjPath

        :return:basename
        """
        apks = os.listdir(prjDir)
        print(prjDir)
        if len(apks) > 0:
            for apk in apks:

                basename = os.path.basename(apk)
                if basename.split('.')[-1] == "apk":
                    return basename
                # if os.path.isfile(apk):
                #     basename = os.path.basename(apk)
                #     print(basename)
                #     if basename.split('.')[-1] == "apk":
                #         print(basename)
                #         return basename
        else:
            return None


if __name__ == '__main__':
    ojb = Init()
    print(ojb.get_deviceName())

