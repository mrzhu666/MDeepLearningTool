import smtplib
from email.mime.text import MIMEText

def send(title='title',text="content"):
    #服务器地址
    mail_host = 'smtp.qq.com'  
    #用户名
    mail_user = '1052712811@qq.com'
    #密码(部分邮箱为授权码) 
    mail_pass = 'aokfqvepblnrbfce'
    #邮件发送方邮箱地址
    sender = '1052712811@qq.com'
    #邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
    receivers = ['mrzhu_work@outlook.com']

    #设置email信息
    #邮件内容设置
    message = MIMEText(text,'plain','utf-8')
    #邮件主题       
    message['Subject'] = title
    #发送方信息
    message['From'] = sender 
    #接受方信息     
    message['To'] = receivers[0]  


    #登录并发送邮件
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host)
        #登录到服务器
        smtpObj.login(mail_user,mail_pass) 
        #发送
        smtpObj.sendmail(
            sender,receivers,message.as_string()) 
        #退出
        smtpObj.quit() 
        print('success')
    except smtplib.SMTPException as e:
        print('error',e) #打印错误

if __name__=='__main__':
    main()