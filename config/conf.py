"""
------------------------------------
@Time :
@Auth :
@File : conf.py
@IDE  : PyCharm
@Motto:
------------------------------------
"""
from datetime import datetime
import os

# 项目根目录
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 报告目录
REPORT_DIR = os.path.join(ROOT_DIR, 'report')
# ui对象库config.ini文件所在目录
CONF_PATH = os.path.join(ROOT_DIR, 'config', 'config.ini')
# 测试数据所在目录
DATA_Path = os.path.join(ROOT_DIR, 'data', 'tcData.xlsx')
# 当前时间
CURRENT_TIME = datetime.now().strftime('%H_%M_%S')

# 邮件配置信息
# 邮件服务器
SMTP_SERVER = 'smtp.qq.com1111'
# 发送者
FROM_USER = '账号@qq.com1111'
# 发送者密码
FROM_PASSWORD = 'mhxvqpewblldbjhf11111'
# 接收者
TO_USER = ['账号@qq.com11111']  # 可以同时发送给多人，追加到列表中
# 邮件标题
SUBJECT = 'xx项目自动化测试报告'
# 邮件正文
CONTENTS = '测试报告正文'
# 报告名称
HTML_NAME = 'testReport{}.html'.format(CURRENT_TIME)

# print(HTML_NAME)
# print(CONF_PATH)
# print(os.path.abspath(__file__))