from Page.BasePage import BasePage
from util.parseConFile import ParseConFile


class CollaborationPage_1(BasePage):
    # 配置文件读取元素
    do_conf = ParseConFile()
    select_opt1 = do_conf.get_locators_or_account('collaborationPageElements_1', 'select_opt1')
    select_opt2 = do_conf.get_locators_or_account('collaborationPageElements_1', 'select_opt2')
    select_opt3 = do_conf.get_locators_or_account('collaborationPageElements_1', 'select_opt3')
    # 登录按钮
    select_Btn = do_conf.get_locators_or_account('collaborationPageElements_1', 'select_Btn')

    # 选择密码登录的按钮
    select1 = do_conf.get_locators_or_account('collaborationPageElements_1', 'select1')
    select2 = do_conf.get_locators_or_account('collaborationPageElements_1', 'select2')
    select3 = do_conf.get_locators_or_account('collaborationPageElements_1', 'select3')
    select4 = do_conf.get_locators_or_account('collaborationPageElements_1', 'select4')
    select5 = do_conf.get_locators_or_account('collaborationPageElements_1', 'select5')
    select6 = do_conf.get_locators_or_account('collaborationPageElements_1', 'select6')
    # 登录按钮
    login_Btn = do_conf.get_locators_or_account('collaborationPageElements_1', 'login_Btn')

    detail_btn = do_conf.get_locators_or_account('collaborationPageElements_1', 'detail_btn')
    tel_btn = do_conf.get_locators_or_account('RecommendPageElements', 'tel_btn')
    email_btn = do_conf.get_locators_or_account('RecommendPageElements', 'email_btn')

    def click_select1_btn(self):
        return self.click(*CollaborationPage_1.select1)
    def click_select2_btn(self):
        return self.click(*CollaborationPage_1.select2)
    def click_select3_btn(self):
        return self.click(*CollaborationPage_1.select3)
    def click_select4_btn(self):
        return self.click(*CollaborationPage_1.select4)
    def click_select5_btn(self):
        return self.click(*CollaborationPage_1.select5)
    def click_select6_btn(self):
        return self.click(*CollaborationPage_1.select6)

    def click_select1_opt(self,value, type):
        return self.select_option(*CollaborationPage_1.select1[1:], value, type)
    def click_select2_opt(self,value, type):
        return self.select_option(*CollaborationPage_1.select2[1:], value, type)
    def click_select3_opt(self,value, type):
        return self.select_option(*CollaborationPage_1.select3[1:], value, type)
    def click_select4_opt(self,value, type):
        return self.select_option(*CollaborationPage_1.select4[1:], value, type)
    def click_select5_opt(self,value, type):
        return self.select_option(*CollaborationPage_1.select5[1:], value, type)
    def click_select6_opt(self,value, type):
        return self.select_option(*CollaborationPage_1.select6[1:], value, type)


class CollaborationPage_2(BasePage):
    # 配置文件读取元素
    do_conf = ParseConFile()
    select_opt1 = do_conf.get_locators_or_account('collaborationPageElements_1', 'select_opt1')
    select_opt2 = do_conf.get_locators_or_account('collaborationPageElements_1', 'select_opt2')
    select_opt3 = do_conf.get_locators_or_account('collaborationPageElements_1', 'select_opt3')
    # 登录按钮
    select_Btn = do_conf.get_locators_or_account('collaborationPageElements_1', 'select_Btn')

    # 选择密码登录的按钮
    select1 = do_conf.get_locators_or_account('collaborationPageElements_2', 'select1')
    select2 = do_conf.get_locators_or_account('collaborationPageElements_2', 'select2')
    select3 = do_conf.get_locators_or_account('collaborationPageElements_2', 'select3')
    select4 = do_conf.get_locators_or_account('collaborationPageElements_2', 'select4')
    select5 = do_conf.get_locators_or_account('collaborationPageElements_2', 'select5')
    select6 = do_conf.get_locators_or_account('collaborationPageElements_2', 'select6')
    # 登录按钮
    login_Btn = do_conf.get_locators_or_account('collaborationPageElements_2', 'login_Btn')

    detail_btn = do_conf.get_locators_or_account('collaborationPageElements_2', 'detail_btn')
    tel_btn = do_conf.get_locators_or_account('collaborationPageElements_2', 'tel_btn')
    email_btn = do_conf.get_locators_or_account('collaborationPageElements_2', 'email_btn')

    def click_select1_btn(self):
        return self.click(*CollaborationPage_2.select1)
    def click_select2_btn(self):
        return self.click(*CollaborationPage_2.select2)
    def click_select3_btn(self):
        return self.click(*CollaborationPage_2.select3)
    def click_select4_btn(self):
        return self.click(*CollaborationPage_2.select4)
    def click_select5_btn(self):
        return self.click(*CollaborationPage_2.select5)
    def click_select6_btn(self):
        return self.click(*CollaborationPage_2.select6)

    def click_select1_opt(self,value, type):
        return self.select_option(*CollaborationPage_2.select1[1:], value, type)
    def click_select2_opt(self,value, type):
        return self.select_option(*CollaborationPage_2.select2[1:], value, type)
    def click_select3_opt(self,value, type):
        return self.select_option(*CollaborationPage_2.select3[1:], value, type)
    def click_select4_opt(self,value, type):
        return self.select_option(*CollaborationPage_2.select4[1:], value, type)
    def click_select5_opt(self,value, type):
        return self.select_option(*CollaborationPage_2.select5[1:], value, type)
    def click_select6_opt(self,value, type):
        return self.select_option(*CollaborationPage_2.select6[1:], value, type)


if __name__ == "__main__":
    # RecommendPage =RecommendPage()
    # print(RecommendPage.select1)
    pass