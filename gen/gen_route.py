import json
import os.path


def gen_route():
    with open('data.json') as json_file:
        data = json.load(json_file)
        for r in data:
            print(r)
            route_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'routes/admin'))

            models_complete = os.path.join(route_path, r + '.py')
            models_file = open(models_complete, "w")

            # Gen import
            models_file.write("from flask import Blueprint, render_template, request, redirect, flash")
            models_file.write("\n")
            models_file.write("from flask_login import login_required, current_user")
            models_file.write("\n")
            models_file.write("from flask_paginate import Pagination, get_page_args")
            models_file.write("\n")
            models_file.write("from datetime import datetime")
            models_file.write("\n")
            models_file.write("import re")
            models_file.write("\n")
            models_file.write("from models." + r + " import " + r.title())
            models_file.write("\n\n")

            blueprint_name = "admin_" + r
            models_file.write(
                blueprint_name + "= Blueprint('Admin" + r.title() + "', __name__, url_prefix='/admin/" + r + "')")
            models_file.write("\n\n")

            # Gen function
            models_file.write("@" + blueprint_name + ".route('/', methods = ['GET'])")
            models_file.write("\n")
            models_file.write("@login_required")
            models_file.write("\n")
            models_file.write("def " + r + "_index():")
            models_file.write("\n")
            models_file.write("\tsearch = False\n\tq = request.args.get('search')\n\tif q:\n\t\tsearch = True\n\tpage, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')")

            models_file.write("\n\tif search:")
            models_file.write("\n\t\tregex = re.compile('.*'+q+'.*')\n\t\t"+r+" = "+r.title()+".objects(is_active=True).skip(offset).limit(per_page)")
            models_file.write("\n\telse:")
            models_file.write("\n\t\t"+r+" = "+r.title()+".objects(active=True).skip(offset).limit(per_page)")
            models_file.write("\n\tpagination = Pagination(page=page, total="+r+".count(), record_name='"+r+"s', css_framework='bootstrap4')")
            models_file.write("\n\treturn render_template('admin/"+r+"/index.html', "+r+"s="+r+", page=page,per_page=per_page, pagination=pagination)")
            models_file.write("\n\n")


            models_file.write("@" + blueprint_name + ".route('/edit/<" + r + "_id" + ">', methods = ['GET'])")
            models_file.write("\n")
            models_file.write("@login_required")
            models_file.write("\n")
            models_file.write("def " + r + "_edit(" + r + "_id" + "):")
            models_file.write("\n")
            models_file.write("\treturn '1'")
            models_file.write("\n\n")

            models_file.write("@" + blueprint_name + ".route('/create', methods = ['POST'])")
            models_file.write("\n")
            models_file.write("@login_required")
            models_file.write("\n")
            models_file.write("def " + r + "_create():")
            models_file.write("\n")
            models_file.write("\treturn '1'")
            models_file.write("\n\n")

            models_file.write("@" + blueprint_name + ".route('/update', methods = ['POST'])")
            models_file.write("\n")
            models_file.write("@login_required")
            models_file.write("\n")
            models_file.write("def " + r + "_update():")
            models_file.write("\n")
            models_file.write("\treturn '1'")
            models_file.write("\n\n")

            models_file.write("@" + blueprint_name + ".route('/delete/<" + r + "_id" + ">', methods = ['GET'])")
            models_file.write("\n")
            models_file.write("@login_required")
            models_file.write("\n")
            models_file.write("def " + r + "_delete(" + r + "_id" + "):")
            models_file.write("\n")
            models_file.write("\treturn '1'")
            models_file.write("\n\n")

            models_file.close()

            # register_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
            # register_file = os.path.join(register_path, '__init__.py')
            # file = open(register_file, "r")
            # insert_blueprint = "insert_blueprint"
            # insert_route = "insert_route"
            # with open(register_file) as myFile:
            #     for num, line in enumerate(myFile, 1):
            #         if insert_route in line:
            #             print('found at line:', num)

gen_route()
