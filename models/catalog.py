from datetime import datetime
from mongoengine import Document, DateField, BooleanField, StringField
class Catalog(Document):
	meta = {'collection': 'catalog'}
	name = StringField()

	active = BooleanField(default=True)
	create_date = DateField(default=datetime.now())