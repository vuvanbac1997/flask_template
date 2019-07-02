from mongoengine import Document, StringField, DateField, BooleanField, DictField


class Post(Document):
    meta = {'collection': 'post'}
    title = StringField(default='')
    content = StringField(default='')
    create_date = DateField()
    active = BooleanField(default=True)
