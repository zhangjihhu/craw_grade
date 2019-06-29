import requests
from bs4 import BeautifulSoup
import json
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import datetime
import time


# 登录
def login():
    # print("正在登录账号", username)
    url = "http://202.119.112.195/hhu/login.action"
    username = "your user name"
    password = "your password"
    data = {
        "username": username,
        "password": password,
        "x": "30",
        "y": "18"
    }
    response = requests.post(url=url, data=data)
    return response.cookies


# 获取成绩页面
def get_grade():
    url = "http://202.119.112.195/hhu/jsp/train/getSorceDetail.action"
    referer = "http://202.119.112.195/hhu/jsp/train/initSorceDetail.action?actType=1"
    data = {
        "xsid": "181307040035"
    }
    cookies = login()
    response = requests.post(url=url, data=data, headers={"Referer": referer}, cookies=cookies)
    return json.loads(response.text)["tableHtml"]


# 提取出成绩
def format_grade():
    data_list = []
    text = get_grade()
    soup = BeautifulSoup(text, "html.parser")
    for tr in soup.find_all("tr"):
        td = tr.find_all("td")
        data_list.append({
            # "编号": td[0].contents[0],
            # "code": td[1].contents[0],
            "名称": td[2].contents[0],
            "学分": td[4].contents[0],
            "成绩": 0 if len(td[5].contents)==0 else td[5].contents[0]
        })

    return str(data_list)

# 使用邮件发送成绩(若成绩发生更新)
def mail(grade):
    ret = True
    # 发件人邮箱账号和密码
    my_sender = '****@qq.com'
    my_pass = '********'
    # 收件人邮箱账号
    my_user = '1325626881@qq.com'
    try:
        msg = MIMEText(grade, 'plain', 'utf-8')
        # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['From'] = formataddr(["zhangji", my_sender])
        # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['To'] = formataddr(["ji_haha", my_user])
        # 邮件的主题，也可以说是标题
        msg['Subject'] = "python grade"

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:
        ret = False
    return ret


if __name__ == '__main__':
    grade = ""
    while 1:
        grade_result = format_grade()
        if grade != grade_result:
            ret = mail(grade_result)
            i = datetime.datetime.now()
            grade = grade_result
            if ret:
                print(i, " 发送成功")
            else:
                print(i, " 发送失败")
        else:
            time.sleep(7200)

