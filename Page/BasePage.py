"""
------------------------------------
@Time :
@Auth :
@File : BasePage.py
@IDE  : PyCharm
@Motto:
------------------------------------
"""
import time
from datetime import datetime

import allure
from _pytest import logging
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait as WD
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    TimeoutException,
    NoAlertPresentException,
)

from config.conf import ROOT_DIR
from util.clipboard import ClipBoard
from util.keyboard import KeyBoard
from util.parseConFile import ParseConFile
from util.parseExcelFile import ParseExcel


class BasePage(object):
    """结合显示等待封装一些selenium内置方法"""
    cf = ParseConFile()
    excel = ParseExcel()

    def __init__(self, driver, timeout=30):
        self.byDic = {
            'id': By.ID,
            'name': By.NAME,
            'class_name': By.CLASS_NAME,
            'xpath': By.XPATH,
            'link_text': By.LINK_TEXT
        }
        self.driver = driver
        self.outTime = timeout

    def find_element(self, by, locator):
        """
        find alone element
        :param by: eg: id, name, xpath, css.....
        :param locator: id, name, xpath for str
        :return: element object
        """
        try:
            print('[Info:Starting find the element "{}" by "{}"!]'.format(locator, by))
            element = WD(self.driver, self.outTime).until(lambda x: x.find_element(by, locator))
        except TimeoutException as t:
            print('error: found "{}" timeout!'.format(locator), t)
        else:
            return element

    def find_elements(self, by, locator):
        """
        find group elements
        :param by: eg: id, name, xpath, css.....
        :param locator: eg: id, name, xpath for str
        :return: elements object
        """
        try:
            print('[Info:start find the elements "{}" by "{}"!]'.format(locator, by))
            elements = WD(self.driver, self.outTime).until(lambda x: x.find_elements(by, locator))
        except TimeoutException as t:
            print('error: found "{}" timeout!'.format(locator), t)
        else:
            return elements

    def is_element_exist(self, by, locator):
        """
        assert element if exist
        :param by: eg: id, name, xpath, css.....
        :param locator: eg: id, name, xpath for str
        :return: if element return True else return false
        """
        if by.lower() in self.byDic:
            try:
                WD(self.driver, self.outTime). \
                    until(ec.visibility_of_element_located((self.byDic[by], locator)))
            except TimeoutException:
                print('Error: element "{}" not exist'.format(locator))
                return False
            return True
        else:
            print('the "{}" error!'.format(by))

    def is_click(self, by, locator):
        if by.lower() in self.byDic:
            try:
                element = WD(self.driver, self.outTime). \
                    until(ec.element_to_be_clickable((self.byDic[by], locator)))
            except TimeoutException:
                print("元素不可以点击")
            else:
                return element
        else:
            print('the "{}" error!'.format(by))

    def is_alert(self):
        """
        assert alert if exsit
        :return: alert obj
        """
        try:
            re = WD(self.driver, self.outTime).until(ec.alert_is_present())
        except (TimeoutException, NoAlertPresentException):
            print("error:no found alert")
        else:
            return re

    def switch_to_frame(self, by, locator):
        """判断frame是否存在，存在就跳到frame"""
        print('info:switching to iframe "{}"'.format(locator))
        if by.lower() in self.byDic:
            try:
                WD(self.driver, self.outTime). \
                    until(ec.frame_to_be_available_and_switch_to_it((self.byDic[by], locator)))
            except TimeoutException as t:
                print('error: found "{}" timeout！切换frame失败'.format(locator), t)
        else:
            print('the "{}" error!'.format(by))

    def switch_to_default_frame(self):
        """返回默认的frame"""
        print('info:switch back to default iframe')
        try:
            self.driver.switch_to.default_content()
        except Exception as e:
            print(e)

    def get_alert_text(self):
        """获取alert的提示信息"""
        alert = self.is_alert()
        if alert:
            return alert.text
        else:
            return None

    def get_element_text(self, by, locator, name=None):
        """获取某一个元素的text信息"""
        try:
            element = self.find_element(by, locator)
            if name:
                return element.get_attribute(name)
            else:
                return element.text
        except AttributeError:
            print('get "{}" text failed return None'.format(locator))

    def load_url(self, url):
        """加载url"""
        print('info: string upload url "{}"'.format(url))
        self.driver.get(url)

    def get_source(self):
        """获取页面源码"""
        return self.driver.page_source

    def send_keys(self, by, locator, value=''):
        """写数据"""
        print('info:input "{}"'.format(value))
        try:
            element = self.find_element(by, locator)
            element.send_keys(value)
        except AttributeError as e:
            print(e)

    def clear(self, by, locator):
        """清理数据"""
        print('info:clearing value')
        try:
            element = self.find_element(by, locator)
            element.clear()
        except AttributeError as e:
            print(e)

    def click(self, by, locator):
        """点击某个元素"""
        print('info:click "{}"'.format(locator))
        element = self.is_click(by, locator)
        if element:
            element.click()
        else:
            print('the "{}" unclickable!')

    @staticmethod
    def sleep(num=0):
        """强制等待"""
        print('info:sleep "{}" minutes'.format(num))
        time.sleep(num)

    def ctrl_v(self, value):
        """ctrl + V 粘贴"""
        print('info:pasting "{}"'.format(value))
        ClipBoard.set_text(value)
        self.sleep(3)
        KeyBoard.two_keys('ctrl', 'v')

    @staticmethod
    def enter_key():
        """enter 回车键"""
        print('info:keydown enter')
        KeyBoard.one_key('enter')

    def wait_element_to_be_located(self, by, locator):
        """显示等待某个元素出现，且可见"""
        print('info:waiting "{}" to be located'.format(locator))
        try:
            return WD(self.driver, self.outTime).until(ec.presence_of_element_located((self.byDic[by], locator)))
        except TimeoutException as t:
            print('error: found "{}" timeout！'.format(locator), t)

    def get_page_source(self):
        return self.get_source()

    """
    功能：遍历option下拉框，比对结果
    value_text写法：从第一个依次写，每个选项用， 分割，最后一个后面需要， 举例"製造業, 卸売業, 小売業, IT, "
    调用：option_value_check(self, "//*[@id='business_types']", "option", "製造業, 卸売業, 小売業, IT, ")
    """
    def option_value_check(self, xpath, tag_name, value_text):
        select = self.find_element_by_xpath(xpath)
        # 注意使用find_elements
        options_list = select.find_elements_by_tag_name(tag_name)
        option_text = ""
        for option in options_list:
            # 获取下拉框的value和text
            # print("Value is:%s  Text is:%s" % (option.get_attribute("value"), option.text))
            s1 = Select(self.driver.find_element_by_xpath(xpath))
            s1.select_by_visible_text(option.text)
            option_text = option_text + option.text + ', '
            time.sleep(1)
        if option_text == value_text:
            option_text = option_text + "选项内容校验正确"
        else:
            option_text = option_text + "选项内容校验错误"
        return option_text

    def select_option(self, locator, value, type="index"):
        #self.wait_utilVisible(locator)
        time.sleep(2)

        se = self.driver.find_element_by_xpath(locator)
        #se = self.get_element_text("xpath", locator, name=None)

        select = Select(se)
        #logging.info("选择的type为{0}".format(type))
        if type == "index":
            select.select_by_index(value)

            #Select(se).select_by_index(self,value)
            #logging.info("选择的index是{0}".format(value))
        elif type == "value":
            Select(se).select_by_value(value)
            #logging.info("选择的值是{0}".format(value))
        else:
            Select(se).select_by_visible_text(value)
            #ogging.info("根据文本内容传的值是{0}".format(value))

    def save_screenshot(self, img_doc):
        '''
        页面截屏保存截图
        :param img_doc: 截图说明
        :return:
        '''
        file_name = ROOT_DIR + "\\{}_{}.png".format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S"), img_doc)
        self.driver.save_screenshot(file_name)
        with open(file_name, mode='rb') as f:
            file = f.read()
        allure.attach(file, img_doc, allure.attachment_type.PNG)

if __name__ == "__main__":
    BasePage= BasePage()
    BasePage.get_element_text("xpath","/html/body/div[3]/div/nav/div/div[2]/ul[2]/li[3]/a")
