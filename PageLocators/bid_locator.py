__author__ = 'mucang'

from selenium.webdriver.common.by import By

class BidLocator:
    '''
    标详情页元素定位表达式locator(定位方式,匹配表达式)
    '''

    #投资金额输入框
    money_input = (By.XPATH,'//input[contains(@class,"invest-unit-investinput")]')

    #投标按钮
    bid_button = (By.XPATH,'//div[@class="body"]//button')

    #投标金额输入错误的提示弹窗文案
    error_data_popUp = (By.XPATH,'//div[@class="layui-layer-content"]')

    #投资成功弹窗的查看并激活按钮
    success_button = (By.XPATH,'//div[@class="layui-layer-content"]//button')
