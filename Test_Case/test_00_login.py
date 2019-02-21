__author__ = 'mucang'

import logging
import pytest
from PageObjects.index_Page import IndexPage
from Test_datas import login_case_data
from common.save_img import save_img



'''
登录测试用例类：不重新启动chrome，所有用例在一个chrome浏览器中完成，效率高（有适用条件）
'''



@pytest.mark.login
@pytest.mark.usefixtures("init_driver","init_loginPage")
class TestLogin():
    '''包含了login模块所有测试用例'''

    @pytest.mark.parametrize("data",login_case_data.error_data_form)
    def test_login_error_form(self,data,init_driver):
        '''异常登录【from错误提示】，测试用例步骤及断言实现一样的可以通过ddt来执行'''
        '''步骤:n'''
        logging.info("表单错误_登录测试_{0}".format(data))
        init_driver[1].login(data["username"],data["pwd"])
        '''断言'''
        try:
            assert data["check"] == init_driver[1].error_from_text()
            logging.info("测试通过")
            test_result = "PASS"
        except:
            logging.exception("测试失败")
            test_result = "FAIL"
            save_img(init_driver[0])
            raise
        finally:
            '''excel中写回测试结果'''
            logging.info('excel中写回测试结果')

    @pytest.mark.parametrize("data",login_case_data.error_data_pageCenter)
    def test_login_error_pageCenter(self,data,init_driver):
        '''异常登录【错误提示pageCenter-totast】，测试用例步骤及断言实现一样的可以通过ddt来执行'''
        '''步骤:'''
        logging.info("totast弹窗错误_登录测试_{0}".format(data))
        init_driver[1].login(data["username"],data["pwd"])
        '''断言'''
        try:
            assert data["check"] == init_driver[1].error_pageCenter_text()
            logging.info("测试通过")
            test_result = "PASS"
        except:
            logging.exception("测试失败")
            save_img(init_driver[0])
            test_result = "FAIL"
            raise
        finally:
            '''excel中写回测试结果'''
            logging.info('excel中写回测试结果')

    @pytest.mark.smoke
    def test_login_success(self,init_driver):
        '''正常登录'''
        '''步骤:'''
        ip = IndexPage(init_driver[0])
        logging.info("正常登录测试_{0}".format(login_case_data.success_data))
        init_driver[1].login(login_case_data.success_data["username"],login_case_data.success_data["pwd"])
        '''断言'''
        try:
            assert ip.member_is_exist()
            logging.info("测试通过")
            test_result = "PASS"
        except:
            test_result = "FAIL"
            logging.exception("测试失败")
            save_img(init_driver[0])
            raise
        finally:
            '''excel中写回测试结果'''
            logging.info('excel中写回测试结果')





