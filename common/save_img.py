__author__ = 'mucang'

from common import file_path
import time
import logging




def save_img(driver,model=None):
    logging.info("用例失败截图:{0}".format(model))
    try:
        filename = file_path.screenshot_path+"\{0}_{1}.png".format(model,time.strftime("%Y%m%d%H%M%S"))
        driver.save_screenshot(filename)
        logging.info("截图文件：{0}".format(filename))
    except:
        logging.info("截图失败!!!")
        raise