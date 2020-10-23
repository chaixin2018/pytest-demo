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
import random
import pytest
from Page import BasePage
from data.login_data import LoginData
from Page.BasePage import BasePage
from conftest import _capture_screenshot
from data.recommend_data import RecommendData
from Page.PageObject import RecommendPage


@pytest.mark.Test
class TestRecommendPage(object):

    """登录"""
    recommendPage_data = RecommendData
    recommendPage_data_select1 = recommendPage_data.select1_data #这个参数是用来做参数化的
    recommendPage_data_select2 = recommendPage_data.select2_data  # 这个参数是用来做参数化的
    recommendPage_data_select3 = recommendPage_data.select3_data  # 这个参数是用来做参数化的
    recommendPage_data_select4 = recommendPage_data.select4_data  # 这个参数是用来做参数化的

    def test_recommend0(self, login):
        home_page = login[1]
        time.sleep(7)
        home_page.select_menu(menu="recommend")

    @pytest.mark.parametrize('value,expect', recommendPage_data_select1)
    def test_recommend1(self, login,value,expect):
        # home_page = login[1]
        # time.sleep(2)
        recommend_page = login[2]
        # home_page.select_menu(menu="recommend")
        #recommend_page.click(recommend_page.select1[0],recommend_page.select1[1])
        recommend_page.select_option(recommend_page.select1[1],value,"index")
        actual_all = recommend_page.get_element_text(recommend_page.select1[0],recommend_page.select1[1]).split('\n')
        actual = actual_all[int(value)].strip()
        assert actual == expect, "断言成功"

    @pytest.mark.parametrize('value,expect', recommendPage_data_select2)
    def test_recommend2(self, login, value, expect):
        recommend_page = login[2]
        # recommend_page.click(recommend_page.select1[0],recommend_page.select1[1])
        recommend_page.select_option(recommend_page.select2[1], value, "index")
        actual_all = recommend_page.get_element_text(recommend_page.select2[0], recommend_page.select2[1]).split('\n')
        actual = actual_all[int(value)].strip()
        assert actual == expect, "断言成功"

    @pytest.mark.parametrize('value,expect', recommendPage_data_select3)
    def test_recommend3(self, login,value,expect):
        recommend_page = login[2]
        #recommend_page.click(recommend_page.select1[0],recommend_page.select1[1])
        recommend_page.select_option(recommend_page.select3[1],value,"index")
        actual_all = recommend_page.get_element_text(recommend_page.select3[0],recommend_page.select3[1]).split('\n')
        actual = actual_all[int(value)].strip()
        assert actual == expect, "断言成功"

    @pytest.mark.parametrize('value,expect', recommendPage_data_select4)
    def test_recommend4(self, login, value, expect):
        recommend_page = login[2]
        # recommend_page.click(recommend_page.select1[0],recommend_page.select1[1])
        recommend_page.select_option(recommend_page.select4[1], value, "index")
        actual_all = recommend_page.get_element_text(recommend_page.select4[0], recommend_page.select4[1]).split('\n')
        actual = actual_all[int(value)].strip()
        assert actual == expect, "断言成功"


@pytest.mark.Test
class TestRecommendPage_flow(object):

    def test_recommend_flow(self, login):
        home_page = login[1]
        time.sleep(7)
        home_page.select_menu(menu="recommend")

        recommend_page = login[2]
        recommend_page.select_option(recommend_page.select1[1], random.randint(0,3), "index")
        recommend_page.select_option(recommend_page.select2[1], 0, "index")
        recommend_page.select_option(recommend_page.select3[1], random.randint(0,5), "index")
        recommend_page.select_option(recommend_page.select4[1], random.randint(0,2), "index")
        recommend_page.click("xpath", recommend_page.nextBtn[1])
        time.sleep(1)
        recommend_page.click("xpath", recommend_page.select5_opt2[1])
        recommend_page.click("xpath", recommend_page.select6_opt2[1])
        recommend_page.click("xpath", recommend_page.select7_opt2[1])
        recommend_page.click("xpath", recommend_page.select8_opt2[1])
        recommend_page.click("xpath", recommend_page.select9_opt2[1])
        recommend_page.click("xpath", recommend_page.loginBtn[1])
        assert "Sevice Recommend" in recommend_page.driver.page_source
        recommend_page.click("xpath", "/html/body/div[4]/div/ul/li[1]/div[2]/div[2]/h4/a")
        time.sleep(2)
        assert "立 刻 购 买" in recommend_page.driver.page_source


    # def test_recommend(self, login):
    #     home_page = login[1]
    #     recommend_page = login[2]
    #     print("home_page",home_page)
    #     time.sleep(7)
    #     home_page.select_menu(menu="recommend")
    #     #home_page.option_value_check("//*[@id='business_types']", "option", "製造業, 卸売業, 小売業, IT, ")
    #     # recommend_page.click_select1_btn()
    #     # recommend_page.click_select1_opt(2,"index")
    #     recommend_page.click(recommend_page.select1[0],recommend_page.select1[1])
    #     recommend_page.select_option(recommend_page.select1[1],2,"index")
    #     #home_page.select_option(locator="//*[@id='business_types']", value=2, type="index")
    #     time.sleep(2)
    #     #expect = recommend_page.get_element_text("xpath","//*[@id='business_types']")
    #     print("recommend_page.select1",recommend_page.select1,recommend_page.select1[1])
    #     expect = recommend_page.get_element_text(recommend_page.select1[0],recommend_page.select1[1])
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
    pytest.main(['-v', 'test_3_recommendPageCase.py'])