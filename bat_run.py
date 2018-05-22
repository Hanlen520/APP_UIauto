import os

path=os.path.dirname(__file__)
#显示当前目录下的所有文件和文件夹
file_name = os.listdir(os.path.join(path,"test.air"))

command_contet=[]
for i in file_name:
    command_contet.append("airtest run E:\F\zhangwk02\APP_UIauto\\test.air\\"+i+" --log E:\F\zhangwk02\APP_UIauto\log")


def run_bat(*args):
    for com in args:
        os.system(com)

run_bat(*command_contet)
