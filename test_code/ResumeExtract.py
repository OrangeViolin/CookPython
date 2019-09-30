# -*- coding: UTF-8 -*-

import pandas as pd
import os
# for info in os.listdir('/Users/caibaomei/Downloads/board'):
#   domain = os.path.abspath('/Users/caibaomei/Downloads/board')
#   file_path = os.path.join(domain,info)
#   pd.read_json(file_path,orient='index')
#   json_framedata = pd.read_json(file_path,orient='index')
#   print(json_framedata)

# 用 pandas 读取 json 数据

domain = os.path.abspath(r'/Users/caibaomei/CookPython/test_code/board')  #读取文件的路径
print(domain)
file_names = os.listdir('/Users/caibaomei/CookPython/test_code/board') #读取文件的名字
for info in file_names:
    file_path = os.path.join(domain, info) #把文件的名字和文件路径合并起来
    global json_framedata
    json_framedata = pd.read_json(file_path, orient='index', typ='frame')
    print(json_framedata)

json_framedata.loc['code']
json_framedata.loc['directors']