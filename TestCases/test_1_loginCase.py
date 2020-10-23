"""
------------------------------------
@Time :
@Auth :
@File : test_1_loginCase.py
@IDE  : PyCharm
@Motto:
------------------------------------
"""
import time

import pytest

from Page import BasePage
from data.login_data import LoginData



@pytest.mark.Test
class TestLogin(object):
    """登录"""
    login_data = LoginData

    @pytest.mark.parametrize('username, password, expect', login_data.login_fail_user_data)
    def test_fail_user_empty(self, open_url, username, password, expect):
        login_page = open_url
        login_page.login(username, password)
        time.sleep(3)
        actual = login_page.get_user_error_text()
        # actual = login_page.get_text(*LoginPage.userError_low)
        assert actual == expect, "登录失败, 断言失败"

    @pytest.mark.parametrize('username, password, expect', login_data.login_fail_password_data)
    def test_fail_password_empty(self, open_url, username, password, expect):
        login_page = open_url
        login_page.login(username, password)
        time.sleep(3)
        actual = login_page.get_password_error_text()
        assert actual == expect, "登录失败, 断言失败"

    @pytest.mark.parametrize('username, password, expect', login_data.login_success_data)
    def test_login(self, open_url, username, password, expect):
        login_page = open_url
        login_page.login(username, password)
        time.sleep(5)
        actual = login_page.get_login_success_account()

        assert expect in actual, "登录成功, 断言成功"
        login_page.click_password_login_btn()
        time.sleep(5)
        #login_page.switch_default_frame()


if __name__ == "__main__":
    pytest.main(['-v', 'test_1_loginCase.py'])
