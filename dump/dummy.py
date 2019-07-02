from models.user import User
from models.post import Post
from faker import Faker, Factory
from datetime import datetime
fake = Faker()


def dump_post():
    for x in range(25):
        title = fake.name()
        content = fake.text()
        create_date = datetime.now()
        Post(title=title, content=content, create_date=create_date).save()

