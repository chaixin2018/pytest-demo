"""
------------------------------------
@Time : 2020/9/15 14:43
@Auth : chai
@File : home_page_data.py
@IDE  : PyCharm
------------------------------------
"""


class HomePageData(object):
    """选择菜单功能
    现在没做断言判断，因为没有界面统一的位置标记，等有了再断言"""

    menu_select = [
        ("recommend", "お困り事"),
        ("collaboration", "ビジネスパートナーに求める条件を選択してください"),
        ("community", "欢迎来中小企業エコシステム"),
        ("myPage", "雇主中心"),
        ("pic_recommend", "お困り事"),
        ("pic_collaboration_needs", "販売代理店の開拓"),
        ("pic_community", "欢迎来中小企業エコシステム"),
        ("pic_collaboration_help", "人気商材の探し")]


if __name__ == '__main__':
    test_data = HomePageData()
    print(test_data.menu_select)
    print(test_data.menu_select[0][0])





