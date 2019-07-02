from mongoengine import Document, StringField
class Catalog(Document):
	meta = {'collection': 'catalog'}
	name = StringField()
