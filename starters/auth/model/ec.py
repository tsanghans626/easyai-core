from starters.exc import BaseEC


class AuthEC(BaseEC):
    LOGIN_FAILED = (100000, "登陆失败")
