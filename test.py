# coding = utf-8

import unittest
from login import app
import json


class LoginTest(unittest.TestCase):
    # 构造单元测试案例
    def test_empty_username_password(self):
        # 测试用户名密码不完整的情况
        # 创建进行web请求的客户端,使用flask提供
        client=app.test_client()
        # 利用client客户端模拟发送web请求
        ret=client.post("/login",data={})

        # ret是视图返回的响应对象,data属性是响应体数据
        resp=ret.data
        # 因为login视图返回的是json字符串
        resp=json.loads(resp)

        # 拿到返回值后,开始断言测试
        self.assertIn("code",resp)
        self.assertEqual(resp["code"],1)

if __name__ == '__main__':
    unittest.main()

