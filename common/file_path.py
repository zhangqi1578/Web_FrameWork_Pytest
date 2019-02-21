__author__ = 'mucang'

import os

project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

logs_path = os.path.join(project_path,"result","logs")

screenshot_path = os.path.join(project_path,"result","screenshots")

test_report_path = os.path.join(project_path,"result","test_report")

test_allureReport_path = os.path.join(project_path,"result","allure_report")


if __name__ == '__main__':
    print(screenshot_path)