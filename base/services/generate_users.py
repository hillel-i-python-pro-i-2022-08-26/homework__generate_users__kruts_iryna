import random
from typing import Any

from faker import Faker

from base.services.user import User

faker = Faker()

def generate_users() -> tuple[Any, Any]:
    rand_name = faker.unique.first_name().lower()
    rand_surname = faker.unique.last_name().lower()
    return User(rand_name+'_'+rand_surname,
                ((rand_name+'_'+rand_surname).lower()+'@example.com'),
                rand_name.lower()[:5]+str(random.randint(1000, 2023)))







