__author__ = 'mucang'

from selenium.webdriver.common.by import By

class LoginLocator:
    '''
    登录页面元素定位表达式locator(定位方式,匹配表达式)
    '''

    #用户名输入框
    user_input = (By.NAME,"phone")

    #密码输入框
    pwd_input = (By.NAME,"password")

    #登录按钮
    login_button = (By.XPATH,'//div[@class="login-form"]//button[text()="登录"]')

    #from错误类型
    error_from = (By.CLASS_NAME,"form-error-info")

    #pageCenter错误类型
    error_pageCenter = (By.CLASS_NAME,"layui-layer-content")

    #验证码输入框
    verifyCode_input = (By.NAME,"vcode")

