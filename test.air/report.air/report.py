from page_obj.rep_page import report_test
from  common.read_json import *
import random
import time

test = report_test()
#1.开始工作
test.login_work(2,(0,1))
#2.报事儿，遍历报事儿类型
for task in rept_list("报事儿类型")[0]:
    test.click_report(task)
    #2.1.所在项目，遍历报事儿项目
    for index2, prj in enumerate(rept_list("所在项目")[0]):
        test.click_project(prj)
        #2.2任务类型
        test.test_task_type()
        #获取子任务类型
        sub_task_tyep=dis_list("报事儿类型", task)
        #遍历任务类型列表
        for index3, sub_list in enumerate(sub_task_tyep):
            #判断 sub_list是否有子列表(任务有子任务)
            if isinstance(sub_list,dict):
                #获取字典的键
                sub_keys=list(sub_list.keys())[0]
                #循环遍历子任务类型
                for value_index in range(len(list(sub_list.values())[0])):

                    test.test_sele_task(sub_keys,value_index,'此任务有以下岗位"安全主管/客服主管/环境主管/环境监控"可在抢单池强单')

                    # 2.3具体位置
                    test.test_positon("测试地址")

                    # 2.4期望处理时间
                    test.test_excp_time()

                    # 2.5.1员工报事儿
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
                    # 下拉界面
                    test.t_swipe()

                    # 2.6添加照片
                    test.test_add_pic(3)

                    # 2.7描述

                    #test.test_description('报事test%s'% (random.uniform(1, 100)))
                    test.test_description('报事test_%s_%s_%s_%s' %(task,prj,sub_keys,list(sub_list.values())[0][value_index]))

                    # if value_index != len(list(sub_list.values())[0]):
                    #     test.click_report(task)

                    if value_index != len(list(sub_list.values())[0]) - 1:
                        test.click_report(task)
                        test.click_project(prj)
                        test.test_task_type()
                        test.test_select_ptype(sub_keys)

                '''
                遍历完子任务类型后，回到主页面。
                点击报事儿，选择报事儿类型——选择项目——选择任务类型
                '''
                test.click_report(task)
                test.click_project(prj)
                test.test_task_type()

            #任务没有子任务
            else:
                test.test_sele_task(sub_list, 0, '此任务有以下岗位"安全主管/客服主管/环境主管/环境监控"可在抢单池强单')

                # 2.3具体位置
                test.test_positon("测试地址")

                # 2.4期望处理时间
                test.test_excp_time()

                # 2.5.1员工报事儿
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
                # 下拉界面
                test.t_swipe()

                # 2.6添加照片
                test.test_add_pic(4)

                # 2.7描述
                #test.test_description('报事test%s' % (random.uniform(1, 100)))
                test.test_description('报事test%s_%s_%s' %(task, prj, sub_keys))

                # if value_index != len(list(sub_list.values())[0]):
                #     test.click_report(task)

                if index3 != len(sub_task_tyep) - 1:
                    test.click_report(task)
                    test.click_project(prj)
                    test.test_task_type()

        if  index2 != len(rept_list("所在项目")[0])-1:
            test.click_report(task)











