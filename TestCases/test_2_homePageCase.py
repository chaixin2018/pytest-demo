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
from data.home_page_data import HomePageData
from data.contact_data import ContactData



@pytest.mark.Test
class TestHomePage(object):
    """登录"""
    homePage_data = HomePageData
    homePage_data_menu = homePage_data.menu_select

    @pytest.mark.parametrize('name,expect', homePage_data_menu)
    def test_homepage(self, login, back_page,name, expect):
        home_page = login[1]
        time.sleep(7)
        home_page.select_menu(menu=name)
        time.sleep(2)
        #actual = home_page.get_path_text()
        #_capture_screenshot()
        assert expect in home_page.driver.page_source, "路径跳转正确, 断言成功"


if __name__ == "__main__":
    pytest.main(['-v', 'test_2_homePageCase.py'])
