from mongoengine import Document, StringField, EmailField, DateField, BooleanField


class User(Document):
    meta = {'collection': 'user'}
    username = StringField(required=True)
    password = StringField(min_length=3)
    email = EmailField()
    contact = StringField(default='')
    address = StringField(default='')
    role = StringField(default='')
    image = StringField(default='')
    create_date = DateField()
    active = BooleanField(default=True)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)
