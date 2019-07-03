from flask import Blueprint, render_template, request, redirect, flash
from flask_login import login_required, current_user
from flask_paginate import Pagination, get_page_args
from datetime import datetime
import re
from models.product import Product

admin_product= Blueprint('AdminProduct', __name__, url_prefix='/admin/product')

@admin_product.route('/', methods = ['GET'])
@login_required
def product_index():
	search = False
	q = request.args.get('search')
	if q:
		search = True
	page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
	if search:
		regex = re.compile('.*'+q+'.*')
		product = Product.objects(catalog_id = q,active=True).skip(offset).limit(per_page)
	else:
		product = Product.objects(active=True).skip(offset).limit(per_page)
	pagination = Pagination(page=page, total=product.count(), record_name='products', css_framework='bootstrap4')
	return render_template('admin/product/index.html', products=product, page=page,per_page=per_page, pagination=pagination)

@admin_product.route('/edit/<product_id>', methods = ['GET'])
@login_required
def product_edit(product_id):
	if product_id != '0':
		product = Product.objects.get(id=product_id)
		return render_template('admin/product/edit.html', product=product)
	else:
		return render_template('admin/product/edit.html')

@admin_product.route('/create', methods = ['POST'])
@login_required
def product_create():
	catalog_id = request.values.get('catalog_id')
	name = request.values.get('name')
	price = request.values.get('price')
	discount = request.values.get('discount')
	image_link = request.values.get('image_link')
	image_list = request.values.get('image_list')
	view = request.values.get('view')
	product = Product(catalog_id = catalog_id, name = name, price = price, discount = discount, image_link = image_link, image_list = image_list, view = view).save()
	id = str(product.id)
	if id:
		flash('Success', 'success')
	else:
		flash('Error', 'error')
	return redirect('/admin/product/edit/' + id)

@admin_product.route('/update', methods = ['POST'])
@login_required
def product_update():
	id = request.values.get('id')
	catalog_id = request.values.get('catalog_id')
	name = request.values.get('name')
	price = request.values.get('price')
	discount = request.values.get('discount')
	image_link = request.values.get('image_link')
	image_list = request.values.get('image_list')
	view = request.values.get('view')
	product = Product(id=id).update(catalog_id = catalog_id, name = name, price = price, discount = discount, image_link = image_link, image_list = image_list, view = view)
	if product:
		flash('Success', 'success')
	else:
		flash('Error', 'error')
	return redirect('/admin/product/edit/' + id)

@admin_product.route('/delete/<product_id>', methods = ['GET'])
@login_required
def product_delete(product_id):
	Product(id=product_id).update(active=False)
	return redirect('/admin/product')

