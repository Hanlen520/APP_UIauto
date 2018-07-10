from page_obj.messagePage import mesPage
from airtest.core.api import *
import sys
sys.path.append("E:\F\zhangwk02\APP_UIauto\common")
from catch_error import catch_error

class message_test():
    @catch_error
    def mess_in_action(self):
        po=mesPage()
        po.mess_in()
        mess_text=po.get_mess()
        assert_equal("消息",mess_text,"消息栏1")
        search_text=po.get_search()
        assert_equal("搜索",search_text,"搜素框")
        add_ement=po.get_add()
        assert_equal(True,add_ement,"加号")

    @catch_error
    def search_action(self):
        po=mesPage()
        po.mess_search()
        searching_text=po.get_searching()
        assert_equal("搜索",searching_text,"搜索中")
        clear_ement=po.get_clear_input()
        assert_equal(True,clear_ement,"判断是否存在")
        cancle_text=po.get_cancle()
        assert_equal("取消",cancle_text,"取消")
        po.mess_cancle()
        search_text=po.get_search()
        assert_equal("搜索",search_text,"返回搜索页面")

    @catch_error
    def search_text(self):
        po=mesPage()
        po.mess_search()
        po.mess_input_text()
        searching_text=po.get_searching()
        assert_equal(po.searching_data,searching_text,"输入文字搜索")
        po.mess_clear()
        searching_text1=po.get_searching()
        assert_equal("搜索",searching_text1,"清除后搜索")
        po.mess_cancle()
        assert_equal(True,po.get_add(),"判断加号存在")

    @catch_error
    def cancle_search(self):
        po=mesPage()
        po.mess_search()
        po.mess_input_text()
        po.mess_cancle()
        assert_equal(True, po.get_add(), "判断加号存在")

    @catch_error
    def add_action(self):
        po=mesPage()
        po.mess_add()
        group_chat_text=po.get_group_chat()
        contacts_text=po.get_Contacts()
        assert_equal(group_chat_text,"发起群聊","断言群聊")
        assert_equal(contacts_text,"通讯录  ","断言通讯录")
        po.mess_add_touch()
        assert_equal(False,po.get_contacts(),"再次点击加号，断言通讯录弹框不存在")

run_mess=message_test()
run_mess.mess_in_action()
run_mess.search_action()
run_mess.search_text()
run_mess.cancle_search()
run_mess.add_action()

# class clsTest():
#     y = '322'
#     z='z1'
#
#     def __init__(self):
#         self.y = '你'
#
#     def test_z(self):
#         self.z="11"
#
#
# x = clsTest
# print(x.z)
#
# m = clsTest()
# print(m.z)