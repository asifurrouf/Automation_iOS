__author__ = 'tongshan'

import unittest


class Demo1(unittest.TestCase):

    # 初始化工作
    def setUp(self):
        pass

    # 退出时的清理工作 e.g.删除产生的环境垃圾，退出登陆的用户
    def tearDown(self):
        pass

    # 具体的测试用例，以test开头
    def test_fail(self):
        self.assertEqual("1", "2", "test fail")

    def test_pass(self):
        self.assertEqual("2", "2", "test pass")

if __name__ == '__main__':
    unittest.main()