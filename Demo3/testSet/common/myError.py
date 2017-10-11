# ========================================================
# Summary        :myError
# Author         :tong shan
# Create Date    :2015-09-28
# Amend History  :
# Amended by     :
# ========================================================

class myError(Exception):

    def __init__(self):
        pass


class clickError(myError):

    def __init__(self, errorLog, errMsg):

        self.errorLog = errorLog
        self.errMsg = errMsg
