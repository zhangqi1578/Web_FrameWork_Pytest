__author__ = 'mucang'

from PageLocators.user_locator import UserLocator
from common.base_page import BasePage

'''
用户操作
'''
class UserPage(BasePage):
    '''
    用户页面业务操作
    '''

    '''点击投资记录tab'''
    def click_Tz_tab(self):
        #方法标识，用来在底层操作出现异常时，定位日志问题
        model = "首页_click_Tz_tab"
        self.click_element(UserLocator.tz_tab,model=model)

    '''获取最近一条投资记录的标id'''
    def get_lastTz_id(self):
        #方法标识，用来在底层操作出现异常时，定位日志问题
        model = "首页_get_lastTz_id"
        self.wait_eleVisible(UserLocator.last_tz_id,model=model)
        bid_id_text = self.get_eleAttribute(UserLocator.last_tz_id,"href",model=model)
        return bid_id_text[-9:-5]

    '''获取最近一条投资记录的投资金额'''
    def get_lastTz_money(self):
        #方法标识，用来在底层操作出现异常时，定位日志问题
        model = "首页_get_lastTz_money"
        self.wait_eleVisible(UserLocator.last_tz_money,model=model)
        money_text = self.get_eleText(UserLocator.last_tz_money,model=model)
        return str(int(float(money_text.replace(",",""))))
