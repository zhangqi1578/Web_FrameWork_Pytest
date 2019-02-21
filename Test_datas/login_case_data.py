__author__ = '82739'

#正常登录
success_data = {"username":"18684720553","pwd":"python"}

#form错误提示：用户名为空、密码为空、用户名密码都为空、手机号格式不正确
error_data_form = [
    {"username":"","pwd":"python","check":"请输入手机号"},
    {"username":"18684720553","pwd":"","check":"请输入密码"},
    {"username":"","pwd":"","check":"请输入手机号"},
    {"username":"1868472055","pwd":"python","check":"请输入正确的手机号"},
    {"username":"186847205533","pwd":"python","check":"请输入正确的手机号"}
]

#pageCente-totast错误提示：账号不存在、密码错误
error_data_pageCenter = [
    {"username":"15731116810","pwd":"python","check":"此账号没有经过授权，请联系管理员!"},
    {"username":"18684720553","pwd":"123456","check":"帐号或密码错误!"}
]
