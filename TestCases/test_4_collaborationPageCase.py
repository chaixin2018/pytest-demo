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
from Page import BasePage
from data.login_data import LoginData
from Page.BasePage import BasePage
from conftest import _capture_screenshot
from data.collaboration_data import CollaborationData, CollaborationData_2
from Page.PageObject import CollaborationPage

@pytest.mark.Test
class TestcollaborationPage_flow(object):

    def test_collaboration_flow(self, login):
        home_page = login[1]
        time.sleep(7)
        home_page.select_menu(menu="collaboration")
        time.sleep(2)

        collaboration_page_1 = login[3]
        collaboration_page_1.click("xpath", collaboration_page_1.select_opt2[1])
        collaboration_page_1.click("xpath", collaboration_page_1.select_Btn[1])
        time.sleep(1)

        collaboration_page_1.select_option(collaboration_page_1.select1[1], 1, "index")
        collaboration_page_1.select_option(collaboration_page_1.select2[1], 1, "index")
        collaboration_page_1.select_option(collaboration_page_1.select3[1], 1, "index")
        collaboration_page_1.select_option(collaboration_page_1.select4[1], 1, "index")
        collaboration_page_1.select_option(collaboration_page_1.select5[1], 1, "index")
        collaboration_page_1.select_option(collaboration_page_1.select6[1], 1, "index")
        collaboration_page_1.click("xpath", collaboration_page_1.login_Btn[1])
        time.sleep(2)
        assert "販売商材" in collaboration_page_1.driver.page_source
        collaboration_page_1.click("xpath", "/html/body/div[4]/div/ul/li[1]/div[2]/div[2]/h4/a")
        time.sleep(2)
        assert "更多服务" in collaboration_page_1.driver.page_source


@pytest.mark.Test
class TestCollaborationPage(object):

    """登录"""
    collaborationPage_data = CollaborationData
    collaborationPage_data_select1 = collaborationPage_data.select1_data #这个参数是用来做参数化的
    collaborationPage_data_select2 = collaborationPage_data.select2_data  # 这个参数是用来做参数化的
    collaborationPage_data_select3 = collaborationPage_data.select3_data  # 这个参数是用来做参数化的
    collaborationPage_data_select4 = collaborationPage_data.select4_data  # 这个参数是用来做参数化的
    collaborationPage_data_select5 = collaborationPage_data.select5_data  # 这个参数是用来做参数化的
    collaborationPage_data_select6 = collaborationPage_data.select6_data  # 这个参数是用来做参数化的

    def test_collaboration0(self, login):
        home_page = login[1]
        time.sleep(7)
        home_page.select_menu(menu="collaboration")
        collaboration_page_1 = login[3]
        print("testdebug111")
        collaboration_page_1.click("xpath", collaboration_page_1.select_opt2[1])
        print("testdebug111",collaboration_page_1.select_opt2)
        collaboration_page_1.click("xpath", collaboration_page_1.select_Btn[1])
        print("testdebug111",collaboration_page_1.select_Btn)
        time.sleep(5)
        

    @pytest.mark.parametrize('value,expect', collaborationPage_data_select1)
    def test_collaboration1(self, login,value,expect):
        # home_page = login[1]
        # time.sleep(2)
        collaboration_page_1 = login[3]
        # home_page.select_menu(menu="collaboration")
        #collaboration_page_1.click(collaboration_page_1.select1[0],collaboration_page_1.select1[1])
        collaboration_page_1.select_option(collaboration_page_1.select1[1],value,"index")
        actual_all = collaboration_page_1.get_element_text(collaboration_page_1.select1[0],collaboration_page_1.select1[1]).split('\n')
        actual = actual_all[int(value)].strip()
        assert actual == expect, "断言成功"

    @pytest.mark.parametrize('value,expect', collaborationPage_data_select2)
    def test_collaboration2(self, login, value, expect):
        collaboration_page_1 = login[3]
        # collaboration_page_1.click(collaboration_page_1.select1[0],collaboration_page_1.select1[1])
        collaboration_page_1.select_option(collaboration_page_1.select2[1], value, "index")
        actual_all = collaboration_page_1.get_element_text(collaboration_page_1.select2[0], collaboration_page_1.select2[1]).split('\n')
        actual = actual_all[int(value)].strip()
        assert actual == expect, "断言成功"

    @pytest.mark.parametrize('value,expect', collaborationPage_data_select3)
    def test_collaboration3(self, login,value,expect):
        collaboration_page_1 = login[3]
        #collaboration_page_1.click(collaboration_page_1.select1[0],collaboration_page_1.select1[1])
        collaboration_page_1.select_option(collaboration_page_1.select3[1],value,"index")
        actual_all = collaboration_page_1.get_element_text(collaboration_page_1.select3[0],collaboration_page_1.select3[1]).split('\n')
        actual = actual_all[int(value)].strip()
        assert actual == expect, "断言成功"

    @pytest.mark.parametrize('value,expect', collaborationPage_data_select4)
    def test_collaboration4(self, login, value, expect):
        collaboration_page_1 = login[3]
        # collaboration_page_1.click(collaboration_page_1.select1[0],collaboration_page_1.select1[1])
        collaboration_page_1.select_option(collaboration_page_1.select4[1], value, "index")
        actual_all = collaboration_page_1.get_element_text(collaboration_page_1.select4[0], collaboration_page_1.select4[1]).split('\n')
        actual = actual_all[int(value)].strip()
        assert actual == expect, "断言成功"

    @pytest.mark.parametrize('value,expect', collaborationPage_data_select5)
    def test_collaboration5(self, login, value, expect):
        collaboration_page_1 = login[3]
        # collaboration_page_1.click(collaboration_page_1.select1[0],collaboration_page_1.select1[1])
        collaboration_page_1.select_option(collaboration_page_1.select5[1], value, "index")
        actual_all = collaboration_page_1.get_element_text(collaboration_page_1.select5[0],
                                                           collaboration_page_1.select5[1]).split('\n')
        actual = actual_all[int(value)].strip()
        assert actual == expect, "断言成功"

    @pytest.mark.parametrize('value,expect', collaborationPage_data_select6)
    def test_collaboration6(self, login, value, expect):
        collaboration_page_1 = login[3]
        # collaboration_page_1.click(collaboration_page_1.select1[0],collaboration_page_1.select1[1])
        collaboration_page_1.select_option(collaboration_page_1.select6[1], value, "index")
        actual_all = collaboration_page_1.get_element_text(collaboration_page_1.select6[0],
                                                           collaboration_page_1.select6[1]).split('\n')
        actual = actual_all[int(value)].strip()
        assert actual == expect, "断言成功"




"""
第二个界面功能测试
"""

@pytest.mark.Test
class TestcollaborationPage_2_flow(object):

    def test_collaboration_2_flow(self, login):
        home_page = login[1]
        time.sleep(7)
        home_page.select_menu(menu="collaboration")
        time.sleep(2)

        collaboration_page_2 = login[4]
        collaboration_page_2.click("xpath", collaboration_page_2.select_opt3[1])
        collaboration_page_2.click("xpath", collaboration_page_2.select_Btn[1])
        time.sleep(1)

        collaboration_page_2.select_option(collaboration_page_2.select1[1], 1, "index")
        collaboration_page_2.select_option(collaboration_page_2.select2[1], 1, "index")
        collaboration_page_2.select_option(collaboration_page_2.select3[1], 1, "index")
        collaboration_page_2.select_option(collaboration_page_2.select4[1], 1, "index")
        collaboration_page_2.select_option(collaboration_page_2.select5[1], 1, "index")
        collaboration_page_2.select_option(collaboration_page_2.select6[1], 1, "index")
        collaboration_page_2.click("xpath", collaboration_page_2.login_Btn[1])
        time.sleep(2)
        assert "販売商材" in collaboration_page_2.driver.page_source
        collaboration_page_2.click("xpath", "/html/body/div[4]/div/ul/li[1]/div[2]/div[2]/h4/a")
        time.sleep(2)
        assert "更多服务" in collaboration_page_2.driver.page_source


@pytest.mark.Test
class TestCollaborationPage_2(object):
    """登录"""
    collaborationPage_data = CollaborationData_2
    collaborationPage_data_select1 = collaborationPage_data.select1_data  # 这个参数是用来做参数化的
    collaborationPage_data_select2 = collaborationPage_data.select2_data  # 这个参数是用来做参数化的
    collaborationPage_data_select3 = collaborationPage_data.select3_data  # 这个参数是用来做参数化的
    collaborationPage_data_select4 = collaborationPage_data.select4_data  # 这个参数是用来做参数化的
    collaborationPage_data_select5 = collaborationPage_data.select5_data  # 这个参数是用来做参数化的
    collaborationPage_data_select6 = collaborationPage_data.select6_data  # 这个参数是用来做参数化的

    def test_collaboration0(self, login):
        home_page = login[1]
        time.sleep(7)
        home_page.select_menu(menu="collaboration")
        collaboration_page_1 = login[4]
        collaboration_page_1.click("xpath", collaboration_page_1.select_opt3[1])
        collaboration_page_1.click("xpath", collaboration_page_1.select_Btn[1])
        time.sleep(5)

    @pytest.mark.parametrize('value,expect', collaborationPage_data_select1)
    def test_collaboration1(self, login, value, expect):
        # home_page = login[1]
        # time.sleep(2)
        collaboration_page_1 = login[4]
        # home_page.select_menu(menu="collaboration")
        # collaboration_page_1.click(collaboration_page_1.select1[0],collaboration_page_1.select1[1])
        collaboration_page_1.select_option(collaboration_page_1.select1[1], value, "index")
        actual_all = collaboration_page_1.get_element_text(collaboration_page_1.select1[0],
                                                           collaboration_page_1.select1[1]).split('\n')
        actual = actual_all[int(value)].strip()
        assert actual == expect, "断言成功"

    @pytest.mark.parametrize('value,expect', collaborationPage_data_select2)
    def test_collaboration2(self, login, value, expect):
        collaboration_page_1 = login[4]
        # collaboration_page_1.click(collaboration_page_1.select1[0],collaboration_page_1.select1[1])
        collaboration_page_1.select_option(collaboration_page_1.select2[1], value, "index")
        actual_all = collaboration_page_1.get_element_text(collaboration_page_1.select2[0],
                                                           collaboration_page_1.select2[1]).split('\n')
        actual = actual_all[int(value)].strip()
        assert actual == expect, "断言成功"

    @pytest.mark.parametrize('value,expect', collaborationPage_data_select3)
    def test_collaboration3(self, login, value, expect):
        collaboration_page_1 = login[4]
        # collaboration_page_1.click(collaboration_page_1.select1[0],collaboration_page_1.select1[1])
        collaboration_page_1.select_option(collaboration_page_1.select3[1], value, "index")
        actual_all = collaboration_page_1.get_element_text(collaboration_page_1.select3[0],
                                                           collaboration_page_1.select3[1]).split('\n')
        actual = actual_all[int(value)].strip()
        assert actual == expect, "断言成功"

    @pytest.mark.parametrize('value,expect', collaborationPage_data_select4)
    def test_collaboration4(self, login, value, expect):
        collaboration_page_1 = login[4]
        # collaboration_page_1.click(collaboration_page_1.select1[0],collaboration_page_1.select1[1])
        collaboration_page_1.select_option(collaboration_page_1.select4[1], value, "index")
        actual_all = collaboration_page_1.get_element_text(collaboration_page_1.select4[0],
                                                           collaboration_page_1.select4[1]).split('\n')
        actual = actual_all[int(value)].strip()
        assert actual == expect, "断言成功"

    @pytest.mark.parametrize('value,expect', collaborationPage_data_select5)
    def test_collaboration5(self, login, value, expect):
        collaboration_page_1 = login[4]
        # collaboration_page_1.click(collaboration_page_1.select1[0],collaboration_page_1.select1[1])
        collaboration_page_1.select_option(collaboration_page_1.select5[1], value, "index")
        actual_all = collaboration_page_1.get_element_text(collaboration_page_1.select5[0],
                                                           collaboration_page_1.select5[1]).split('\n')
        actual = actual_all[int(value)].strip()
        assert actual == expect, "断言成功"

    @pytest.mark.parametrize('value,expect', collaborationPage_data_select6)
    def test_collaboration6(self, login, value, expect):
        collaboration_page_1 = login[4]
        # collaboration_page_1.click(collaboration_page_1.select1[0],collaboration_page_1.select1[1])
        collaboration_page_1.select_option(collaboration_page_1.select6[1], value, "index")
        actual_all = collaboration_page_1.get_element_text(collaboration_page_1.select6[0],
                                                           collaboration_page_1.select6[1]).split('\n')
        actual = actual_all[int(value)].strip()
        assert actual == expect, "断言成功"




    # def test_collaboration(self, login):
    #     home_page = login[1]
    #     collaboration_page_1 = login[3]
    #     print("home_page",home_page)
    #     time.sleep(7)
    #     home_page.select_menu(menu="collaboration")
    #     #home_page.option_value_check("//*[@id='business_types']", "option", "製造業, 卸売業, 小売業, IT, ")
    #     # collaboration_page_1.click_select1_btn()
    #     # collaboration_page_1.click_select1_opt(2,"index")
    #     collaboration_page_1.click(collaboration_page_1.select1[0],collaboration_page_1.select1[1])
    #     collaboration_page_1.select_option(collaboration_page_1.select1[1],2,"index")
    #     #home_page.select_option(locator="//*[@id='business_types']", value=2, type="index")
    #     time.sleep(2)
    #     #expect = collaboration_page_1.get_element_text("xpath","//*[@id='business_types']")
    #     print("collaboration_page_1.select1",collaboration_page_1.select1,collaboration_page_1.select1[1])
    #     expect = collaboration_page_1.get_element_text(collaboration_page_1.select1[0],collaboration_page_1.select1[1])
    #     assert "小売業" in expect, "路径跳转正确, 断言成功"
    #     home_page.select_option(locator="//*[@id='position']", value=0, type="index")
    #     expect = home_page.get_element_text("xpath", "//*[@id='position']")
    #     assert "経営者" in expect, "路径跳转正确, 断言成功"
    #     home_page.select_option(locator="//*[@id='scale']", value=1, type="index")
    #     expect = home_page.get_element_text("xpath", "//*[@id='scale']")
    #     assert "10~20人未満" in "10~20人未満", "路径跳转正确, 断言成功"
    #     time.sleep(5)
    #     #home_page.get_element(self.Button_Search).click()


if __name__ == "__main__":
    pytest.main(['-v', 'test_3_collaborationPageCase.py'])