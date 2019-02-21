__author__ = 'mucang'

#正常投资
success_data = {"money":"1000"}

#弹窗错误提示：0投资、投资不为100倍数、投资金额大于标剩余金额、投标金额大于用户余额
error_data_popUp = [
    {"money":"0","check":"请正确填写投标金额"},
    {"money":"1050","check":"投标金额必须为100的倍数"},
    {"money":"moreBidLeft","check":"购买标的金额不能大于标剩余金额"},
    {"money":"moreUserLeft","check":"投标金额大于可用金额"},

]

#button错误提示：投资不为10整数倍
error_data_button = {"money":"555","check":"请输入10的整数倍"}
