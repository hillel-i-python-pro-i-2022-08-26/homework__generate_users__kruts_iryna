import random

from faker import Faker

from apps.base.services.user import User

faker = Faker()


def generate_user() -> User:
    random_name = faker.unique.first_name().lower()
    random_surname = faker.unique.last_name().lower()
    return User(
        random_name + "_" + random_surname,
        ((random_name + "_" + random_surname).lower() + "@example.com"),
        random_name.lower()[:5] + str(random.randint(1900, 2023)),
    )
