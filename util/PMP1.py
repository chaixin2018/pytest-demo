#!/usr/bin/env python3.6

# -*- coding: utf-8 -*-

import logging
import os
import platform
import time

import selenium.webdriver.support.ui as ui
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as WD
from selenium.webdriver.chrome.options import Options


# from time import sleep, time
# 首页界面
login_user = "Login_uName"  # id
login_password = "Login_uPass" # id
login_button = "uLogin" # id
sign_entrance = "/html/body/div[3]/div[1]/div[2]/div[1]/div/ul/li[1]/span/a" # xpath
i_sign_entrance = "/html/body/div[2]/div[1]/div[1]/div[2]/table/tbody/tr[1]/td/div/div[2]/div[1]/div/a" # xpath
next_button = "/html/body/div[2]/div[1]/div[1]/div[2]/div[1]/table[1]/tbody/tr/td[2]/div/a"
yes_button ="clause_yes"
info_confirm ="/html/body/div[2]/div[1]/div[1]/div[2]/div[1]/form/table/tbody/tr[21]/td/input"
exam_type_1 = "/html/body/div[2]/div[1]/div[1]/div[2]/div[1]/form/table/tbody/tr[2]/td[1]/span/label[1]/input"
exam_type_2 = "/html/body/div[2]/div[1]/div[1]/div[2]/div[1]/form/table/tbody/tr[2]/td[1]/span/label[2]/input"
last_name ="Xing"
middle_name ="Zhong"
first_name = "Ming"
training_agency = "/html/body/div[2]/div[1]/div[1]/div[2]/div[1]/form/table/tbody/tr[6]/td[1]/select/option[2]"
username_web = "PMIUname"
password_web = "PMIUpass"
dateF = "PMItimeB"
dateF1="/html/body/div[4]/table/tbody/tr[2]/td[1]/a"
dateT = "PMItimeE"
dateT1 ="/html/body/div[4]/table/tbody/tr[5]/td[1]/a"
test_site = "//*[@id='Kaodian']/option[7]"  # 大连东软
finish = "//*[@id='vform']/table/tbody/tr[14]/td/input"

logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'
)

'''
options = webdriver.ChromeOptions()
prefs = {
    'profile.default_content_setting_values' :
        {
        'notifications' : 2
         }
}
options.add_experimental_option('prefs',prefs)
driver = webdriver.Chrome(chrome_options = options)
'''

# 无头模式打开浏览器
__options = Options()
__options.add_argument('--headless')
__options.add_argument('--window-size=1440x900')
__options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
# 无头模式打开浏览器
#browser = webdriver.Chrome(chrome_options=__options)
# 不使用无头模式打开浏览器
browser = webdriver.Chrome()
url = "http://exam.chinapmp.cn/"
url1= "http://user.chinapmp.cn/examsign;sign.shtml"
logging.warning('kaishi！')
browser.get(url)

# t_system = platform.system()
# if t_system == 'Windows':
#     chromedriver_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'E://Program Files//Python//Python38//Scripts//chromedriver.exe')
#     browser = webdriver.Chrome(chromedriver_path)
# else:
#     browser = webdriver.Chrome()

wait2s = ui.WebDriverWait(browser, 2)
wait10s = ui.WebDriverWait(browser, 10)
wait30s = ui.WebDriverWait(browser, 30)

#url = "https://account.chsi.com.cn/passport/login?entrytype=yzgr&service=https%3a%2f%2fyz.chsi.com.cn%2fuser%2fcenter.jsp"


def click_select(name: str, opt_text: str):
    wait10s.until(
        EC.presence_of_element_located((By.XPATH, f"//select[@name='{name}']/option[contains(text(),'{opt_text}')]"))
    ).click()


def page_has_loaded(driver):
    """
 页面是否加载完
    :param driver:
    :return:
    """
    page_state = driver.execute_script('return document.readyState;')
    return page_state == 'complete'

try:
    # 登录

    browser.get(url)
    wait30s.until(EC.title_is('首页-项目管理职业资格认证'))
    #BasePage = Page.BasePage
    element = browser.find_element_by_xpath(sign_entrance)
    element.click()
    # BasePage.click("xpath",sign_entrance)
    #wait30s.until(EC.title_is('会员登录-首页-项目管理职业资格认证'))
    time.sleep(1)
    username = browser.find_element_by_id(login_user)
    username.send_keys("chai1005")  # 请再这儿输入用户名！
    password = browser.find_element_by_id(login_password)
    time.sleep(1)
    password.send_keys("chai1005")  # 请再这儿输入密码！
    browser.find_element_by_id(login_button).click()
    # password.send_keys(Keys.ENTER)
    time.sleep(1)
    cookies = browser.get_cookies()
    print(cookies)
    c1= cookies[0]
    print("c1:  ",c1)
    c2 = cookies[1]
    print("c2:  ", c2)
    c3 = cookies[2]
    print("c3:  ", c3)
    # c1 = {'domain': '.chinapmp.cn',
    #         'httpOnly': True,
    #         'name': 'user',
    #         'path': '/',
    #         'secure': False,
    #         'value': 'Te6Im1OPs5FPP88z0Ixj2f9i_yb_Yv8W'}
    # c2= {'domain': '.chinapmp.cn',
    #      'httpOnly': True,
    #      'name': 'SYSTEM_TEMP_COOKIE_NAME',
    #      'path': '/', 'secure': False,
    #      'value': 'B3D8E21B1D65DA723114967F114E359D'}
    # c3= {'domain': '.chinapmp.cn',
    #        'expiry': 1634708549, #1634698949
    #        'httpOnly': True,
    #        'name': 'SYSTEM_ONLY_COOKIE_NAME',
    #        'path': '/',
    #        'secure': False,
    #        'value': 'B5B26CE39ED2C81F82FDF17D1FC2C4E5'}
    browser.add_cookie(c1)
    browser.add_cookie(c2)
    browser.add_cookie(c3)
    # browser.get(url1)
    # 点击报名
    # browser.find_element_by_xpath(i_sign_entrance).click()
    # time.sleep(1)
    # 点击下一步
    # browser.find_element_by_xpath(next_button).click()
    # time.sleep(61)
    # 点击同意
    # browser.find_element_by_id(yes_button).click()
    # time.sleep(1)
    # 点击个人信息确认无误
    # browser.find_element_by_xpath(info_confirm).click()
    # time.sleep(1)
    # 输入报考信息
    # browser.find_element_by_xpath(exam_type_1).click()
    # browser.find_element_by_id(last_name).send_keys("XXXX")
    # browser.find_element_by_id(middle_name).send_keys("XXXX")
    # browser.find_element_by_id(first_name).send_keys("XXXX")
    # browser.find_element_by_xpath(training_agency).click()
    # browser.find_element_by_id(username_web).send_keys("XXXX")
    # browser.find_element_by_id(password_web).send_keys("XXXX")
    # #browser.find_element_by_id(dateT).send_keys(Keys.ENTER)
    # browser.find_element_by_id(dateF).click()
    # browser.find_element_by_xpath(dateF1).click()
    # #browser.find_element_by_id(dateF).send_keys(Keys.ENTER)
    # browser.find_element_by_id(dateT).click()
    # browser.find_element_by_xpath(dateT1).click()
    # browser.find_element_by_xpath(test_site).click()
    # browser.save_screenshot("./filename.png")
    # 点击报名
    #browser.find_element_by_xpath(finish).click()

    time.sleep(10)
finally:
    browser.close()