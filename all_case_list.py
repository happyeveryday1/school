# *_*coding:utf-8 *_*
import sys
sys.path.append('...')
from login import start_login
#用例文件列表
def caselist():
    alltestnames = [
        start_login.Login,
    ]
    print "success read case list"
    return alltestnames