from typing import NamedTuple


class User(NamedTuple):
    user_login: str
    email: str
    password: int

    def __str__(self):
        return (
            f"Login: {self.user_login}. Email: {self.email}. Password: {self.password}"
        )
