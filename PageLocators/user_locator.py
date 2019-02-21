__author__ = 'mucang'

from selenium.webdriver.common.by import By

class UserLocator:
    '''
    用户个人页元素定位表达式locator(定位方式,匹配表达式)
    '''

    #投资项目tab标题
    tz_tab = (By.XPATH,'//div[@class="deal_manage"]//div[@data-type="tz"]')

    #最近一条投资记录的标名称
    last_tz_id = (By.XPATH,'//div[@ms-controller="tz_list"]//table[@class="deal_mange_tab"]//tr[1]//div[@ms-html="item.title"]//a')

    #最近一条投资记录的金额
    last_tz_money = (By.XPATH,'//div[@ms-controller="tz_list"]//table[@class="deal_mange_tab"]//tr[1]//div[@ms-html="item.money"]')
