import os
import json
def read_json(path="E:\F\zhangwk02\APP_UIauto\data\\report.json",json_name=""):
    with open(path,encoding='utf-8') as f:
        json_data = json.load(f)
        #获取报事儿类型
        content_list=[]
        for i in json_data[json_name]:
            content_list.append(i)

        return content_list

def rept_list(name):
    fl = read_json(json_name=name)
    ttype_ke = []
    ttype_va=[]
    for i in fl:
        for j,k in i.items():
            #任务类型
            ttype_ke.append(j)
            ttype_va.append(k)

    return ttype_ke,ttype_va

def dis_list(name,ty_name):
    a=rept_list(name)
    len=a[0].index(ty_name)
    return a[1][len]



# we=dis_list("报事儿类型","工程")
# for i in we:
#     if isinstance(i,dict):
#         print(list(i.keys())[0])
#         print(list(i.values())[0])
#         print(len(list(i.values())[0]))
#         for j in range(len(list(i.values())[0])):
#             print(j)
#
#

