#!/usr/bin/env python
# encoding=utf-8
# -*- coding: UTF-8 -*-
import os
import smtplib
import zipfile
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def mail():
    print ("log----send email ");
    global ret
    try:
        # ret == True
        message = MIMEMultipart()
        message['From'] = Header("自动发包脚本", 'utf-8')
        message['To'] = Header("测试", 'utf-8')
        subject = 'Python SMTP 邮件测试'
        message['Subject'] = Header(subject, 'utf-8')
        message.attach(MIMEText('这是吴焱的Python 邮件发送测试……附件为极速钱包apk的包', 'plain', 'utf-8'))
        att1 = MIMEText(
            open('E:/kdlc_apk_packaged/KDLC_apk/KDLC_Apk/kdlc_apk_signd_taged/testapk.zip','rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att1["Content-Disposition"] = 'attachment; filename="apk.zip"'
        message.attach(att1)

        server = smtplib.SMTP_SSL("smtp.qq.com", "465")  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], message.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接

    except Exception,e:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        print e
        ret == False
    return ret


def buildAPk():
    print("log----build apk")
    # os.system("E:")
    # os.system('cd E:\\MySpace\\koudailicai\\koudaiStudio')
    # os.system('gradlew assemblerelease')
    os.chdir(r'E:\\MySpace\\koudailicai\\koudaiStudio')
    os.system('gradlew assemblerelease')


def zip_dir(dirname, zipfilename):
    filelist = []
    if os.path.isfile(dirname):
        filelist.append(dirname)
    else:
        for root, dirs, files in os.walk(dirname):
            for name in files:
                filelist.append(os.path.join(root, name))

    zf = zipfile.ZipFile(zipfilename, "w", zipfile.zlib.DEFLATED)
    for tar in filelist:
        arcname = tar[len(dirname):]
        zf.write(tar, arcname)
    zf.close()


my_sender = '1402575386@qq.com'  # 发件人邮箱账号
my_pass = 'fkbrlcbviuzvfgif'  # 发件人邮箱密码
my_user = 'ke11839@163.com'  # 收件人邮箱账号，我这边发送给自己

buildAPk()
zip_dir("E:/kdlc_apk_packaged/KDLC_apk/KDLC_Apk/kdlc_apk_signd_taged/testapk",
        "E:/kdlc_apk_packaged/KDLC_apk/KDLC_Apk/kdlc_apk_signd_taged/testapk.zip")
ret = True
ret = mail()
if ret:
    print("log----send email succeed")
else:
    print("log----send email error")