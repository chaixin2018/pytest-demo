from Page.BasePage import BasePage
from util.parseConFile import ParseConFile


class RecommendPage(BasePage):
    # 配置文件读取元素
    do_conf = ParseConFile()
    # 选择密码登录的按钮
    select1 = do_conf.get_locators_or_account('RecommendPageElements', 'select1')
    # 登录框外的iframe
    select2 = do_conf.get_locators_or_account('RecommendPageElements', 'select2')
    # 用户名输入框
    select3 = do_conf.get_locators_or_account('RecommendPageElements', 'select3')
    # 密码输入框
    select4 = do_conf.get_locators_or_account('RecommendPageElements', 'select4')
    # 登录按钮
    nextBtn = do_conf.get_locators_or_account('RecommendPageElements', 'next_btn')

    select5_opt2 = do_conf.get_locators_or_account('RecommendPageElements', 'select5_opt2')
    select6_opt2 = do_conf.get_locators_or_account('RecommendPageElements', 'select6_opt2')
    select7_opt2 = do_conf.get_locators_or_account('RecommendPageElements', 'select7_opt2')
    select8_opt2 = do_conf.get_locators_or_account('RecommendPageElements', 'select8_opt2')
    select9_opt2 = do_conf.get_locators_or_account('RecommendPageElements', 'select9_opt2')
    # 登录按钮
    loginBtn = do_conf.get_locators_or_account('RecommendPageElements', 'login_Btn')

    detail_btn = do_conf.get_locators_or_account('RecommendPageElements', 'detail_btn')
    tel_btn = do_conf.get_locators_or_account('RecommendPageElements', 'tel_btn')
    email_btn = do_conf.get_locators_or_account('RecommendPageElements', 'email_btn')

    def click_select1_btn(self):
        return self.click(*RecommendPage.select1)
    def click_select2_btn(self):
        return self.click(*RecommendPage.select2)
    def click_select3_btn(self):
        return self.click(*RecommendPage.select3)
    def click_select4_btn(self):
        return self.click(*RecommendPage.select4)

    def click_select1_opt(self,value, type):
        return self.select_option(*RecommendPage.select1[1:], value, type)
    def click_select2_opt(self,value, type):
        return self.select_option(*RecommendPage.select2[1:], value, type)
    def click_select3_opt(self,value, type):
        return self.select_option(*RecommendPage.select3[1:], value, type)
    def click_select4_opt(self,value, type):
        return self.select_option(*RecommendPage.select4[1:], value, type)




if __name__ == "__main__":
    # RecommendPage =RecommendPage()
    # print(RecommendPage.select1)
    pass