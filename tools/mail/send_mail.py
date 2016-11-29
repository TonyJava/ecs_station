#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import smtplib
import datetime

from email.mime.text import MIMEText

mailto_list=["yuanyunchao@xiaomi.com","gongbowen@xiaomi.com","lidongmei@xiaomi.com"]
mail_host="mail.xiaomi.com"  #设置服务器
mail_user="robot"    #用户名
mail_pass=""   #口令
mail_postfix="xiaomi.com"  #发件箱的后缀

def send_mail(to_list,sub,content):
    me="hello"+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content,_subtype='plain',_charset='gb2312')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)
        server.login(mail_user,mail_pass)
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception, e:
        print str(e)
        return False

if __name__ == '__main__':
    try :
        file = open("/home/yuanyunchao/mail/mail_content");
    except :
        print "file open error."
    txt = "" ;
    for l in file.readlines():
        if l.startswith("######"):
            break ;
        else :
            txt = txt + l ;
    txt = txt + "\n" + "（自动日报发送脚本测试）" +"\n"
    mail_title = "Daily report from yuanyunchao("+str(datetime.date.today())+")"
    if send_mail(mailto_list,mail_title,txt):
        print "发送成功"
    else:
        print "发送失败"
