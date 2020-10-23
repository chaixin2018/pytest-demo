"""
------------------------------------
@Time :
@Auth :
@File : conftest.py
@IDE  : PyCharm
@Motto:
------------------------------------
"""
import pytest

from Page.PageObject.CollaborationPage import CollaborationPage_1, CollaborationPage_2
from Page.PageObject.LoginPage import LoginPage
from Page.PageObject.HomePage import HomePage
from Page.PageObject.MyPage import MyPage
from Page.PageObject.RecommendPage import RecommendPage
from util.parseConFile import ParseConFile


do_conf = ParseConFile()
# 从配置文件中获取正确的用户名和密码
userName = do_conf.get_locators_or_account('LoginAccount', 'username')
passWord = do_conf.get_locators_or_account('LoginAccount', 'password')


# @pytest.fixture(scope='function')
# def login(driver):
#     """除登录用例，每一个用例的前置条件"""
#     print('------------staring login------------')
#     login_action = LoginPage(driver, 30)
#     login_action.login(userName, passWord)
#     yield
#     print('------------end login------------')
#     driver.delete_all_cookies()

class CollaborationPage(object):
    pass


@pytest.fixture(scope='class')
def ini_pages(driver):
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    recommend_page=RecommendPage(driver)
    collaboration_page= CollaborationPage_1(driver)
    collaboration_page_2 = CollaborationPage_2(driver)
    setting = MyPage(driver)
    # contact_page = ContactPage(driver)
    # send_mail_page = SendMailPage(driver)
    #yield driver, login_page, home_page, contact_page, send_mail_page
    yield driver, login_page, home_page,recommend_page, collaboration_page,collaboration_page_2,setting


@pytest.fixture(scope='function')
def open_url(ini_pages):
    driver = ini_pages[0]
    login_page = ini_pages[1]
    # login_page.open_url()
    yield login_page
    driver.delete_all_cookies()


@pytest.fixture(scope='class')
def login(ini_pages):
    # driver, login_page, home_page, contact_page, send_mail_page = ini_pages
    driver, login_page, home_page, recommend_page, collaboration_page, collaboration_page_2,setting = ini_pages
    # login_page.open_url()
    login_page.login(userName, passWord)
    login_page.switch_default_frame()
    #yield login_page, home_page, contact_page, send_mail_page
    yield login_page, home_page, recommend_page, collaboration_page, collaboration_page_2,setting
    driver.delete_all_cookies()


@pytest.fixture(scope='function')
def refresh_page(ini_pages):
    driver = ini_pages[0]
    yield
    driver.refresh()


@pytest.fixture(scope='function')
def back_page(ini_pages):
    driver = ini_pages[0]
    yield
    driver.back()
