import coreapi

# Initialize a client & load the schema document
auth = coreapi.auth.BasicAuthentication("user", "password")  # 上传需要用户验证 填写你的用户名和密码
client = coreapi.Client(auth=auth)
schema = client.get("http://127.0.0.1:8000/api/v2/docs")  # API文档

# Interact with the API endpoint
action = ["pins", "create"]
params = {
    "private": False,
    "check": 1, # 默认是已经审核
    "url": "", # 这里填写图片的url
    "description": "",
    "referer": "",
    "tags": ["xx", "xxx"], # 这里是标签，需要列表格式
}
result = client.action(schema, action, params=params)
print(result)
