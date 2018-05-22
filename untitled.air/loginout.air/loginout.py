# -*- encoding=utf8 -*-
__author__ = "zhangwk02"

from airtest.core.api import *

auto_setup(__file__)
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from common.read_xls import read_xls

poco = AndroidUiautomationPoco(force_restart=False)

login_data=read_xls("test_data.xlsx")
#判断是否处于登录状态

def login():
    poco("com.vanke.wyguide:id/et_username").set_text(login_data[0][0])
    poco("com.vanke.wyguide:id/et_password").set_text(login_data[0][1])
    poco("android.widget.Button").click()
    sleep(1)
    a = poco("com.vanke.wyguide:id/titleRb").get_text()
    assert_equal("工作台", a, "登录成功.")

def login_out():
    # 登出
    poco("com.vanke.wyguide:id/navigation_dashboard").child("com.vanke.wyguide:id/icon").click()
    poco("com.vanke.wyguide:id/logoutBtn").click()
    login = poco("android.widget.Button").get_text()
    assert_equal("登 录", login, "登出1_.")

#通过判断一下元素是否存在，来判断是否处于登录状态
if __name__ == '__main__':
    if poco("com.vanke.wyguide:id/navigation_dashboard"):
        #元素存在，处于登录状态
        login_out()

    else:
        #元素不存在，不处于登录状态
        try:
            login()
        except Exception as ex:
            raise ex
        #退出try语句总会执行程序
        finally:
            login_out()










