# *_*coding:utf-8 *_*
import unittest,time
import requests
class Login(unittest.TestCase):
    def setUp(self):
        self.base_url='http://test.lierdalux.cn:8080/action'
        self.verificationErrors = []
        self.accept_next_alert = True

     #正常登录
    def test_login_01(self):
        u"正常登录"
        form_data = {
            "companyname": "杭州市第一实验中学",
            'type': "2",
            'account': "hym",
            "password": "lierda",
            "pn": "adminLogin2"
        }
        result = requests.request("post", self.base_url, params=form_data).status_code
        print result

    def tearDown(self):
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()