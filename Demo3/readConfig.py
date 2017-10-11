import os
import configparser
import codecs
global configfile_path

prjDir = os.path.split(os.path.realpath(__file__))[0]
configfile_path = os.path.join(prjDir, "config.ini")


class ReadConfig:
    def __init__(self):

        fd = open(configfile_path)
        data = fd.read()
        # remove BOM
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(configfile_path, "w")
            file.write(data)
            file.close()
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(configfile_path)

    def getConfigValue(self, name):
        value = self.cf.get("config", name)
        return value

    def getcmdValue(self, name):
        value = self.cf.get("cmd", name)
        return value