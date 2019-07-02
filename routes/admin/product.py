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
		product = Product.objects(is_active=True).skip(offset).limit(per_page)
	else:
		product = Product.objects(active=True).skip(offset).limit(per_page)
	pagination = Pagination(page=page, total=product.count(), record_name='products', css_framework='bootstrap4')
	return render_template('admin/product/index.html', products=product, page=page,per_page=per_page, pagination=pagination)

@admin_product.route('/edit/<product_id>', methods = ['GET'])
@login_required
def product_edit(product_id):
	return '1'

@admin_product.route('/create', methods = ['POST'])
@login_required
def product_create():
	return '1'

@admin_product.route('/update', methods = ['POST'])
@login_required
def product_update():
	return '1'

@admin_product.route('/delete/<product_id>', methods = ['GET'])
@login_required
def product_delete(product_id):
	return '1'

