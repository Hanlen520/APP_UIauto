# -*- encoding=utf8 -*-
__author__ = "zhangwk02"
import json
from airtest.core.api import *

auto_setup(__file__)
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(force_restart=False)

poco("com.vanke.wyguide:id/titleRb").click()
#全选
select=poco("com.vanke.wyguide:id/checkAllBtn").get_text()
#开始工作
begin_text=poco("com.vanke.wyguide:id/startWorkBtn").get_text()

assert_equal("全选", select, "开始工作1.1")
assert_equal("开始工作", begin_text, "开始工作1.2")


