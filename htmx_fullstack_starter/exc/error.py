from htmx_fullstack_starter.exc.ec import BaseEC


class BusinessException(Exception):
    def __init__(self, ec: BaseEC):
        self.code = ec.get_code()
        self.msg = ec.get_msg()
