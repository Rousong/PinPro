#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os

from tkinter import *
from tkinter.font import Font
from tkinter.ttk import *
from tkinter.messagebox import *
import coreapi

class Application_ui(Frame):
    #这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('熊猫上传')
        self.master.geometry('537x384')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.Command1Var = StringVar(value='执行上传')
        self.style.configure('TCommand1.TButton', font=('宋体',9))
        self.Command1 = Button(self.top, text='执行上传', textvariable=self.Command1Var, command=self.Command1_Cmd, style='TCommand1.TButton')
        self.Command1.setText = lambda x: self.Command1Var.set(x)
        self.Command1.text = lambda : self.Command1Var.get()
        self.Command1.place(relx=0.089, rely=0.771, relwidth=0.806, relheight=0.148)

        self.tagsVar = StringVar(value='')
        self.tags = Entry(self.top, textvariable=self.tagsVar, font=('宋体',9))
        self.tags.setText = lambda x: self.tagsVar.set(x)
        self.tags.text = lambda : self.tagsVar.get()
        self.tags.place(relx=0.268, rely=0.583, relwidth=0.628, relheight=0.086)

        self.boardIDVar = StringVar(value='')
        self.boardID = Entry(self.top, textvariable=self.boardIDVar, font=('宋体',9))
        self.boardID.setText = lambda x: self.boardIDVar.set(x)
        self.boardID.text = lambda : self.boardIDVar.get()
        self.boardID.place(relx=0.611, rely=0.438, relwidth=0.091, relheight=0.086)

        self.boardcheckVar = IntVar(value=0)
        self.style.configure('Tboardcheck.TCheckbutton', font=('宋体',9))
        self.boardcheck = Checkbutton(self.top, text='是否添加到分类', variable=self.boardcheckVar, style='Tboardcheck.TCheckbutton')
        self.boardcheck.setValue = lambda x: self.boardcheckVar.set(x)
        self.boardcheck.value = lambda : self.boardcheckVar.get()
        self.boardcheck.place(relx=0.06, rely=0.458, relwidth=0.374, relheight=0.044)

        self.style.configure('T安全项.TLabelframe', font=('宋体',9))
        self.style.configure('T安全项.TLabelframe.Label', font=('宋体',9))
        self.安全项 = LabelFrame(self.top, text='安全项', style='T安全项.TLabelframe')
        self.安全项.place(relx=0.045, rely=0., relwidth=0.881, relheight=0.419)

        self.Label5Var = StringVar(value='标签')
        self.style.configure('TLabel5.TLabel', anchor='w', font=('宋体',9))
        self.Label5 = Label(self.top, text='标签', textvariable=self.Label5Var, style='TLabel5.TLabel')
        self.Label5.setText = lambda x: self.Label5Var.set(x)
        self.Label5.text = lambda : self.Label5Var.get()
        self.Label5.place(relx=0.045, rely=0.583, relwidth=0.196, relheight=0.086)

        self.Label4Var = StringVar(value='分类ID')
        self.style.configure('TLabel4.TLabel', anchor='w', font=('宋体',9))
        self.Label4 = Label(self.top, text='分类ID', textvariable=self.Label4Var, style='TLabel4.TLabel')
        self.Label4.setText = lambda x: self.Label4Var.set(x)
        self.Label4.text = lambda : self.Label4Var.get()
        self.Label4.place(relx=0.507, rely=0.458, relwidth=0.076, relheight=0.065)

        self.Label1Var = StringVar(value='网站地址')
        self.style.configure('TLabel1.TLabel', anchor='w', font=('宋体',9))
        self.Label1 = Label(self.安全项, text='网站地址', textvariable=self.Label1Var, style='TLabel1.TLabel')
        self.Label1.setText = lambda x: self.Label1Var.set(x)
        self.Label1.text = lambda : self.Label1Var.get()
        self.Label1.place(relx=0.034, rely=0.199, relwidth=0.104, relheight=0.106)

        self.Label3Var = StringVar(value='密码')
        self.style.configure('TLabel3.TLabel', anchor='w', font=('宋体',9))
        self.Label3 = Label(self.安全项, text='密码', textvariable=self.Label3Var, style='TLabel3.TLabel')
        self.Label3.setText = lambda x: self.Label3Var.set(x)
        self.Label3.text = lambda : self.Label3Var.get()
        self.Label3.place(relx=0.034, rely=0.745, relwidth=0.087, relheight=0.106)

        self.Label2Var = StringVar(value='用户名')
        self.style.configure('TLabel2.TLabel', anchor='w', font=('宋体',9))
        self.Label2 = Label(self.安全项, text='用户名', textvariable=self.Label2Var, style='TLabel2.TLabel')
        self.Label2.setText = lambda x: self.Label2Var.set(x)
        self.Label2.text = lambda : self.Label2Var.get()
        self.Label2.place(relx=0.034, rely=0.447, relwidth=0.104, relheight=0.155)

        self.urlVar = StringVar(value='https://bizhi.art/api/v2/docs')
        self.url = Entry(self.安全项, textvariable=self.urlVar, font=('宋体',9))
        self.url.setText = lambda x: self.urlVar.set(x)
        self.url.text = lambda : self.urlVar.get()
        self.url.place(relx=0.186, rely=0.149, relwidth=0.746, relheight=0.205)

        self.usernameVar = StringVar(value='')
        self.username = Entry(self.安全项, textvariable=self.usernameVar, font=('宋体',9))
        self.username.setText = lambda x: self.usernameVar.set(x)
        self.username.text = lambda : self.usernameVar.get()
        self.username.place(relx=0.186, rely=0.447, relwidth=0.408, relheight=0.155)

        self.passwordVar = StringVar(value='')
        self.password = Entry(self.安全项, textvariable=self.passwordVar, font=('宋体',9))
        self.password.setText = lambda x: self.passwordVar.set(x)
        self.password.text = lambda : self.passwordVar.get()
        self.password.place(relx=0.186, rely=0.696, relwidth=0.408, relheight=0.155)


class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)

    def upload(self):
        auth = coreapi.auth.BasicAuthentication(self.usernameVar.get(), self.passwordVar.get())  # 上传需要用户验证 填写你的用户名和密码
        client = coreapi.Client(auth=auth)
        schema = client.get(self.urlVar.get())  # API文档
        ADD_TO_BOARD = self.boardcheckVar.get()
        BOARD_ID = self.boardIDVar.get()  # 要添加到哪个分类ID下
        tags = self.tagsVar.get()
        tagsList = tags.split(" ")

        # Interact with the API endpoint
        action = ["pins", "create"]
        params = {
            "private": False,
            "check": 1,  # 默认是已经审核
            "url": "",  # 这里填写图片的url
            "description": "",
            "referer": "",
            "tags": tagsList,  # 这里是标签，需要列表格式
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
            f.write(url)  # 追加写入本次的新url
            params["url"] = url
            pinResult = client.action(schema, action, params=params)
            print("成功添加新的图片，ID为{}".format(pinResult['id']))
            if ADD_TO_BOARD == 1:
                boardParams["pins_to_add"] = [pinResult['id']]
                boardResult = client.action(schema, addToBoard, params=boardParams)
                print("成功把ID为{}的图片添加到分类".format(pinResult['id']))

        f.close()
        new_f.close()

    def Command1_Cmd(self, event=None):
        self.upload()


if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()

