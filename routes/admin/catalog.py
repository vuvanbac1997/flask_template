from flask import Blueprint, render_template, request, redirect, flash
from flask_login import login_required, current_user
from flask_paginate import Pagination, get_page_args
from datetime import datetime
import re
from models.catalog import Catalog

admin_catalog= Blueprint('AdminCatalog', __name__, url_prefix='/admin/catalog')

@admin_catalog.route('/', methods = ['GET'])
@login_required
def catalog_index():
	search = False
	q = request.args.get('search')
	if q:
		search = True
	page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
	if search:
		regex = re.compile('.*'+q+'.*')
		catalog = Catalog.objects(is_active=True).skip(offset).limit(per_page)
	else:
		catalog = Catalog.objects(active=True).skip(offset).limit(per_page)
	pagination = Pagination(page=page, total=catalog.count(), record_name='catalogs', css_framework='bootstrap4')
	return render_template('admin/catalog/index.html', catalogs=catalog, page=page,per_page=per_page, pagination=pagination)

@admin_catalog.route('/edit/<catalog_id>', methods = ['GET'])
@login_required
def catalog_edit(catalog_id):
	return '1'

@admin_catalog.route('/create', methods = ['POST'])
@login_required
def catalog_create():
	return '1'

@admin_catalog.route('/update', methods = ['POST'])
@login_required
def catalog_update():
	return '1'

@admin_catalog.route('/delete/<catalog_id>', methods = ['GET'])
@login_required
def catalog_delete(catalog_id):
	return '1'

