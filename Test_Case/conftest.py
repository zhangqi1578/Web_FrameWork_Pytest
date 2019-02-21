__author__ = 'mucang'

import pytest
import logging
from selenium import webdriver
from PageUrl import page_url
from PageObjects.login_Page import LoginPage
from PageObjects.index_Page import IndexPage
from PageObjects.bid_Page import BidPage
from Test_datas import common_datas

driver = None

@pytest.fixture(scope="class")
def init_driver():
    global driver
    logging.info("初始化chrome浏览器")
    driver = webdriver.Chrome()
    driver.maximize_window()
    lp = LoginPage(driver)
    yield (driver,lp)
    logging.info("关闭chrome浏览器")
    driver.quit()

@pytest.fixture
def init_loginPage():
    global driver
    logging.info("执行测试用例,进入前程贷登录页面")
    driver.get(page_url.login_page_url)
    yield
    logging.info("用例执行完成")


@pytest.fixture(scope="class")
def init_login():
    global driver
    logging.info("进入前程贷登录页面，登录系统")
    driver.get(page_url.login_page_url)
    lp = LoginPage(driver)
    lp.login(common_datas.common_user,common_datas.common_pwd)
    ip = IndexPage(driver)
    ip.click_bid_button()
    yield ip

@pytest.fixture
def init_bidPage():
    global driver
    logging.info("执行测试")
    logging.info("获取标的相关信息：标余额，用户余额，标id")
    bp = BidPage(driver)
    bid_left_money = bp.get_bid_left_money()
    user_left_money = bp.get_user_left_money()
    bid_id = bp.get_bid_id()
    yield (bid_left_money,user_left_money,bid_id)
    logging.info("刷新标页面")
    driver.refresh()




