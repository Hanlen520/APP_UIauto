import sys
sys.path.append("E:\F\zhangwk02\APP_UIauto\page_obj")
from reportPage import reportPage
from airtest.core.api import *
import sys
sys.path.append("E:\F\zhangwk02\APP_UIauto\common")
from catch_error import catch_error
import longin_begin as lb


class report_test(reportPage):

    @catch_error
    def login_work(self,row,a):
        lb.login(row)
        lb.begin_work(a)

    @catch_error
    def click_report(self,titl):
        po = reportPage()
        po.rept_click(titl)
        text_title=po.get_title()
        assert_equal(titl, text_title, "标题栏")

    @catch_error
    def click_project(self,proj_name):
        po = reportPage()
        po.at_project()
        text_seleprj=po.get_prj_select()
        assert_equal("项目选择",text_seleprj,"断言项目栏")
        #选择项目
        po.select_project(proj_name)
        #选择项目后断言信息
        # text_proj_name=po.text_at_proj()
        # assert_equal(proj_name,text_proj_name,"断言选择的项目")

    @catch_error
    def test_task_type(self):
        po=reportPage()
        po.task_click()
        #断言title
        text_title=po.get_title()
        assert_equal("任务类型",text_title,"断言title")


    @catch_error
    def test_select_ptype(self,task_name):
        #选择父任务类型
        po=reportPage()
        po.select_ptype(task_name)

    @catch_error
    def test_sele_task(self,task_name,No,txt_mess):
        #选择任务类型
        po=reportPage()
        po.select_type(task_name,No)
        #断言任务描述
        text_task_mess=po.get_task_mess()
        #assert_equal(txt_mess,text_task_mess,"断言角色描述")
        po.commit()

    #位置
    @catch_error
    def test_positon(self,position_mess):
        po=reportPage()
        po.position_click(position_mess)

    #期望时间
    @catch_error
    def test_excp_time(self):
        po=reportPage()
        po.exception_time()
        po.sub_continue()
        #选择时间弹框，断言title
        selectt_text=po.get_selett_tile()
        assert_equal("选择时间",selectt_text)
        po.sub_continue()

    @catch_error
    #员工
    def test_Employee(self):
        po=reportPage()
        po.Employee()

    #所在网格
    @catch_error
    def at_grid(self):
        po=reportPage()
        po.unit_now()
        #断言title
        grid_tile=po.get_title()
        assert_equal("所在网格",grid_tile,"断言网格title")
        po.unit_now1()
        #断言房屋与元素不存在
        contas_name=po.get_hskeeper()
        assert_equal("网格管家",contas_name)

    @catch_error
    #住户
    def test_Households(self):
        po=reportPage()
        po.Households()

    @catch_error
    def test_house(self,h1,h2):
        po=reportPage()
        po.select_house(h1)
        #断言title
        house_title=po.get_prj_select()
        assert_equal("选择房屋", house_title, "断言房屋title")
        po.select_house_No(h2)
        assert_equal("选择房屋", house_title, "断言房屋title")

    @catch_error
    def test_Contacts(self,name):
        po=reportPage()
        po.Contacts(name)

    @catch_error
    def test_con_phone(self,number):
        po=reportPage()
        po.con_phone(number)

    @catch_error
    #选择图片，后续完善断言
    def test_add_pic(self,n):
        po=reportPage()
        po.picture()
        po.select_picture(n)
        po.select_done()

    @catch_error
    def test_description(self,text_data):
        po=reportPage()
        po.text_area(text_data)
        po.commit()
        sleep(1)
        #报事儿完成，回到主界面，断言
        text_report=po.get_rept_txt()
        sleep(1)
        assert_equal("报事",text_report,"报事儿成功，断言回到主界面")







