# -*- encoding=utf8 -*-
__author__ = "zhangwk02"
import json
from airtest.core.api import *
import sys
sys.path.append("E:\F\zhangwk02\APP_UIauto\common")
from catch_error import catch_error

auto_setup(__file__)
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
global poco
poco = AndroidUiautomationPoco(force_restart=False)


# 展开折叠开始工作列表
@catch_error
def start_working1():
    poco("com.vanke.wyguide:id/titleRb").click()
    #全选
    select=poco("com.vanke.wyguide:id/checkAllBtn").get_text()
    #开始工作
    begin_text=poco("com.vanke.wyguide:id/startWorkBtn").get_text()

    assert_equal("全选", select, "开始工作1.1")
    assert_equal("开始工作", begin_text, "开始工作1.2")

    poco("com.vanke.wyguide:id/listView").child("android.widget.LinearLayout")[0].click()
    assert_exists(Template(r"selected.png", record_pos=(0.424, -0.619), resolution=(1080, 1920)), "勾选第一个岗位")
    #重复点击
    poco("com.vanke.wyguide:id/listView").child("android.widget.LinearLayout")[0].click()
    assert_exists(Template(r"unselect.png", record_pos=(0.424, -0.356), resolution=(1080, 1920)), "取消勾选第一个岗位")
    #折叠列表
    poco("com.vanke.wyguide:id/titleTv").click()
    assert_not_exists(Template(r"unselect.png", record_pos=(0.424, -0.356), resolution=(1080, 1920)), "取消勾选第一个岗位")
    return True


@catch_error
def stw_selct_all():
    poco("com.vanke.wyguide:id/titleRb").click()
    poco("com.vanke.wyguide:id/checkAllBtn").click()
    unselect_text=poco("com.vanke.wyguide:id/checkAllBtn").get_text()
    assert_equal("取消全选",unselect_text,"全选工作岗位")
    #取消全选
    poco("com.vanke.wyguide:id/checkAllBtn").click()
    sele_text=poco("com.vanke.wyguide:id/checkAllBtn").get_text()
    assert_equal("全选",sele_text,"取消全选工作岗位")
    #折叠列表
    poco("com.vanke.wyguide:id/titleTv").click()
    assert_not_exists(Template(r"unselect.png", record_pos=(0.424, -0.356), resolution=(1080, 1920)), "取消勾选第一个岗位")
    return True


@catch_error
def working():
    poco("com.vanke.wyguide:id/titleRb").click()
    #开始工作元素存在
    if poco("com.vanke.wyguide:id/startWorkBtn").get_text()=="开始工作":
        poco("com.vanke.wyguide:id/listView").child("android.widget.LinearLayout")[0].click()
        poco("com.vanke.wyguide:id/listView").child("android.widget.LinearLayout")[1].click()
        #开始工作
        poco("com.vanke.wyguide:id/startWorkBtn").click()
        #再次进入工作台
        poco("com.vanke.wyguide:id/titleRb").click()
        end_work=poco("com.vanke.wyguide:id/finishWorkBtn").get_text()
        change_work=poco("com.vanke.wyguide:id/startWorkBtn").get_text()
        assert_equal("结束工作",end_work,"开始工作断言1")
        assert_equal("岗位切换",change_work,"开始工作断言2")

    elif poco("com.vanke.wyguide:id/finishWorkBtn").get_text()=="结束工作":
        poco("com.vanke.wyguide:id/finishWorkBtn").click()
        #断言结束工作
        cancle=poco("android:id/button2").get_text()
        ok=poco("android:id/button1").get_text()
        assert_equal("取消",cancle,"结束工作断言1")
        assert_equal("确定",ok,"结束工作断言2")
        poco("android:id/button2").click()
        assert_equal("结束工作", poco("com.vanke.wyguide:id/finishWorkBtn").get_text(), "取消结束工作断言1")
        poco("com.vanke.wyguide:id/finishWorkBtn").click()
        poco("android:id/button1").click()
        poco("com.vanke.wyguide:id/titleRb").click()
        assert_equal("开始工作",poco("com.vanke.wyguide:id/startWorkBtn").get_text(),"结束工作")

    poco("com.vanke.wyguide:id/titleTv").click()
    return True

start_working1()
stw_selct_all()
working()
