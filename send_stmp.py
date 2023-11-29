import os
import smtplib
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from Personal_information_generation import generate_random_phone_number,generate_random_id
import string
import base64


# 读取txt文件内容并存储到列表中
file_path = "deformation.txt"
with open(file_path, "r") as file:
    lines = file.readlines()
    api_names = [line.strip() for line in lines]


def directory_path():
    attachment_directory = "E:\\项目\\PRS-NTA\\job\\tophant\\SAI\\evilfile"
    file_name_list = os.listdir(attachment_directory)
    random_element = random.choice(file_name_list)
    return random_element


def generate_random_string(length):
    # 生成随机字符串
    characters = string.ascii_lowercase + string.digits
    random_str = ''.join(random.choice(characters) for _ in range(length))
    return random_str


def send_smtp_msg(index,links,file_names):
    # 邮件服务器信息
    smtp_server = '10.0.80.231'
    smtp_port = 25
    smtp_username = 'xuxu@tthant.cn'
    # smtp_username = generate_random_string(128) + '@tthant.cn'
    smtp_password = 'tophant123'
    to_username = 'qinghua@tthant.cn'

    # 构建邮件内容
    message = MIMEMultipart()
    message['From'] = f'xuxu{index}@tthant.cn'
    print(message['From'])
    message['To'] = to_username
    message['Subject'] = f'这是第{index}敏感信息数据'

    phone = generate_random_phone_number()
    ID_card = generate_random_id()
    # 邮件正文
    # body = f"请前往：{links}\n联系电话：{phone}\n身份证号：{ID_card}"
    body = f"联系电话：{phone}\n身份证号：{ID_card}"
    # body = f"尊敬的用户您好：\n\t感谢您一直以来的支持！"
    message.attach(MIMEText(body, 'plain'))

    # 添加附件
    send_file = False
    if send_file == True:
        with open(os.path.join(path, file_names), "rb") as attachment_file:
            attachment = MIMEApplication(attachment_file.read())
            attachment.add_header('Content-Disposition', f'attachment; filename="{file_names}"')
            message.attach(attachment)

    # 连接到SMTP服务器
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.connect(smtp_server,smtp_port)
    server.ehlo()
    # 指定认证方式为AUTH LOGIN
    server.docmd(f"AUTH LOGIN {base64.b64encode(smtp_username.encode()).decode()}")
    server.docmd(f"{base64.b64encode(smtp_password.encode()).decode()}")

    # 不指定认证方式，使用默认认证方式为AUTH PLAIN
    # server.login(smtp_username, smtp_password)

    # 发送邮件
    server.sendmail(smtp_username, to_username, message.as_string())
    # 关闭连接
    server.quit()

if __name__ == '__main__':
    for index,link in enumerate(api_names):
        path = "E:\\项目\\PRS-NTA\\job\\tophant\\SAI\\evilfile"
        # file_names =  path + directory_path()
        file_names = directory_path()
        index = index + 1
        send_smtp_msg(index,link,file_names)