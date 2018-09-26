#!/usr/bin/env python
#Author:TangHu


#需求：（1）模拟登陆验证
#     （2）根据不同的页面采用不同的验证方式
Username = 'tanghulu'
Password = 'admin123'

def auth_login(auth_type):

    def out_wrapper(func):

        def wrapper(*args, **kwargs):

            if auth_type=="local":
                print("开始采用本地验证了。。。。")
                username = input("请输入您的用户名：").strip()
                password = input("请输入您的密码：").strip()

                if username == Username and password == Password:
                    print("\033[32;1m验证成功，欢迎进入\033[0m")
                    res = func(*args, **kwargs)
                    return res
                else:
                    exit("\033[31;1m验证失败，账户或密码错误\033[0m")
            elif auth_type=="ldap":
                print("开始采用ldap验证了。。。。")
                username = input("请输入您的用户名：").strip()
                password = input("请输入您的密码：").strip()

                if username == Username and password == Password:
                    print("\033[32;1m验证成功，欢迎进入\033[0m")
                    res = func(*args, **kwargs)
                    return res
                else:
                    exit("\033[31;1m验证失败，账户或密码错误\033[0m")
        return wrapper
    return out_wrapper


@auth_login(auth_type="local")
def index():
    print("This Is first index page....")
    return "from in the index...."
@auth_login(auth_type="ldap")
def home():
    print("This Is home page....")

@auth_login(auth_type="local")
def traffic():
    print("This Is traffic page....")



print(index())

home()

traffic()