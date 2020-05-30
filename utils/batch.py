import os
import coreapi

# Initialize a client & load the schema document
auth = coreapi.auth.BasicAuthentication("ceshi1", "qq11111")  # 上传需要用户验证 填写你的用户名和密码
client = coreapi.Client(auth=auth)
schema = client.get("http://127.0.0.1:8000/api/v2/docs")  # API文档

ADD_TO_BOARD = True # 是否加分类的开关 开是True 关闭则是False
BOARD_ID = 20 # 要添加到哪个分类ID下

# Interact with the API endpoint
action = ["pins", "create"]
params = {
    "private": False,
    "check": 1,  # 默认是已经审核
    "url": "",  # 这里填写图片的url
    "description": "",
    "referer": "",
    "tags": ['xx','xx','xx','xx',],  # 这里是标签，需要列表格式
}

# 获取绝对路径
path = os.path.abspath(os.path.dirname(__file__))
OLD_URL_ROOT = os.path.join(path, 'url.txt')
NEW_URL_ROOT = os.path.join(path, 'new_url.txt')

uploaded_url = []
upload_url = []

# 打开旧的文本文件
f = open(OLD_URL_ROOT, "rt")
for x in f:
    uploaded_url.append(x)
f.close()

# 打开新的文本文件
new_f = open(NEW_URL_ROOT, "rt")
for y in new_f:
    if y not in uploaded_url:
        upload_url.append(y)

addToBoard = ["boards", "partial_update"]
boardParams = {"id": "", "pins_to_add": "", 'id': BOARD_ID}

# 追加模式打开旧文本
f = open(OLD_URL_ROOT, "a")

# 循环遍历替换json中的url
for url in upload_url:
    f.write(url) #追加写入本次的新url
    params["url"] = url
    pinResult = client.action(schema, action, params=params)
    print("成功添加新的图片，ID为{}".format(pinResult['id']))
    if ADD_TO_BOARD is True:
        boardParams["pins_to_add"] = [pinResult['id']]
        boardResult = client.action(schema, addToBoard, params=boardParams)
        print("成功把ID为{}的图片添加到分类".format(pinResult['id']))

f.close()
new_f.close()
