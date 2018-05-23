# -*- encoding=utf8 -*-
__author__ = "zhangwk02"
from airtest.core.api import *

auto_setup(__file__)
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

import sys
#sys.path.insert(1, "E:\F\zhangwk02\APP_UIauto\common")
sys.path.append("E:\F\zhangwk02\APP_UIauto\common")

from read_xls import read_xls

poco = AndroidUiautomationPoco(force_restart=False)

login_data=read_xls("test_data.xlsx")
#判断是否处于登录状态

def login(poco, login_data):
    poco("com.vanke.wyguide:id/et_username").set_text(login_data[0][0])
    poco("com.vanke.wyguide:id/et_password").set_text(login_data[0][1])
    poco("android.widget.Button").click()
    sleep(1)
    a = poco("com.vanke.wyguide:id/titleRb").get_text()
    assert_equal("张文凯的工作台", a, "登录成功.")
#登出
def login_out(poco):
    #点击进入我的栏目
    poco("com.vanke.wyguide:id/navigation_home").click()
    #点击进入工作台
    poco("com.vanke.wyguide:id/titleRb").click()
    #判断是否处于工作状态
    if poco("com.vanke.wyguide:id/startWorkBtn").get_text() == "开始工作":
        poco("com.vanke.wyguide:id/titleTv").click()
        poco("com.vanke.wyguide:id/navigation_dashboard").child("com.vanke.wyguide:id/icon").click()
        poco("com.vanke.wyguide:id/logoutBtn").click()
        login = poco("android.widget.Button").get_text()
        assert_equal("登 录", login, "登出1_.")
    #开始工作后退出登录
    else:
        poco("com.vanke.wyguide:id/titleTv").click()
        poco("com.vanke.wyguide:id/navigation_dashboard").child("com.vanke.wyguide:id/icon").click()
        poco("com.vanke.wyguide:id/logoutBtn").click()
        loginout_text=["com.vanke.wyguide:id/alertTitle","android:id/button2","android:id/button1"]
        assert_equal("退出登录",poco(loginout_text[0]).get_text())
        assert_equal("取消",poco(loginout_text[1]).get_text())
        assert_equal("确定",poco(loginout_text[2]).get_text())
        #先点取消按钮
        poco(loginout_text[1]).click()
        assert_equal("退出登录",poco("com.vanke.wyguide:id/logoutBtn").get_text(),"取消退出登录")
        #确定退出登录
        poco("com.vanke.wyguide:id/logoutBtn").click()
        poco(loginout_text[2]).click()
        login = poco("android.widget.Button").get_text()
        assert_equal("登 录", login, "登出1_.")

#通过判断一下元素是否存在，来判断是否处于登录状态
if poco("com.vanke.wyguide:id/navigation_dashboard"):
    #元素存在，处于登录状态
    login_out(poco)

else:
    #元素不存在，不处于登录状态
    try:
        login(poco, login_data)
    except Exception as ex:
        raise ex
    #退出try语句总会执行程序
    finally:
        login_out(poco)










