```angular2
SAI:
    evilfile:恶意附件存储路径。
    deformation.txt:畸形链接文件，不清空文件内容。
    output_phishing_link.txt：检测完成后生成的钓鱼链接文件。每次检测前会清空该文件内容。
    output_Suspicious_domain_link.txt：检测完成后生成的可疑域名链接文件。每次检测前会清空该文件内容。
    Personal_information_generation.py：生成敏感信息。
    Phishing_link.py：拉取链接，链接检测。
    phishing_link.txt：拉取"https://openphish.com/feed.txt"中的链接，将链接写入该文件。
    send_stmp.py：邮件发送。

Phishing_link.py：
    links()函数中，拉取链接时需要代理去拉取，注意本机的代理端口是否需要修改。
    Phishing_link()函数中，每次检测链接时会清空上次检测结果。
    
send_stmp.py：
    邮件发送JOB，发送SAI不同风险类型的JOB，目前需手动调整不同类型的邮件内容，还需优化。
    
send_kafka_risk.py：
    生成不同类型的邮件风险，直接往kafka写风险数据。
```