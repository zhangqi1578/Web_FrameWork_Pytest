__author__ = 'mucang'

from PageLocators.login_locator import LoginLocator
from common.base_page import BasePage

'''
登录操作
'''
class LoginPage(BasePage):
    '''
    登录页面业务操作
    '''


    '''登录操作'''
    def login(self,username,passward):
        #方法标识，用来在底层操作出现异常时，定位日志问题
        model = "登录页_login"
        #等待用户名输入框清空并输入
        self.wait_eleVisible(LoginLocator.user_input,model=model)
        self.clear_input_text(LoginLocator.user_input,model=model)
        self.send_keys(LoginLocator.user_input,username,model)
        #等待密码输入框清空并输入
        self.wait_eleVisible(LoginLocator.pwd_input,model=model)
        self.clear_input_text(LoginLocator.pwd_input,model=model)
        self.send_keys(LoginLocator.pwd_input,passward,model=model)
        #等待登录按钮并点击
        self.click_element(LoginLocator.login_button,model=model)

    '''判断form错误提示文案'''
    def error_from_text(self):
        #方法标识，用来在底层操作出现异常时，定位日志问题
        model = "登录页_error_from_text"
        self.wait_eleVisible(LoginLocator.error_from,model=model)
        return self.get_eleText(LoginLocator.error_from,model=model)

    '''判断pageCenter错误提示文案'''
    def error_pageCenter_text(self):
        #方法标识，用来在底层操作出现异常时，定位日志问题
        model = "登录页_error_pageCenter_text"
        self.wait_eleVisible(LoginLocator.error_pageCenter,model=model)
        return self.get_eleText(LoginLocator.error_pageCenter,model=model)

    '''图片验证码输入框是否存在'''
    def verifyCode_input_is_exist(self):
        model = "登录页_verifyCode_input_is_exist"
        self.wait_eleVisible(LoginLocator.verifyCode_input,model=model)
        return self.wait_eleVisible(LoginLocator.verifyCode_input,model=model)




