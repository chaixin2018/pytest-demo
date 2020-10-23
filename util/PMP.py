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
dateT = "PMItimeE"
test_site = "/html/body/div[2]/div[1]/div[1]/div[2]/div[1]/form/table/tbody/tr[13]/td[1]/select/option[2]"


logging.basicConfig(
    level=logging.WARNING,
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
url_1 = "http://user.chinapmp.cn/examsign;sign.shtml"

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
    browser.find_element_by_xpath(i_sign_entrance).click()
    time.sleep(1)
    browser.find_element_by_xpath(next_button).click()
    time.sleep(61)
    browser.find_element_by_id(yes_button).click()
    time.sleep(1)
    browser.find_element_by_xpath(info_confirm).click()
    time.sleep(1)
    browser.find_element_by_xpath(exam_type_1).click()
    browser.find_element_by_id(last_name).send_keys("XXXX")
    browser.find_element_by_id(middle_name).send_keys("XXXX")
    browser.find_element_by_id(first_name).send_keys("XXXX")
    browser.find_element_by_xpath(training_agency).click()
    browser.find_element_by_id(username_web).send_keys("XXXX")
    browser.find_element_by_id(password_web).send_keys("XXXX")
    time.sleep(1)
    browser.find_element_by_id(dateT).send_keys(Keys.ENTER)
    time.sleep(1)
    browser.find_element_by_id(dateF).send_keys(Keys.ENTER)
    time.sleep(1)

    browser.find_element_by_xpath(test_site).click()
    time.sleep(1)
    browser.save_screenshot("./filename.png")
    # # 点击关闭关注学信公众号
    # wait10s.until(EC.title_is('全国硕士研究生招生考试网上报名平台'))
    # element = browser.find_element_by_class_name('ivu-modal-close')
    # element.click()
    #
    # # 点击确定
    # # wait10s.until(EC.title_is('全国硕士研究生招生考试网上报名平台'))
    # time.sleep(1.0)  # 等一下
    # element = browser.find_element_by_xpath('//a[text()="确定"]')
    # element.click()
    #
    # # 点击 填写报考信息
    # wait10s.until(EC.visibility_of_element_located((By.CLASS_NAME, 'yzwb-box2-cnt')))
    # element = browser.find_element_by_xpath('//div[text()="填写报考信息"]')
    # element.click()
    #
    # # 点击 阅读完毕
    # wait10s.until(lambda driver: driver.find_element_by_xpath('//button/span[text()="阅读完毕"]')).click()
    #
    # # 点击 同意 , 考生诚信考试承诺书界面, 要等10s才能点击。
    # wait30s.until(
    #     EC.element_to_be_clickable((By.XPATH, '//button/span[text()="同意"]'))
    # ).click()
    #
    # # 点击 确认 , 确认考生信息 界面
    # wait10s.until(
    #     EC.element_to_be_clickable((By.XPATH, '//button/span[text()="确认"]'))
    # ).click()
    #
    # # 报考单位 界面
    #
    # # 招生单位
    # click_select('yzwb_zsdwss', '输入省份')  # 输入省份
    # click_select('yzwb_bkdwdm', '输入学校')  # 输入学校
    #
    # # 考试方式
    # click_select('yzwb_ksfsm', '21(全国统考)')  # 输入考试方式
    # # 专项计划
    # click_select('yzwb_zxjh', '0(无)')  # 输入专项计划， 默认无。
    # # 报考类别
    # click_select('yzwb_bklbm', '11(非定向就业)')  # 输入报考类别， 默认：非定向就业
    #
    # wait10s.until(
    #     EC.element_to_be_clickable((By.XPATH, '//button/span[text()="下一步"]'))
    # ).click()
    #
    # # 备用信息
    # wait10s.until(
    #     EC.element_to_be_clickable((By.XPATH, '//button/span[text()="下一步"]'))
    # ).click()
    #
    # # 报考专业
    #
    # # 报考院系所名称
    # click_select('yzwb_mainyxsm', '报考院系所名称')  # 报考院系所名称，默认无
    # # 报考专业
    # click_select('yzwb_mainzydm', '报考专业')  # 报考专业，默认无
    # # 研究方向
    # click_select('yzwb_mainyjfxm', '研究方向')  # 研究方向，默认无
    #
    # # 学习方式
    # click_select('yzwb_mainbkxxfs', '1(全日制)')  # 学习方式，默认无
    # # 考试科目
    # click_select('yzwb_kskm', '')  # 考试科目，默认无
    #
    # wait10s.until(
    #     EC.element_to_be_clickable((By.XPATH, '//button/span[text()="下一步"]'))
    # ).click()
    #
    # # 报考点
    #
    # # 报考点所在省（市）
    # is_first = False
    # while True:
    #     logging.warning('选择报考点进行提交！')
    #     if is_first:
    #         # 直接刷新，避免走下面2个select的ajax请求。
    #         browser.refresh()
    #     else:
    #         is_first = True
    #         click_select('yzwb_bmdss', '51(四川省)')  # 报考点所在省（市），默认无
    #         click_select('yzwb_bmddm', '')  # 报考点，默认无
    #         wait10s.until(
    #             EC.element_to_be_clickable((By.XPATH, '//button/span[text()="下一步"]'))
    #         ).click()
    #
    #     while True:
    #         time.sleep(0.1)
    #         if page_has_loaded(browser):
    #             break
    #
    #     logging.warning('检查是否成功提交报考点！')
    #     is_success = False
    #     # 查看是否有错误弹框div
    #     try:
    #         c = browser.find_element_by_xpath(
    #             xpath='//div[contains(@class, "ivu-notice-with-error") and contains(@class, "ivu-notice-with-desc")]'
    #         )
    #         error_msg = c.text
    #         if error_msg and '错误' in error_msg:
    #             time.sleep(1)
    #             continue
    #     except NoSuchElementException:
    #         try:
    #             wait2s.until(EC.visibility_of_element_located((By.XPATH, '//h2[contains(text(), "确认报名信息")]')))
    #             break
    #         except (NoSuchElementException, TimeoutException):
    #             time.sleep(1)
    #             continue
    #
    # # 确认报名信息
    # wait10s.until(
    #     EC.element_to_be_clickable((By.XPATH, ".//*[contains(text(), '本人承诺信息完整属实，符合相关规定')]"))
    # ).click()
    #
    # wait10s.until(
    #     EC.element_to_be_clickable((By.XPATH, '//button/span[text()="确认报名"]'))
    # ).click()

    time.sleep(10)
finally:
    browser.close()