from mongoengine import Document, StringField, DateField, BooleanField, DictField
from datetime import datetime

class Post(Document):
    meta = {'collection': 'post'}
    title = StringField(default='')
    content = StringField(default='')
    create_date = DateField(default=datetime.now())
    active = BooleanField(default=True)
