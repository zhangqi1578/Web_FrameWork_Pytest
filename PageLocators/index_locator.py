__author__ = 'mucang'

from selenium.webdriver.common.by import By

class IndexLocator:
    '''
    首页页面元素定位表达式locator(定位方式,匹配表达式)
    '''

    #我的账户
    my_user = (By.XPATH,'//a[@href="/Member/index.html"]')

    #首页第一个标的抢投标按钮
    bid_button = (By.XPATH,'//a[text()="抢投标"]')