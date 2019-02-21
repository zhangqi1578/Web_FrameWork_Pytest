__author__ = 'mucang'

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common import file_path
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from common import logging_config
import logging






class BasePage:

    def __init__(self,driver):
        self.driver = driver


    def save_webImg(self,model):
        logging.info("错误截图...")
        if model == None:
            filename = file_path.screenshot_path+"\{0}_{1}.png".format("未知功能",time.strftime("%Y%m%d%H%M%S"))
        else:
            filename = file_path.screenshot_path+"\{0}_{1}.png".format(model,time.strftime("%Y%m%d%H%M%S"))
        try:
            self.driver.save_screenshot(filename)
            logging.info("截图文件：{0}".format(filename))
        except:
            logging.exception("截图失败!!!")
            raise

    #等待元素可见
    def wait_eleVisible(self,loc,timeout=30,poll_frequency=0.5,model=None):
        logging.info("等待元素:({0})".format(model))
        try:
            start = time.time()
            WebDriverWait(self.driver,timeout,poll_frequency).until(EC.visibility_of_element_located(loc))
            end = time.time()
            logging.info("等待元素成功:{0}，用时:{1}".format(model,(end-start)))
            return True
        except:
            self.save_webImg(model)
            logging.exception("等待元素失败:({0})".format(model))
            raise

    def find_element(self,loc,model=None):
        logging.info("查找元素:({0})".format(model))
        try:
            return self.driver.find_element(*loc)
        except:
            self.save_webImg(model)
            logging.exception("查找元素失败:({0})".format(model))
            raise

    def click_element(self,loc,timeout=30,poll_frequency=0.5,model=None):
        logging.info("点击元素:({0})".format(model))
        try:
            WebDriverWait(self.driver,timeout,poll_frequency).until(EC.element_to_be_clickable(loc)).click()
            logging.info("点击元素成功:({0})".format(model))
        except:
            logging.exception("点击元素失败:({0})".format(model))
            self.save_webImg(model)
            raise

    def clear_input_text(self,loc,model=None):
        ele = self.find_element(loc,model)
        logging.info("清空输入框文本:({0})".format(model))
        try:
            ele.clear()
            logging.info("清空输入框成功:({0})".format(model))
        except:
            logging.exception("清空输入框失败:({0})".format(model))
            self.save_webImg(model)
            raise

    def send_keys(self,loc,text,model=None):
        ele = self.find_element(loc,model)
        logging.info("{0}_输入文本:{1}".format(model,text))
        try:
            ele.send_keys(text)
            logging.info("{0}_输入文本成功:{1}".format(model,text))
        except:
            logging.exception("{0}_输入文本失败:{1}".format(model,text))
            self.save_webImg(model)
            raise

    def get_eleText(self,loc,model=None):
        ele = self.find_element(loc,model)
        logging.info("获取元素文本:({0})".format(model))
        try:
            return ele.text
        except:
            logging.exception("获取元素文本失败:({0})".format(model))
            self.save_webImg(model)
            raise

    def get_eleAttribute(self,loc,name,model=None):
        ele = self.find_element(loc,model)
        logging.info("{0}_获取元素属性:{0}".format(model,name))
        try:
            return ele.get_attribute(name)
        except:
            logging.exception("{0}_获取元素属性失败:{0}".format(model,name))
            self.save_webImg(model)
            raise

    def switch_to_alert(self,timeout=30,poll_frequency=0.5,model=None):
        logging.info("{0}_切换alert弹窗".format(model))
        try:
            return WebDriverWait(timeout,poll_frequency).until(EC.alert_is_present())
        except:
            logging.exception("{0}_切换alert弹窗失败".format(model))
            self.save_webImg(model)
            raise

    def switch_to_frame(self,frame_reference,timeout=30,poll_frequency=0.5,model=None):
        logging.info("{0}_切换iframe".format(model))
        try:
            WebDriverWait(timeout,poll_frequency).until(EC.frame_to_be_available_and_switch_to_it(frame_reference))
        except:
            logging.exception("{0}_切换iframe".format(model))
            self.save_webImg(model)
            raise

    def switch_to_window(self,window_reference,timeout=30,poll_frequency=0.5,window_handles=None,model=None):
        '''

        :param window_reference:
        :param timeout:
        :param poll_frequency:
        :param model:
        :return:
        '''
        logging.info("{0}_切换窗口".format(model))
        try:
            if window_reference == "new":
                if window_handles:
                    WebDriverWait(timeout,poll_frequency).until(EC.new_window_is_opened(window_handles))
                    current_window_handles = self.driver.window_handles
                    self.driver.switch_to.window(current_window_handles[-1])
                else:
                    logging.exception("打开新窗口时，请传入window_handles参数")
                    raise ("打开新窗口时，请传入window_handles参数")
            elif window_reference == "default":
                self.driver.switch_to.default_content()
            else:
                self.driver.switch_to.window(window_reference)
            logging.info("{0}_切换窗口成功".format(model))
        except:
            logging.exception("{0}_切换窗口失败".format(model))
            self.save_webImg(model)
            raise














