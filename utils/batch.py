import os
import coreapi

# Initialize a client & load the schema document
auth = coreapi.auth.BasicAuthentication("xxxx", "xxxx")  # 上传需要用户验证 填写你的用户名和密码
client = coreapi.Client(auth=auth)
schema = client.get("https://xxxxxx.xyz/api/v2/docs")  # API文档

# Interact with the API endpoint
action = ["pins", "create"]
params = {
    "private": False,
    "check": 1,  # 默认是已经审核
    "url": "",  # 这里填写图片的url
    "description": "",
    "referer": "",
    "tags": ["xx", "xxx"],  # 这里是标签，需要列表格式
}

# 获取绝对路径
path = os.path.abspath(os.path.dirname(__file__))
URL_ROOT = os.path.join(path, 'url.txt')

# 打开文本文件
f = open(URL_ROOT, "rt")

# 循环遍历替换json中的url
for i in f:
    params["url"] = i
    result = client.action(schema, action, params=params)
    print(result)

f.close()
