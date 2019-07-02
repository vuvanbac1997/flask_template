import base64

from flask import Blueprint, render_template, request, redirect, flash
from flask_login import login_required, current_user
from flask_mongoengine.wtf import model_form
from models.user import User
from werkzeug.security import generate_password_hash
from flask_paginate import Pagination, get_page_args
import re


admin = Blueprint('Admin', __name__, url_prefix="/admin")


@admin.route("/user")
@login_required
def user_index():
    search = False
    q = request.args.get('search')
    if q:
        search = True

    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    if search:
        regex = re.compile('.*' + q + '.*')
        user = User.objects(username=regex, active=True).skip(offset).limit(per_page)
    else:
        user = User.objects(active=True).skip(offset).limit(per_page)

    # pagination = Pagination(page=page, total=post.count(), search=search, record_name='posts', css_framework='bootstrap4')
    pagination = Pagination(page=page, total=user.count(), record_name='users', css_framework='bootstrap4')

    return render_template("admin/user/index.html",
                           users=user,
                           search=search,
                           page=page,
                           per_page=per_page,
                           pagination=pagination)


@admin.route("/user/edit/<user_id>")
@login_required
def user_edit(user_id):
    user_form = model_form(User)
    if user_id != "0":
        user = User.objects.get(id=user_id)
        return render_template("admin/user/edit.html", user=user, form=user_form)
    else:
        return render_template("admin/user/edit.html", form=user_form)


@admin.route("/user/update", methods=['GET', 'POST'])
@login_required
def user_update():
    id = request.values.get("id")
    usname = request.values.get("uname")
    pwd = request.values.get("pwd")
    email = request.values.get("email")
    contact = request.values.get("contact")
    address = request.values.get("address")
    image = request.files["file_image"]
    image_string = base64.b64encode(image.read())
    image_string = "data:image/jpeg;base64," + str(image_string, 'utf-8')

    if image:
        user = User(id=id).update(username=usname, email=email, contact=contact, address=address, image=image_string)
    else:
        user = User(id=id).update(username=usname, email=email, contact=contact, address=address)
    flash('Success')

    return redirect("/admin/user/edit/" + id)


@admin.route("/user/create", methods=['GET', 'POST'])
@login_required
def user_create():
    usname = request.values.get("uname")
    pwd = generate_password_hash(request.values.get("pwd"), method='sha256')
    email = request.values.get("email")
    contact = request.values.get("contact")
    address = request.values.get("address")
    image = request.files["file_image"]
    image_string = base64.b64encode(image.read())
    image_string = "data:image/jpeg;base64," + str(image_string, 'utf-8')

    if image:
        user = User(username=usname, password=pwd, email=email, contact=contact, address=address,
                    image=image_string).save()
        user_id = str(user.id)
    else:
        user = User(username=usname, password=pwd, email=email, contact=contact, address=address).save()
        user_id = str(user.id)
    flash('Success')
    return redirect("/admin/user/edit/" + user_id)


@admin.route("/user/delete/<user_id>")
@login_required
def user_delete(user_id):
    user = User(id=user_id).delete()
    return redirect("/admin/user")


@admin.route("/profile")
@login_required
def profile_page():
    user_form = model_form(User)
    user = User.objects.get(id=current_user.id)
    return render_template("admin/profile/edit.html", user=user, form=user_form)
