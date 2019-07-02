from mongoengine import Document, StringField, FloatField, IntField, ListField
class Product(Document):
	meta = {'collection': 'product'}
	catalog_id = StringField()
	name = StringField()
	price = FloatField()
	discount = FloatField()
	image_link = StringField()
	image_list = ListField()
	view = IntField()
