"""
------------------------------------
@Time :
@Auth :
@File : contact_data.py
@IDE  : PyCharm
@Motto:
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""


class ContactData(object):
    """添加联系人测试数据"""

    add_contact_success = [
        (
            "recommend",
            "281754041@qq.com",
            "1",
            "13691579841",
            "添加联系人1",
            "281754041@qq.com"
        )
    ]
    add_contact_fail = [
        (
            "linux2",
            "@qq.com",
            "0",
            "13691579842",
            "添加联系人2",
            "请正确填写邮件地址。"
        )
    ]


if __name__ == '__main__':
    test_data = ContactData()
    print(test_data.add_contact_success)
    print(test_data.add_contact_success[0][0])
