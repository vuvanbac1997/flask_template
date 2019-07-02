from wtforms import Form, BooleanField, StringField, PasswordField, validators


class RegistrationForm(Form):
    username = StringField('Username', [
        validators.Length(min=3, max=25, message="Tối thiểu 3 kí tự")
    ])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords không trùng nhau'),
        validators.Length(min=3, max=25, message="Tối thiểu 3 kí tự")
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('Đồng ý điều khoản', [validators.DataRequired()])
