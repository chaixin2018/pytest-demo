"""
------------------------------------
@Time :
@Auth :
@File : login_data.py
@IDE  : PyCharm
@Motto:
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""
class LoginData(object):
    """用户登录测试数据
    用户名，密码，期待值"""
    login_success_data = [
        ("daido1","daido001","ログアウト"),
        ("daido2","daido002","ログアウト"),
        ("daido3","daido003","ログアウト")]

    login_fail_user_data = [
        ("1","daido001","对不起！用户名有误,用户名长度不能小于3位！"), #用户名小于三位
        ("","daido001","对不起！请输入用户名！")] #用户名为空

    login_fail_password_data = [
        ("1","1","对不起！密码长度不能小于6位！"), #密码小于三位
        ("","","对不起！请输入密码！")] #密码为空

if __name__ == '__main__':
    testdata = LoginData
    print(LoginData.login_success_data)
    print(LoginData.login_success_data[0][0])
    print(LoginData.login_success_data[0][1])
    print(LoginData.login_success_data[0][2])




