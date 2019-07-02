from wtforms import Form, validators, StringField 
class CatalogForm(Form):
	name = StringField('Name')
