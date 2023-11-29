import requests
import json


def links():
    uri = "https://openphish.com/feed.txt"
    proxy = {
        # 配置代理地址
        "https": "http://127.0.0.1:7890"
    }
    print("开始拉取链接...")
    link = requests.get(uri,proxies=proxy,verify=False)
    link_uri = link.text
    uri_list = link_uri.strip().split('\n')
    # print(uri_list)
    phishing_link = "phishing_link.txt"
    with open(phishing_link, "w") as file:
        file.write(f"{link_uri}\n")
    print(f"拉取链接完成，链接写入到:{phishing_link}文件")


def clear_file_content(filename):
    with open(filename,"w") as file:
        pass

def link_file():
    # 读取txt文件内容并存储到列表中
    file_path = "phishing_link.txt"
    with open(file_path, "r") as file:
        lines = file.readlines()
        api_names = [line.strip() for line in lines]
    return api_names


def Phishing_link():
    print(f"开始检测链接...")
    uri = "http://10.0.80.67/mail-cloud/linkCheck/processCheckLink"
    # 钓鱼链接输出文件
    output_phishing_link = "output_phishing_link.txt"
    # 可疑域名链接输出文件
    output_Suspicious_domain_link = "output_Suspicious_domain_link.txt"

    # 设置output文件是否需要被清空标识
    clear_file = False
    if clear_file:
        # 第一次运行时清空
        clear_file_content(output_phishing_link)
        clear_file_content(output_Suspicious_domain_link)
        clear_file = False

    phishing_link_list= []
    Suspicious_domain_link_list = []
    api_names = link_file()
    for index,links in enumerate(api_names):
        # print(f"当前检测的链接为：{links}")
        data = {"link":links,"type":0}
        headers ={
            "Content-Type": "application/json"
        }
        reslut = requests.post(uri,json=data,headers=headers)
        if reslut.status_code == 200:
            res = reslut.text
            # print(res)
            res_data = json.loads(res)
            fish_Score = res_data["data"]["fishScore"]
            malWeb_Score = res_data["data"]["malWebScore"]
            link_Url = res_data["data"]["linkUrl"]

            # 检测是否为可疑域名链接
            if malWeb_Score >= 0.6:
                Suspicious_domain_link_list.append(link_Url)
                # print(f"{malWeb_Score}\t{link_Url}")
                with open(output_Suspicious_domain_link, "a") as file:
                    file.write(f"{link_Url}\n")
                # 检测是否为钓鱼链接
                if fish_Score >= 1.0:
                    phishing_link_list.append(link_Url)
                    print(f"{fish_Score}\t{link_Url}")
                    with open(output_phishing_link, "a") as file:
                        file.write(f"{link_Url}\n")
        else:
            continue

    print(f"链接检测完成：共检测可疑域名链接：{len(Suspicious_domain_link_list)}个,钓鱼链接：{len(phishing_link_list)}个")
    file.close()


if __name__ == '__main__':
    # 获取最新的链接
    # links()
    # 检测链接
    Phishing_link()