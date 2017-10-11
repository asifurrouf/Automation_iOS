__author__ = 'tongshan'

import unittest
import paramunittest


@paramunittest.parametrized((1, 2), (2, 1))
class Demo2(paramunittest.ParametrizedTestCase):

    # 初始化工作
    def setUp(self):
        self.case_name = "test Parameters"
        self.Begin = "../../result/image/1.png"
        self.CheckPoint = "../../result/image/1.png"
        self.End = "../../result/image/1.png"

    # 设置参数
    def setParameters(self, a):
        self.a = a

    # 退出时的清理工作 e.g.删除产生的环境垃圾，退出登陆的用户
    def tearDown(self):
        pass

    # 具体的测试用例，以test开头
    def test_11(self):
        self.assertEqual(self.a, 1, "test Parameters")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Demo2)
    unittest.TextTestRunner(verbosity=2).run(suite)
