"""
------------------------------------
@Time :
@Auth :
@File : HomePage.py
@IDE  : PyCharm
@Motto:
------------------------------------
"""
from time import sleep

from Page.BasePage import BasePage
from util.parseConFile import ParseConFile


class HomePage(BasePage):
    # 配置文件读取元素
    do_conf = ParseConFile()
    # 左上角登录icon
    loginIcon = do_conf.get_locators_or_account('HomePageElements', 'loginIcon')
    # 菜单栏
    # 首页
    top = do_conf.get_locators_or_account('HomePageElements', 'top')
    # 推荐
    recommend = do_conf.get_locators_or_account('HomePageElements', 'recommend')
    # 援助
    collaboration = do_conf.get_locators_or_account('HomePageElements', 'collaboration')
    # 社区
    community = do_conf.get_locators_or_account('HomePageElements', 'community')
    # 个人主页
    myPage = do_conf.get_locators_or_account('HomePageElements', 'myPage')

    # 图片点击
    # 推荐
    pic_recommend = do_conf.get_locators_or_account('HomePageElements', 'pic_recommend')
    # 援助-need
    pic_collaboration_needs = do_conf.get_locators_or_account('HomePageElements', 'pic_collaboration_needs')
    # 社区
    pic_community = do_conf.get_locators_or_account('HomePageElements', 'pic_community')
    # 援助-help
    pic_collaboration_help = do_conf.get_locators_or_account('HomePageElements', 'pic_collaboration_help')

    def select_menu(self, menu=''):
        if menu == "top":
            self.click_top_menu()
        elif menu == 'recommend':
            self.click_recommend_menu()
        elif menu == 'collaboration':
            self.click_collaboration_menu()
        elif menu == 'community':
            self.click_community_menu()
        elif menu == 'myPage':
            self.click_myPage_menu()
        elif menu == 'pic_recommend':
            self.click_pic_recommend()
        elif menu == 'pic_collaboration_needs':
            self.click_pic_collaboration_needs()
        elif menu == 'pic_community':
            self.click_pic_community()
        elif menu == 'pic_collaboration_help':
            self.click_pic_collaboration_help()
        else:
            raise ValueError(
                '''菜单选择错误!
                top->首页
                recommend->推荐
                collaboration->援助
                community->社区
                myPage->个人主页'''
            )

    def click_top_menu(self):
        print("top的位置地址是：", *HomePage.top)
        return self.click(*HomePage.top)

    def click_recommend_menu(self):
        print("recommend的位置地址是", *HomePage.recommend)
        return self.click(*HomePage.recommend)

    def click_collaboration_menu(self):
        print("collaboration的位置地址是", *HomePage.collaboration)
        return self.click(*HomePage.collaboration)

    def click_community_menu(self):
        print("community的位置地址是", *HomePage.community)
        return self.click(*HomePage.community)

    def click_myPage_menu(self):
        print("myPage的位置地址是", *HomePage.myPage)
        return self.click(*HomePage.myPage)

    def click_pic_recommend(self):
        print("pic_recommend的位置地址是：",*HomePage.pic_recommend)
        return self.click(*HomePage.pic_recommend)

    def click_pic_collaboration_needs(self):
        print("recommend的位置地址是", *HomePage.pic_collaboration_needs)
        return self.click(*HomePage.pic_collaboration_needs)

    def click_pic_community(self):
        print("collaboration的位置地址是", *HomePage.pic_community)
        return self.click(*HomePage.pic_community)

    def click_pic_collaboration_help(self):
        print("community的位置地址是", *HomePage.pic_collaboration_help)
        return self.click(*HomePage.pic_collaboration_help)


if __name__ == '__main__':
    # print(*HomePage.top)
    print(*HomePage.top[1:])
