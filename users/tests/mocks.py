from faker import Faker

fake = Faker()

test_user = {
    "username": fake.name(),
    "email": fake.email(),
    "password": fake.password(),
}

test_user_2 = {
    "username": fake.user_name(),
    "password": fake.password(),
    "email": fake.email(),
}
