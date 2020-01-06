import unittest

import app
from api.login_api import LoginApi
import logging

from utils import assert_commom


class Login(unittest.TestCase):
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

    def test_login(self):
        # 调用封装的登陆接口
        response = self.login_api.login('13800000002', '123456')
        # 接收返回的json数据
        jsonData = response.json()
        # 调试输出登陆接口返回的数据
        logging.info("登陆成功接口返回的数据为：{}".format(jsonData))
        assert_commom(self, response, 200, True, 10000, "操作成功")
        # 获取令牌，并拼接成以Bearer 开头的令牌字符中
        token = jsonData.get("data")
        # 保存令牌到全局变量
        app.HEADERS['Authorization'] = "Bearer " + token
        logging.info("保存的令牌是：{}".format(app.HEADERS))
