# -*- coding: utf-8 -*-
# @Time    : 2018/10/21 19:49
# @Author  : pyj
# @FileName: my_log
# @Software: PyCharm
import logging
from common import file_path


class MyLog:
    def my_log(self, level, msg):
        my_logger=logging.getLogger("python10")
        my_logger.setLevel("DEBUG")

        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')

        ch = logging.StreamHandler()  # 输出到控制台
        ch.setLevel("DEBUG")  # 设置输出级别  大写
        ch.setFormatter(formatter)

        fh = logging.FileHandler(file_path.logs_path+"/Web_Autotest.log", encoding='UTF-8')  # 输出到制定文件
        fh.setLevel("DEBUG")  # 设置输出级别  大写
        fh.setFormatter(formatter)

        # 对接起来 给日志收集器添加一个渠道
        my_logger.addHandler(ch)
        my_logger.addHandler(fh)

        if level == 'DEBUG':
            my_logger.debug(msg)
        elif level == 'INFO':
            my_logger.info(msg)
        elif level == 'WARNING':
            my_logger.warning(msg)
        elif level == 'ERROR':
            my_logger.error(msg)
        elif level == 'CRITICAL':
            my_logger.critical(msg)

        # #渠道要记得移除掉 否则 日志输出会重复
        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)

    def debug(self, msg):
        self.my_log("DEBUG", msg)

    def info(self, msg):
        self.my_log("INFO", msg)

    def warning(self, msg):
        self.my_log("ERROR", msg)

    def error(self, msg):
        self.my_log("WARNING", msg)

    def critical(self, msg):
        self.my_log("CRITICAL", msg)


if __name__ == '__main__':
    my_logger = MyLog()
    my_logger.debug("天啦噜，水滴同学没有见过日志！")  # 收集
    my_logger.info("小场面 ，不要慌！")  # print
    my_logger.warning("这么巧，Monica陪着水滴没见过日志！")
    my_logger.error("华华要生气了！")
    my_logger.critical("讲了100遍，还不懂，华华要奔溃了！")
