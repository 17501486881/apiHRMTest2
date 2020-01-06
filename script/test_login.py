import unittest
from api.login_api import LoginApi
import logging

from utils import assert_commom


class TestIHRMLogin(unittest.TestCase):
    def setUp(self) -> None:
        pass

    @classmethod
    def setUpClass(cls) -> None:
        # 初始化登陆类
        cls.login_api = LoginApi()

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test01_login_success(self):
        # 调用封装的登陆接口
        response = self.login_api.login('13800000002', '123456')
        # 接收返回的json数据
        jsonData = response.json()
        # 调试输出登陆接口返回的数据
        logging.info("登陆成功接口返回的数据为：{}".format(jsonData))

        # # 断言
        # self.assertEqual(200, response.status_code)
        # self.assertEqual(True, jsonData.get('success'))
        # self.assertEqual(10000, jsonData.get("code"))
        # self.assertIn("操作成功", jsonData.get('message'))

        assert_commom(self, response, 200, True, 10000, "操作成功")

    def test02_username_is_not_exist(self):
        # 调用封装的登陆接口
        response = self.login_api.login('13900000002', '123456')

        # 接收返回的json数据
        jsonData = response.json()

        # 调试输出登陆接口返回的数据
        logging.info("账号不存在时输出的数据为:{}".format(jsonData))
        # 断言
        assert_commom(self, response, 200, False, 20001, "用户名或密码错误")

    def test03_password_is_not_error(self):
        # 调用封装的登陆接口
        response = self.login_api.login('13800000002', 'error')

        # 接收返回的json数据
        jsonData = response.json()

        # 调试输出登陆接口返回的数据
        logging.info("密码错误时输出的数据为:{}".format(jsonData))
        # 断言
        assert_commom(self, response, 200, False, 20001, "用户名或密码错误")

    def test04_username_have_special_char(self):
        # 调用封装的登陆接口
        response = self.login_api.login('@#%4_^7*%4', '123456')

        # 接收返回的json数据
        jsonData = response.json()

        # 调试输出登陆接口返回的数据
        logging.info("账号输入特殊字符时输出的数据为:{}".format(jsonData))
        # 断言
        assert_commom(self, response, 200, False, 20001, "用户名或密码错误")

    def test05_username_is_empty(self):
        # 调用封装的登陆接口
        response = self.login_api.login('', '123456')

        # 接收返回的json数据
        jsonData = response.json()

        # 调试输出登陆接口返回的数据
        logging.info("账号为空时输出的数据为:{}".format(jsonData))
        # 断言
        assert_commom(self, response, 200, False, 20001, "用户名或密码错误")

    def test06_password_is_empty(self):
        # 调用封装的登陆接口
        response = self.login_api.login('13800000002', '')

        # 接收返回的json数据
        jsonData = response.json()

        # 调试输出登陆接口返回的数据
        logging.info("账号为空时输出的数据为:{}".format(jsonData))
        # 断言
        assert_commom(self, response, 200, False, 20001, "用户名或密码错误")

    def test07_username_have_chinese(self):
        # 调用封装的登陆接口
        response = self.login_api.login('138000000中2', '123456')

        # 接收返回的json数据
        jsonData = response.json()

        # 调试输出登陆接口返回的数据
        logging.info("账号有中文时输出的数据为:{}".format(jsonData))
        # 断言
        assert_commom(self, response, 200, False, 20001, "用户名或密码错误")

    def test08_username_(self):
        # 调用封装的登陆接口
        response = self.login_api.login('138000000 2', '123456')

        # 接收返回的json数据
        jsonData = response.json()

        # 调试输出登陆接口返回的数据
        logging.info("账号有空格时输出的数据为:{}".format(jsonData))
        # 断言
        assert_commom(self, response, 200, False, 20001, "用户名或密码错误")



