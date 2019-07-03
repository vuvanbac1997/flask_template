from datetime import datetime
from mongoengine import Document, DateField, IntField, ListField, BooleanField, StringField, FloatField
class Product(Document):
	meta = {'collection': 'product'}
	catalog_id = StringField()
	name = StringField()
	price = FloatField()
	discount = FloatField()
	image_link = StringField()
	image_list = ListField()
	view = IntField()

	active = BooleanField(default=True)
	create_date = DateField(default=datetime.now())