# *_*coding:utf-8 *_*
import requests
from hashlib import md5

url='http://test.lierdalux.cn:8080/action'
form_data={
    "companyname":"杭州市第一实验中学",
    'type':"2",
    'account':"hym",
    "password":"lierda",
    "pn":"adminLogin2"
}
result=requests.request("post",url,params=form_data).status_code
print result

