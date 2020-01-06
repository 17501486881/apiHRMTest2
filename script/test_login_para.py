import unittest
from api.login_api import LoginApi
import logging
from parameterized.parameterized import parameterized
from utils import assert_commom, read_login_data


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

    @parameterized.expand(read_login_data)
    def test_login(self,mobile,password,http_code,success,code,message):
        # 调用封装的登陆接口
        response = self.login_api.login(mobile,password)
        # 接收返回的json数据
        jsonData = response.json()
        # 调试输出登陆接口返回的数据
        logging.info("登陆接口返回的数据为：{}".format(jsonData))
        assert_commom(self,response,http_code,success,code,message)



