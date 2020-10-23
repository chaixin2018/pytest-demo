"""
------------------------------------
@Time :
@Auth :
@File : RunTestCase.py
@IDE  : PyCharm
@Motto:
------------------------------------
"""
import logging
import os
import sys
from datetime import datetime

import pytest
from selenium import webdriver
from time import sleep, ctime
import threading


# from config.conf import ROOT_DIR, HTML_NAME
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CURRENT_TIME = datetime.now().strftime('%H_%M_%S')
HTML_NAME = 'testReport{}.html'.format(CURRENT_TIME)

def main():
    """
    执行的方法可以通过参数灵活多变
    args = ['--reruns', '1', '--html=' + './report/' + HTML_NAME] #执行失败的用例会重新再跑一遍
    args = ['-m', 'not conatctTest', '--html=' + './report/' + HTML_NAME] #执行标记为loginTest的用例 标记可以用and or not连接
    args = ['-s', 'not conatctTest','-n=2', '--html=' + './report/' + HTML_NAME] # 多线程
    """
    if ROOT_DIR not in sys.path:
        sys.path.append(ROOT_DIR)
    # 执行用例
    args = ['-m','Test','--alluredir', "./reportAllure", '--html=' + './report/' + HTML_NAME,  "--capture=sys"] # 生成allure报告 同时生成html报告
    pytest.main(args)
    # terminal 输入
    # allure generate reportAllure/ -o report/html --clean
    cmd = 'allure generate reportAllure/ -o report/html --clean'
    try:
        os.system(cmd)
    except Exception as e:
        logging.error('命令{}执行失败'.format(cmd))
        sys.exit


# def main(browser, search):
#     # print('start:%s' % ctime())
#     # print('browser:%s,' % browser)
#     # if browser == 'ie':
#     #     driver = webdriver.Ie()
#     # elif browser == "chrome":
#     #     driver = webdriver.Chrome()
#     # elif browser == 'ff':
#     #     driver = webdriver.Firefox()
#     # else:
#     #     print("browser 参数有误，只能为ie ，ff，chrome")
#     args = ['-m', 'Test1', '--alluredir', "./reportAllure", '--html=' + './report/' + HTML_NAME,"--capture=sys"]  # 生成allure报告 同时生成html报告
#     pytest.main(args)


if __name__ == '__main__':
    main()

# if __name__ == '__main__':
#     # 启动参数（指定浏览器与百度收缩内容）
#     lists = {'ie': 'threading', 'chrome': 'webdriver', 'ff': 'python'}
#     threads = []
#     files = range(len(lists))
#     print("files",files)
#
#     # 创建线程
#     for browser,search in lists.items():
#         t = threading.Thread(target=main, args=(browser,search))
#         threads.append(t)
#
#     # 启动线程
#     for t in files:
#         threads[t].start()
#     for t in files:
#         threads[t].join()
#     print('end:%s' % ctime())

# if __name__ == '__main__':
#     # 启动参数（指定浏览器与百度收缩内容）
#     threads = []
#     files = range(0,4)
#     print("files",files)
#
#     # 创建线程
#     for i in files:
#         t = threading.Thread(target=main, args=("chrome","search"))
#         threads.append(t)
#
#     # 启动线程
#     for t in files:
#         threads[t].start()
#     for t in files:
#         threads[t].join()
#     print('end:%s' % ctime())

# 我的部分博客地址
# https://www.cnblogs.com/linuxchao/p/linuxchao-pytest-report.html
# https://www.cnblogs.com/linuxchao/p/linuxchao-pytest-configfile.html
# https://www.cnblogs.com/linuxchao/p/linuxchao-pytest-conftest.html

# thread.start_new_thread( print_time, ("Thread-1", 2, ) )