import msgspec


class SuperUserLogin(msgspec.Struct):
    username: str
    password: str


class SuperUserOut(msgspec.Struct):
    user_id: int
    username: str
