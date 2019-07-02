from flask import Blueprint, render_template, request, redirect, flash
from flask_login import login_required, current_user
from flask_paginate import Pagination, get_page_args
from datetime import datetime
import re

from models.post import Post

admin_post = Blueprint('AdminPost', __name__, url_prefix="/admin/post")


@admin_post.route("/", methods = ['POST', 'GET'])
@login_required
def post_index():

    search = False
    q = request.args.get('search')
    if q:
        search = True

    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    if search:
        regex = re.compile('.*'+q+'.*')
        post = Post.objects(title=regex, is_active=True).skip(offset).limit(per_page)
    else:
        post = Post.objects(active=True).skip(offset).limit(per_page)

    #pagination = Pagination(page=page, total=post.count(), search=search, record_name='posts', css_framework='bootstrap4')
    pagination = Pagination(page=page, total=post.count(), record_name='posts', css_framework='bootstrap4')

    return render_template("admin/post/index.html",
                           posts=post,
                           search=search,
                           page=page,
                           per_page=per_page,
                           pagination=pagination)


@admin_post.route("/edit/<post_id>")
@login_required
def post_edit(post_id):
    if post_id != "0":
        post = Post.objects.get(id=post_id)
        return render_template("admin/post/edit.html", post=post)
    else:
        return render_template("admin/post/edit.html")


@admin_post.route("/create", methods=['POST'])
@login_required
def post_create():
    title = request.values.get('title')
    content = request.values.get('content')
    create_date = datetime.now()
    post = Post(title=title, content=content, create_date=create_date).save()
    id = str(post.id)
    if id:
        flash("Success", 'success')
    else:
        flash("Error", 'error')
    return redirect("/admin/post/edit/" + id)


@admin_post.route("/update", methods=['POST'])
@login_required
def post_update():
    id = request.values.get('id')
    title = request.values.get('title')
    content = request.values.get('content')
    post = Post(id=id).update(title=title, content=content)
    if post:
        flash("Success", 'success')
    else:
        flash("Error", 'error')
    return redirect("/admin/post/edit/" + id)

@admin_post.route("/delete/<post_id>")
@login_required
def post_delete(post_id):
    Post(id=post_id).update(active=False)
    return redirect('/admin/post')