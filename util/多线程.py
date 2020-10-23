
"""
********************************************************************
demo1
_thread方法
********************************************************************
"""
#!/usr/bin/python
# -*- coding: UTF-8 -*-

# import threading
# import time
# import _thread
#
#
# # 为线程定义一个函数
# def print_time(threadName, delay):
#     count = 0
#     while count < 5:
#         time.sleep(delay)
#         count += 1
#         print ("%s: %s" % (threadName, time.ctime(time.time())))
#
#
# # 创建两个线程
# try:
#     _thread.start_new_thread(print_time, ("Thread-1", 2,))
#     _thread.start_new_thread(print_time, ("Thread-2", 4,))
# except:
#     print ("Error: unable to start thread")
#
# while 1:
#     pass
from telnetlib import EC

from selenium.webdriver.common.by import By

"""
********************************************************************
demo2
threading方法
********************************************************************
"""
# !/usr/bin/python
# -*- coding: UTF-8 -*-

# import threading
# import time
#
# exitFlag = 0
#
#
# class myThread(threading.Thread):  # 继承父类threading.Thread
#     def __init__(self, threadID, name, counter):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.counter = counter
#
#     def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
#         print ("Starting " + self.name)
#         print_time(self.name, self.counter, 5)
#         print ("Exiting " + self.name)
#
#
# def print_time(threadName, delay, counter):
#     while counter:
#         if exitFlag:
#             (threading.Thread).exit()
#         time.sleep(delay)
#         print ("%s: %s" % (threadName, time.ctime(time.time())))
#         counter -= 1
#
#
# # 创建新线程
# thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(2, "Thread-2", 2)
#
# # 开启线程
# thread1.start()
# thread2.start()
#
# print ("Exiting Main Thread")


"""
********************************************************************
demo3
锁
********************************************************************
"""
# # !/usr/bin/python
# # -*- coding: UTF-8 -*-
#
# import threading
# import time
#
#
# class myThread(threading.Thread):
#     def __init__(self, threadID, name, counter):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.counter = counter
#
#     def run(self):
#         print ("Starting " + self.name)
#         # 获得锁，成功获得锁定后返回True
#         # 可选的timeout参数不填时将一直阻塞直到获得锁定
#         # 否则超时后将返回False
#         threadLock.acquire()
#         print_time(self.name, self.counter, 3)
#         # 释放锁
#         threadLock.release()
#
#
# def print_time(threadName, delay, counter):
#     while counter:
#         time.sleep(delay)
#         print ("%s: %s" % (threadName, time.ctime(time.time())))
#         counter -= 1
#
#
# threadLock = threading.Lock()
# threads = []
#
# # 创建新线程
# thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(2, "Thread-2", 2)
#
# # 开启新线程
# thread1.start()
# thread2.start()
#
# # 添加线程到线程列表
# threads.append(thread1)
# threads.append(thread2)
#
# # 等待所有线程完成
# for t in threads:
#     t.join()
# print ("Exiting Main Thread")


# !/usr/bin/python
# -*- coding: UTF-8 -*-

"""
********************************************************************
demo4
队列
********************************************************************
"""

# import queue
# import threading
# import time
#
# exitFlag = 0
#
#
# class myThread(threading.Thread):
#     def __init__(self, threadID, name, q):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.q = q
#
#     def run(self):
#         print("Starting " + self.name)
#         process_data(self.name, self.q)
#         print("Exiting " + self.name)
#
#
# def process_data(threadName, q):
#     while not exitFlag:
#         queueLock.acquire()
#         if not workQueue.empty():
#             data = q.get()
#             queueLock.release()
#             print("%s processing %s" % (threadName, data))
#         else:
#             queueLock.release()
#         time.sleep(1)
#
#
# threadList = ["Thread-1", "Thread-2", "Thread-3"]
# nameList = ["One", "Two", "Three", "Four", "Five"]
# queueLock = threading.Lock()
# workQueue = queue.Queue(10)
# threads = []
# threadID = 1
#
# # 创建新线程
# for tName in threadList:
#     thread = myThread(threadID, tName, workQueue)
#     thread.start()
#     threads.append(thread)
#     threadID += 1
#
# # 填充队列
# queueLock.acquire()
# for word in nameList:
#     workQueue.put(word)
# queueLock.release()
#
# # 等待队列清空
# while not workQueue.empty():
#     pass
#
# # 通知线程是时候退出
# exitFlag = 1
#
# # 等待所有线程完成
# for t in threads:
#     t.join()
# print("Exiting Main Thread")

"""
********************************************************************
demo5
python多线程+selenium启动多个浏览器
********************************************************************
"""
# from time import ctime, sleep
# from selenium import webdriver
# import threading
#
#
# def select_browser(browser):
#     print("start %s" % browser, ctime())
#     try:
#         if browser == 'Chrome' or browser == "Ch":
#             dr = webdriver.Chrome()
#         elif browser == 'Firefox' or browser == 'Ff':
#             dr = webdriver.Firefox()
#         elif browser == 'Ie' or browser == 'ie':
#             dr = webdriver.Ie()
#         elif browser == 'phantomjs' or browser == 'PhantomJS':
#             dr = webdriver.PhantomJS()
#         else:
#             print("Not found %s browser,You can use ‘firefox‘, ‘chrome‘, ‘ie‘ or ‘phantomjs‘" % browser)
#         return dr
#     except Exception as msg:
#         print("启动浏览器出现异常：%s" % str(msg))
#
# def test_baidu(browser_name):
#     driver = select_browser(browser_name)
#     driver.maximize_window()
#     driver.get("https://www.baidu.com")
#     driver.find_element_by_id('kw').send_keys('selenium')
#     driver.find_element_by_id('su').click()
#     sleep(5)
#     print(driver.title)
#     driver.quit()
#     print("end %s" % browser_name, ctime())
#
#
#
#
# def thread_browser(*args):
#     if args:
#         threads = []  # 创建线程列表
#         for browser in args:
#             t = threading.Thread(target=test_baidu, args=(browser,))  # 创建线程
#             threads.append(t)
#         for t in threads:
#             t.start()  # 启动线程
#         for t in threads:
#             t.join()  # 守护线程
#         print("end all time %s" % ctime())
#     else:
#         print("Please pass at least one browser name")
#
#
# if __name__ == "__main__":
#     thread_browser('Firefox', 'Chrome')
"""
********************************************************************
demo6
python多线程+selenium启动多个浏览器
********************************************************************
"""

# !/usr/bin/python3
# coding=utf-8
from selenium import webdriver
from tomorrow import threads
from time import ctime, sleep
import threading

def select_browser(browser):
    print("start %s" % browser, ctime())
    try:
        if browser == 'Chrome' or browser == "Ch":
            dr = webdriver.Chrome()
        elif browser == 'Firefox' or browser == 'Ff':
            dr = webdriver.Firefox()
        elif browser == 'Ie' or browser == 'ie':
            dr = webdriver.Ie()
        elif browser == 'phantomjs' or browser == 'PhantomJS':
            dr = webdriver.PhantomJS()
        else:
            print("Not found %s browser,You can use ‘firefox‘, ‘chrome‘, ‘ie‘ or ‘phantomjs‘" % browser)
        return dr
    except Exception as msg:
        print("启动浏览器出现异常：%s" % str(msg))

def test_baidu(browser_name):
    driver = select_browser(browser_name)
    driver.maximize_window()
    driver.get("https://www.baidu.com")
    driver.find_element_by_id('kw').send_keys('selenium')
    driver.find_element_by_id('su').click()
    sleep(5)
    print(driver.title)
    driver.quit()
    print("end %s" % browser_name, ctime())

def thread_browser(*args):
    if args:
        threads = []  # 创建线程列表
        for browser in args:
            t = threading.Thread(target=test_baidu, args=(browser,))  # 创建线程
            threads.append(t)
        for t in threads:
            t.start()  # 启动线程
        for t in threads:
            t.join()  # 守护线程
        print("end all time %s" % ctime())
    else:
        print("Please pass at least one browser name")

def test_baidu_01(name):
    driver = select_browser(name)
    driver.maximize_window()
    driver.get("https://www.baidu.com")
    driver.find_element_by_id("kw").send_keys("python")
    driver.find_element_by_id('su').click()
    print(driver.title,"111111")

    driver.quit()
    print("quit %s" % name, ctime())


def test_baidu_02(name):
    driver = select_browser(name)
    driver.maximize_window()
    driver.get("https://www.baidu.com")
    print(driver.title, "222222")
    driver.find_element_by_link_text("更多").click()
    sleep(5)
    # driver.WebDriverWait(driver, 5, 0.5).until(EC.visibility_of_element_located((By.LINK_TEXT, "搜索设置")), message="搜索设置未出现")
    # print(driver.find_element_by_link_text("搜索设置").text)
    # driver.find_element_by_link_text("搜索设置").click()
    # driver.find_element_by_link_text("保存设置").click()
    # print(driver.title, "222222")
    driver.quit()
    print("quit %s" % name, ctime())


@threads(n=10)  # n为线程数
def all(name):
    test_baidu_01(name)
    test_baidu_02(name)


if __name__ == "__main__":
    browsers = ("Chrome", "Chrome")
    for i in browsers:
        all(i)