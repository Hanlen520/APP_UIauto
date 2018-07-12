from airtest.core.api import *
from page_obj.Base_report import Base
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(force_restart=False)

#消息栏页面对象
class reportPage(Base):

    #将每个元素的操作封装成功一个方法
    #项目
    def rept_click(self,rp_type):
        poco(text=self.rp).click()
        poco(text=rp_type).click()


    def get_rept_txt(self):
        return poco(text=self.rp).get_text()

    def get_title(self):
        return poco(self.title).get_text()

    def at_project(self):
        poco(self.project).click()

    # def text_at_proj(self):
    #     poco(self.project).get_text()

    def select_project(self,prj_name):
        poco(text=prj_name).click()

    def get_prj_select(self):
        return poco(self.project_select).get_text()



#--------------------------------------------------
    #任务
    def task_click(self):
        poco(self.task_type).click()

    #父级别任务
    def select_ptype(self,task_name):
        poco(text=task_name).click()

    def select_type(self,task_name,No):
        poco(text=task_name).click()
        poco(self.single_task[0]).child(self.single_task[1])[No].child(self.single_task[2]).click()

    def task_submit(self):
        poco(self.submit).click()

    def get_task_mess(self):
        return poco(self.task_mess).get_text()
#-------------------------------------------------
    #具体位置
    def position_click(self,position_mess):
        poco(self.position).set_text(position_mess)


#---------------------------------------------------
    #期望时间
    def exception_time(self):
        poco(self.Proce_time).click()
        #poco(text=date).click()

    def sub_continue(self):
        poco(self.contiue).click()

    def get_selett_tile(self):
        return poco(self.selett_title).get_text()

    def cancl(self):
        poco(self.cancle).click()

#-----------------------------------------------------
    #员工
    def Employee(self):
        poco(self.yungong).click()

    def unit_now(self):
        poco(self.unit).click()

    def unit_now1(self):
        poco(self.at_unit).click()

    def get_hskeeper(self):
        return poco(self.handover).get_text()

    #住户
    def Households(self):
        poco(self.zhuhu).click()

    def select_house(self,h1):
        poco(self.house).click()
        poco(text=h1).click()

    def select_house_No(self,h2):
        poco(text=h2).click()

    def Contacts(self,name):
        poco(self.cont_user).set_text(name)

    def con_phone(self,number):
        poco(self.cont_phone).set_text(number)

#-----------------------------------------------
    #添加照片
    def picture(self):
        poco(self.add_pic[0]).child(self.add_pic[1]).click()

    def select_picture(self,n):
        poco(self.select_pic[0]).child(self.select_pic[1])[n].child(self.select_pic[2]).click()

    def select_done(self):
        poco(self.done).click()

#----------------------------------------------
    def t_swipe(self):
        poco(self.yungong).swipe([0.0688, -0.5058])
        sleep(1)
#-----------------------------------------------
    #具体描述
    def text_area(self,text_data):
        poco(self.textarea).set_text(text_data)


#-------------------------------------------------
    #提交报事儿
    def commit(self):
        poco(self.submit).click()







