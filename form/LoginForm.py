from wtforms import Form, BooleanField, StringField, PasswordField, validators


class LoginForm(Form):
    username = StringField('Username', [
        validators.DataRequired(),
        validators.Length(min=3, message="Tối thiểu 3 ký tự")
    ])
    password = PasswordField("Password", [
        validators.DataRequired(),
        validators.Length(min=6, message="Tối thiểu 6 ký tự")
    ])
    remember_me = BooleanField("Remember me")
