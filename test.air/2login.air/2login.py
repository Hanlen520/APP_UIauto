# coding=utf-8

import time
from airtest.core.api import *
import sys
sys.path.insert(1, "E:\F\zhangwk02\APP_UIauto\common")
from read_xls import read_xls

login_data=read_xls("test_data.xlsx")

auto_setup(__file__)
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(force_restart=False)



poco("com.vanke.wyguide:id/et_username").set_text(login_data[0][0])
poco("com.vanke.wyguide:id/et_password").set_text(login_data[0][1])
poco("android.widget.Button").click()
sleep(1)
a=poco("com.vanke.wyguide:id/titleRb").get_text()
assert_equal("张文凯的工作台", a, "登录成功.")
