__author__ = 'mucang'


import pytest
from common import file_path

pytest.main([
             # "-m invest",
             "--html={0}/report.html".format(file_path.test_report_path),
             "--junitxml={0}/report.xml".format(file_path.test_report_path),
             "--alluredir={0}".format(file_path.test_allureReport_path),
             "--reruns","2","--reruns-delay","5"]
)

