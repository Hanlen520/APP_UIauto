import os

def run_bat():
    path=os.path.dirname(__file__)
    #显示当前目录下的所有文件和文件夹
    file_name = os.listdir(os.path.join(path,"test.air"))
    for i in file_name:
        run_command="airtest run E:\F\zhangwk02\APP_UIauto\\test.air\\"+i+" --device Android:///T7G5T15A28000712 --log E:\F\zhangwk02\APP_UIauto\log"
        try:
            os.system(run_command)
            print(i+'-----success!!!')
        except Exception as ex:
            print(i+'---error:',ex)
    try:
        report_command="airtest report E:\F\zhangwk02\APP_UIauto\\test.air" \
                   " --log_root E:\F\zhangwk02\APP_UIauto\log --outfile E:\F\zhangwk02\APP_UIauto\\report\log.html --lang zh"
        os.system(report_command)
    except Exception as e:
        print("report-----error:",e)

run_bat()
