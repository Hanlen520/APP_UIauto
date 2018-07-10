from page_obj.rep_page import report_test
from  common.read_json import *
import random

test = report_test()
#1.开始工作
test.login_work(2,(0,1))
#2.报事儿
for task in rept_list("报事儿类型")[0]:
    test.click_report(task)
    #2.1.所在项目
    for index2, prj in enumerate(rept_list("所在项目")[0]):
        test.click_project(prj)
        #2.2任务类型
        test.test_task_type()
        #获取子任务类型
        sub_task_tyep=dis_list("报事儿类型", task)
        for index3, sub_list in enumerate(sub_task_tyep):
            #判断 sub_list是否有子列表
            if isinstance(sub_list,dict):
                #获取字典的键
                sub_keys=list(sub_list.keys())[0]
                #循环遍历子任务类型
                for value_index in range(len(list(sub_list.values())[0])):
                    test.test_sele_task(sub_keys,value_index,'此任务有以下岗位"安全主管/客服主管/环境主管/环境监控"可在抢单池强单')
            else:
                test.test_sele_task(sub_list, 0, '此任务有以下岗位"安全主管/客服主管/环境主管/环境监控"可在抢单池强单')

            #2.3具体位置
            test.test_positon("测试地址")

            #2.4期望处理时间
            test.test_excp_time()

            #2.5.1员工报事儿
            test.test_Employee()
            test.at_grid()

            """
            #2.5.2住户报事儿
            test.test_Households()
            test.test_house("光谷万科中心写字楼","201")

            #联系人、电话
            test.test_Contacts("张邯")
            test.test_con_phone("13213221331")
            """
            #下拉界面
            test.t_swipe()

            #2.6添加照片
            test.test_add_pic(4)

            #2.7描述

            test.test_description('报事test%s' %(random.uniform(1,100)))


                    # if value_index != len(list(sub_list.values())[0]):
                    #     test.click_report(task)

            if index3 != len(sub_task_tyep)-1:
                test.click_report(task)
                test.click_project(prj)
                test.test_task_type()

        if  index2 != len(rept_list("所在项目")[0])-1:
            test.click_report(task)











