__author__ = "zhangwk02"
from airtest.core.api import *
import sys

auto_setup(__file__)
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(force_restart=False)

sys.path.insert(1, "E:\F\zhangwk02\APP_UIauto\common")
from read_xls import read_xls

login_data=read_xls("test_data.xlsx")

#通过判断一下元素是否存在，来判断是否处于登录状态
def login(row):
    # 元素存在，处于登录状态
    #if #poco("com.vanke.wyguide:id/navigation_dashboard"):
    if poco("com.vanke.wyguide:id/navigation_dashboard").exists():
        #退出登录
        #poco("com.vane.wyguide:id/navigation_home").click()
        poco("com.vanke.wyguide:id/navigation_dashboard").child("com.vanke.wyguide:id/icon").click()
        poco("com.vanke.wyguide:id/logoutBtn").click()
        if poco("android:id/button1").exists():
            poco("android:id/button1").click()
        #退出登录后，开始重新登录
        poco("com.vanke.wyguide:id/et_username").set_text(login_data[row][0])
        poco("com.vanke.wyguide:id/et_password").set_text(login_data[row][1])
        poco("android.widget.Button").click()
    else:
        poco("com.vanke.wyguide:id/et_username").set_text(login_data[row][0])
        poco("com.vanke.wyguide:id/et_password").set_text(login_data[row][1])
        poco("android.widget.Button").click()

def begin_work(a):
    poco("com.vanke.wyguide:id/titleRb").click()
    for i in a:
        poco("com.vanke.wyguide:id/listView").child("android.widget.LinearLayout")[i].click()
    poco("com.vanke.wyguide:id/startWorkBtn").click()

# login(1)
# begin_work([0,1,2])



