"""
------------------------------------
@Time :
@Auth :
@File : MyPage.py
@IDE  : PyCharm
@Motto:
------------------------------------
"""
from time import sleep

from Page.BasePage import BasePage
from util.parseConFile import ParseConFile


class MyPage(BasePage):
    # 配置文件读取元素
    do_conf = ParseConFile()
    # 左上角登录icon
    iamC = do_conf.get_locators_or_account('MyPageElements', 'iamC')
    # 首页
    manage = do_conf.get_locators_or_account('MyPageElements', 'manage')
    # 推荐
    message = do_conf.get_locators_or_account('MyPageElements', 'message')
    # 援助
    info = do_conf.get_locators_or_account('MyPageElements', 'info')
    # 社区
    iamS = do_conf.get_locators_or_account('MyPageElements', 'iamS')


    # 推荐
    iamC_Center = do_conf.get_locators_or_account('MyPageElements', 'iamC_Center')
    # 援助-need
    iamC_Order = do_conf.get_locators_or_account('MyPageElements', 'iamC_Order')
    # 社区
    iamC_Evaluation = do_conf.get_locators_or_account('MyPageElements', 'iamC_Evaluation')
    # 援助-help
    iamC_Refund = do_conf.get_locators_or_account('MyPageElements', 'iamC_Refund')
    # 援助-help
    iamC_ReportT = do_conf.get_locators_or_account('MyPageElements', 'iamC_ReportT')
    # 援助-help
    iamC_FReport = do_conf.get_locators_or_account('MyPageElements', 'iamC_FReport')

    def my_page_select_menu(self, menu=''):
        if menu == "iamC":
            self.click_iamC()
        elif menu == 'manage':
            self.click_manage()
        elif menu == 'message':
            self.click_message()
        elif menu == 'info':
            self.click_info()
        elif menu == 'iamS':
            self.click_iamS()
        # elif menu == 'iamC_Center':
        #     self.click_iamC_Center()
        # elif menu == 'iamC_Order':
        #     self.click_iamC_Order()
        # elif menu == 'iamC_Evaluation':
        #     self.click_iamC_Evaluation()
        # elif menu == 'iamC_Refund':
        #     self.click_iamC_Refund()
        # elif menu == 'iamC_ReportT':
        #     self.click_iamC_ReportT()
        # elif menu == 'iamC_FReport':
        #     self.click_iamC_FReport()
        # else:
        #     pass

    def click_iamC(self):
        print("iamC的位置地址是：", *MyPage.iamC)
        return self.click(*MyPage.iamC)

    def click_manage(self):
        print("manage的位置地址是", *MyPage.manage)
        return self.click(*MyPage.manage)

    def click_message(self):
        print("message的位置地址是", *MyPage.message)
        return self.click(*MyPage.message)

    def click_info(self):
        print("info的位置地址是", *MyPage.info)
        return self.click(*MyPage.info)
    
    def click_iamS(self):
        print("iamS的位置地址是", *MyPage.iamS)
        return self.click(*MyPage.iamS)


    def click_iamC_Center(self):
        print("iamC_Center的位置地址是：",*MyPage.iamC_Center)
        return self.click(*MyPage.iamC_Center)

    def click_iamC_Order(self):
        print("recommend的位置地址是", *MyPage.iamC_Order)
        return self.click(*MyPage.iamC_Order)

    def click_iamC_Evaluation(self):
        print("message的位置地址是", *MyPage.iamC_Evaluation)
        return self.click(*MyPage.iamC_Evaluation)

    def click_iamC_Refund(self):
        print("message的位置地址是", *MyPage.iamC_Refund)
        return self.click(*MyPage.iamC_Refund)

    def click_iamC_ReportT(self):
        print("message的位置地址是", *MyPage.iamC_ReportT)
        return self.click(*MyPage.iamC_ReportT)

    def click_iamC_FReport(self):
        print("message的位置地址是", *MyPage.iamC_FReport)
        return self.click(*MyPage.iamC_FReport)

if __name__ == '__main__':
    # print(*MyPage.top)
    print(*MyPage.top[1:])
