import os
import yagmail
import sys
sys.path.append("E:\F\zhangwk02\APP_UIauto\common")
from catch_error import catch_error

@catch_error
def run_bat():
    path=os.path.dirname(__file__)
    #显示当前目录下的所有文件和文件夹
    file_name = os.listdir(os.path.join(path,"test.air"))
    #设备ID
    #device_id=os.system("adb devices")
    for i in file_name:
        log_path="E:\F\zhangwk02\APP_UIauto\log\\"+i
        report_path="E:\F\zhangwk02\APP_UIauto\\report\\"+i
        folder_log=os.path.exists(log_path)
        folder_report=os.path.exists(report_path)
        if not folder_log:
            log_path=os.makedirs("log\\"+i)
        if not folder_report:
            report_path=os.makedirs("report\\"+i)

        # run_command="airtest run E:\F\zhangwk02\APP_UIauto\\test.air\\"+i+" --device Android:///2e6e029 --log E:\F\zhangwk02\APP_UIauto\log"
        #
        # report_command =P_UIauto\\test.air\\"+i+" --device Android:///2e6e029 --log E:\F\zhangwk02\APP_UIauto\log\path"

        run_command = "airtest run E:\F\zhangwk02\APP_UIauto\\test.air\\" + i + " --device Android:///2e6e029 --log "+log_path

        report_command = "airtest report E:\F\zhangwk02\APP_UIauto\\test.air\\"+i+\
                         " --log_root "+ log_path +" --outfile "+ report_path+"\log.html --lang zh"
        try:
            os.system(run_command)
            os.system(report_command)
            print(i+'-----success!!!')
        except Exception as ex:
            print(i+'---error:',ex)
    # try:
    #     report_command="airtest report  --export E:\F\zhangwk02\APP_UIauto\\report E:\F\zhangwk02\APP_UIauto\\test.air" \
    #                " --log_root E:\F\zhangwk02\APP_UIauto\log --outfile E:\F\zhangwk02\APP_UIauto\\report\log.html --lang zh"
    #     os.system(report_command)
    # except Exception as e:
    #     print("report-----error:",e)

@catch_error
def send_mail():
    # 链接邮箱服务器
    yag = yagmail.SMTP(user="1627894439@qq.com", password="ohytilmbcckedajj", host='smtp.qq.com')

    # 邮箱正文
    contents = ['安卓自动化测试报告']

    # 发送邮件
    #yag.send('zhangwk02@vanke.com', '测试报告', contents)
    #带附件发送
    yag.send(['zhangwk02@vanke.com','v-yangl81@vanke.com'], '测试报告', contents, ["E:\F\zhangwk02\APP_UIauto\log\log.txt", "E:\F\zhangwk02\APP_UIauto\\report\log.html"])

run_bat()
#send_mail()