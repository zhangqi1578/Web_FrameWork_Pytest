__author__ = 'mucang'


from PageLocators.bid_locator import BidLocator
from common.base_page import BasePage


'''
表详情页面操作
'''
class BidPage(BasePage):
    '''
    标详情页面业务操作
    '''

    '''对标进行输入金额操作'''
    def input_money(self,money):
        #方法标识，用来在底层操作出现异常时，定位日志问题
        model = "登录页_input_money"
        self.wait_eleVisible(BidLocator.money_input,model=model)
        self.send_keys(BidLocator.money_input,money,model=model)

    '''点击投资按钮'''
    def click_invest_button(self):
        #方法标识，用来在底层操作出现异常时，定位日志问题
        model = "登录页_click_invest_button"
        self.click_element(BidLocator.bid_button,model=model)

    '''点击投标成功的查看并激活按钮'''
    def click_success_button(self):
        #方法标识，用来在底层操作出现异常时，定位日志问题
        model = "登录页_click_success_button"
        self.click_element(BidLocator.success_button,model=model)

    '''获取标剩余钱数'''
    def get_bid_left_money(self):
        #方法标识，用来在底层操作出现异常时，定位日志问题
        model = "登录页_get_bid_left_money"
        self.wait_eleVisible(BidLocator.money_input,model=model)
        return self.get_eleAttribute(BidLocator.money_input,"data-left",model=model)

    '''获取用户剩余钱数'''
    def get_user_left_money(self):
        #方法标识，用来在底层操作出现异常时，定位日志问题
        model = "登录页_get_user_left_money"
        self.wait_eleVisible(BidLocator.money_input,model=model)
        return self.get_eleAttribute(BidLocator.money_input,"data-amount",model=model)

    '''获取标id'''
    def get_bid_id(self):
        #方法标识，用来在底层操作出现异常时，定位日志问题
        model = "登录页_get_bid_id"
        self.wait_eleVisible(BidLocator.money_input,model=model)
        return self.get_eleAttribute(BidLocator.money_input,"data-id",model=model)

    '''获取投标按钮的文案'''
    def get_bidButton_text(self):
        #方法标识，用来在底层操作出现异常时，定位日志问题
        model = "登录页_get_bidButton_text"
        self.wait_eleVisible(BidLocator.bid_button,model=model)
        return self.get_eleText(BidLocator.bid_button,model=model)

    '''获取错误提示弹窗的文案'''
    def get_errorPopUp_text(self):
        #方法标识，用来在底层操作出现异常时，定位日志问题
        model = "登录页_get_errorPopUp_text"
        self.wait_eleVisible(BidLocator.error_data_popUp,model=model)
        return self.get_eleText(BidLocator.error_data_popUp,model=model)
