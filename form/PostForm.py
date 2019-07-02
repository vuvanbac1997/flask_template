from wtforms import Form, StringField, validators


class PostForm(Form):
    title = StringField('Title', [validators.DataRequired()])
    content = StringField("Content")
