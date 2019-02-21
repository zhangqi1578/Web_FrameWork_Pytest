__author__ = 'mucang'


from PageLocators.index_locator import IndexLocator
from common.base_page import BasePage

'''
首页操作
'''
class IndexPage(BasePage):
    '''
    首页业务层操作
    '''

    '''判断首页中我的账户元素是否存在'''
    def member_is_exist(self):
        #方法标识，用来在底层操作出现异常时，定位日志问题
        model = "首页_member_is_exist"
        return self.wait_eleVisible(IndexLocator.my_user,model=model)

    '''点击标的抢投标按钮'''
    def click_bid_button(self):
        #方法标识，用来在底层操作出现异常时，定位日志问题
        model = "首页_click_bid_button"
        self.click_element(IndexLocator.bid_button,model=model)




