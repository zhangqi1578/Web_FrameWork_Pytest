__author__ = 'mucang'


import logging
from PageObjects.bid_Page import BidPage
from PageObjects.user_Page import UserPage
from Test_datas import invest_case_data

import pytest
from common.save_img import save_img


@pytest.mark.invest
@pytest.mark.usefixtures("init_driver","init_login","init_bidPage")
class TestInvest():

    @pytest.mark.parametrize("data",invest_case_data.error_data_popUp)
    def test_invest_error_popUp(self,data,init_driver,init_bidPage):
        logging.info("投标测试_投资失败_弹窗提示：{0}".format(data))

        if data["money"] == "moreBidLeft":
            logging.info("moreBidLeft数据替换为：{0}".format(str(int(init_bidPage[0])+100)))
            data["money"] = str(int(init_bidPage[0])+100)
        elif data["money"] == "moreUserLeft":
            logging.info("moreUserLeft数据替换为：{0}".format(str((int(float(init_bidPage[1]))//100+1)*100)))
            data["money"] = str((int(float(init_bidPage[1]))//100+1)*100)
        bp = BidPage(init_driver[0])
        bp.input_money(data["money"])
        bp.click_invest_button()
        try:
            assert data["check"] == bp.get_errorPopUp_text()
            logging.info("测试通过")
            test_result = "PASS"
        except:
            logging.exception("测试失败")
            save_img(init_driver[0])
            test_result = "FAIL"
            raise
        finally:
            '''写回测试结果'''
            logging.info("excel写回测试结果")

    def test_invest_error_button(self,init_driver):
        logging.info("投标测试_投资失败_投标按钮提示：{0}".format(invest_case_data.error_data_button))
        bp = BidPage(init_driver[0])
        bp.input_money(invest_case_data.error_data_button["money"])
        try:
            assert invest_case_data.error_data_button["check"] == bp.get_bidButton_text()
            logging.info("测试通过")
            test_result = "PASS"
        except:
            logging.exception("测试失败")
            test_result = "FAIL"
            save_img(init_driver[0])
            raise
        finally:
            '''写回测试结果'''
            logging.info("excel写回测试结果")

    @pytest.mark.smoke
    def test_invest_success(self,init_driver,init_bidPage):
        '''
        成功投标测试用例
        :return:
        ''''''
        :return:
        '''
        bp = BidPage(init_driver[0])
        up = UserPage(init_driver[0])
        logging.info("投标测试_投资成功：{0}".format(invest_case_data.success_data))
        bp.input_money(invest_case_data.success_data["money"])
        bp.click_invest_button()
        bp.click_success_button()
        up.click_Tz_tab()
        TZ_info = (up.get_lastTz_id(),up.get_lastTz_money())
        try:
            assert (init_bidPage[2],invest_case_data.success_data["money"]) == TZ_info
            logging.info("测试通过")
            test_result = "PASS"
        except:
            logging.exception("测试失败")
            test_result = "FAIL"
            save_img(init_driver[0])
            raise
        finally:
            '''写回测试结果'''
            logging.info("excel写回测试结果")




