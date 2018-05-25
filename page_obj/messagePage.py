from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(force_restart=False)

#消息栏页面对象
class mesPage(object):
    #底部标签栏，消息栏元素
    mes_bottom=('消息')
    #搜索框
    search=("com.vanke.wyguide:id/im_search")
    search_txt="搜索"
    #点击后的搜索框
    searching=("com.vanke.wyguide:id/ac_et_search")
    searching_data="测试aaaaaa"
    #清除
    clear=("com.vanke.wyguide:id/clear_input")
    #取消
    cancle=("com.vanke.wyguide:id/ac_iv_press_back")

    #加号
    add=("com.vanke.wyguide:id/more_im")
    add1=(Template(r"tpl1527220902576.png", record_pos=(0.427, -0.746), resolution=(1080, 1920)))
    group_chat=("发起群聊")
    Contacts=("通讯录  ")

    #将每个元素的操作封装成功一个方法
    def mess_in(self):
        poco(text=self.mes_bottom).click()

    def mess_search(self):
        poco(self.search).click()

    def mess_searching(self):
        poco(self.searching).click()

    def mess_input_text(self):
        poco(self.searching).set_text(self.searching_data)

    def mess_clear(self):
        poco(self.clear).click()

    def mess_cancle(self):
        poco(self.cancle).click()

    def mess_add(self):
        poco(self.add).click()

    def mess_add_touch(self):
        touch(self.add1)

    def mess_group_chat(self):
        poco(text=self.group_chat).click()

    def mess_Contacts(self):
        poco(text=self.Contacts).click()

    def get_mess(self):
        return poco(text=self.mes_bottom).get_text()

    def get_search(self):
        return poco(text=self.search_txt).get_text()

    def get_searching(self):
        return poco(self.searching).get_text()

    def get_clear_input(self):
        return poco(self.clear).exists()

    def get_cancle(self):
        return poco(self.cancle).get_text()

    def get_add(self):
        return poco(self.add).exists()

    def get_group_chat(self):
        return poco(text=self.group_chat).get_text()

    def get_Contacts(self):
        return poco(text=self.Contacts).get_text()

    def get_contacts(self):
        return poco(text=self.Contacts).exists()





