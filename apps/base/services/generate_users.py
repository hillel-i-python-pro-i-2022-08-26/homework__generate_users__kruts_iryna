import random
from typing import Any

from faker import Faker

from apps.base.services.user import User

faker = Faker()


def generate_users() -> tuple[Any, Any]:
    rand_name = faker.unique.first_name().lower()
    rand_surname = faker.unique.last_name().lower()
    yield User(rand_name + '_' + rand_surname,
               ((rand_name + '_' + rand_surname).lower() + '@example.com'),
               rand_name.lower()[:5] + str(random.randint(1900, 2023)))
