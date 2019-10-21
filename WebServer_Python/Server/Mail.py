# -*- coding:utf-8 -*-
import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json


def MySendMail(to_email, title, content):
    with open("config.json", "r") as f:
        configDic = json.load(f)

    if 'Account' not in configDic or 'PassWord' not in configDic:
        print("配置文件错误")
        return
    EMAIL_FROM = configDic['Account']  # 刚才配置的发信地址
    EMAIL_HOST_PASSWORD = configDic['PassWord']  # 密码
    EMAIL_HOST, EMAIL_PORT = configDic['Host'], int(configDic['Port'])
    # 自定义的回复地址
    replyto = EMAIL_FROM
    msg = MIMEMultipart('alternative')
    msg['Subject'] = title
    msg['From'] = '%s <%s>' % ("admin", EMAIL_FROM)
    msg['To'] = '%s <%s>' % ("client", to_email)

    msg['Reply-to'] = replyto
    msg['Message-id'] = email.utils.make_msgid()
    msg['Date'] = email.utils.formatdate()
    textplain = MIMEText('{}'.format(content), _subtype='plain', _charset='UTF-8')
    msg.attach(textplain)

    try:
        client = smtplib.SMTP()
        client.connect(EMAIL_HOST, EMAIL_PORT)
        # 开启DEBUG模式
        client.set_debuglevel(0)
        client.login(EMAIL_FROM, EMAIL_HOST_PASSWORD)
        client.sendmail(EMAIL_FROM, [to_email], msg.as_string())
        client.quit()
        return True
    except smtplib.SMTPConnectError as e:
        error_msg = '邮件发送失败，连接失败'
    except smtplib.SMTPAuthenticationError as e:
        error_msg = '邮件发送失败，认证错误:'
    except smtplib.SMTPSenderRefused as e:
        error_msg = '邮件发送失败，发件人被拒绝:'
    except smtplib.SMTPRecipientsRefused as e:
        error_msg = '邮件发送失败，收件人被拒绝:'
    except smtplib.SMTPDataError as e:
        error_msg = '邮件发送失败，数据接收拒绝:'
    except smtplib.SMTPException as e:
        error_msg = '邮件发送失败, {}'.format(e.message)
    except Exception as e:
        error_msg = '邮件发送异常, {}'.format(str(e))
    print(error_msg)
    return False


if __name__ == '__main__':
    MySendMail("906747215@qq.com", "test", "test")
