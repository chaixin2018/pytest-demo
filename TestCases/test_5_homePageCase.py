"""
------------------------------------
@Time : 2020/9/15 14:46
@Auth : chai
@File : test_2_homePageCase.py
@IDE  : PyCharm
@Motto:
------------------------------------
"""
import time

import pytest

from Page.BasePage import BasePage
from conftest import _capture_screenshot
from data.contact_data import ContactData
from data.my_page import MyPageData


@pytest.mark.Test2
class TestHomePage(object):
    """登录"""
    MyPage_data = MyPageData
    MyPage_data_menu = MyPage_data.menu_select

    def test_myPage0(self, login):
        home_page = login[1]
        time.sleep(7)
        home_page.select_menu(menu="myPage")

    @pytest.mark.parametrize('name,expect', MyPage_data_menu)
    def test_myPage1(self, login, name, expect):
        # my_page = login[1]
        # time.sleep(7)
        # my_page.select_menu(menu="myPage")
        my_page = login[5]
        my_page.my_page_select_menu(menu=name)
        time.sleep(1)
        #actual = my_page.get_path_text()
        #_capture_screenshot()
        actual = my_page.get_element_text("xpath","/html/body/div[4]/div/div[2]/div/div/h3")
        print(actual,"actual")
        #assert expect in my_page.driver.page_source, "路径跳转正确, 断言成功"
        assert (expect == actual or expect in my_page.driver.page_source)


if __name__ == "__main__":
    pytest.main(['-v', 'test_2_homePageCase.py'])
