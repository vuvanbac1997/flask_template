from flask import Blueprint, render_template, redirect, request, flash
from form.LoginForm import LoginForm
from form.RegistrationForm import RegistrationForm
from werkzeug.security import check_password_hash, generate_password_hash

from models.user import User
from flask_login import login_manager, logout_user, login_required, login_user, current_user

auth = Blueprint('Auth', __name__, url_prefix="/")


@auth.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == "GET":
        if current_user.is_authenticated:
            return redirect('/admin')
        return render_template("auth/login.html", form=form)

    if request.method == "POST":
        username = request.values.get("username")
        password = request.values.get("password")
        if form.validate():
            check_user = User.objects(username=username).first()
            if check_user:
                if check_password_hash(check_user['password'], password):
                    login_user(check_user)
                    return redirect("/admin")

            flash("Error! Wrong username or password")
    return render_template("auth/login.html", form=form)


@auth.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'GET':
        return render_template("auth/register.html", form=form)

    if request.method == 'POST':
        username = request.values.get("username")
        password = request.values.get("password")
        if form.validate():
            existing_user = User.objects(username=username).first()
            if existing_user:
                flash('Error! Username existed')
                return render_template("auth/register.html", form=form)
            else:
                flash('Register success')
                hash_pass = generate_password_hash(password, method='sha256')
                user = User(username=username, password=hash_pass).save()
                # login_user(user)

    return render_template("auth/register.html", form=form)




@auth.route("/admin")
@login_required
def admin():
    return render_template("admin/index.html")


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/login')