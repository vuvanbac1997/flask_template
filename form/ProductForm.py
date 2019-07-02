from wtforms import Form, validators, StringField 
class ProductForm(Form):
	catalog_id = StringField('Catalog_Id')
	name = StringField('Name')
	price = StringField('Price')
	discount = StringField('Discount')
	image_link = StringField('Image_Link')
	image_list = StringField('Image_List')
	view = StringField('View')
