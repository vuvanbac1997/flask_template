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
            # list
            models_file.write("@" + blueprint_name + ".route('/', methods = ['GET'])")
            models_file.write("\n")
            models_file.write("@login_required")
            models_file.write("\n")
            models_file.write("def " + r + "_index():")
            models_file.write("\n")
            models_file.write("\tsearch = False\n\tq = request.args.get('search')\n\tif q:\n\t\tsearch = True\n\tpage, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')")
            first_key_to_search = next(iter(data.get(r).keys()))
            models_file.write("\n\tif search:")
            models_file.write("\n\t\tregex = re.compile('.*'+q+'.*')\n\t\t"+r+" = "+r.title()+".objects("+first_key_to_search+" = q,active=True).skip(offset).limit(per_page)")
            models_file.write("\n\telse:")
            models_file.write("\n\t\t"+r+" = "+r.title()+".objects(active=True).skip(offset).limit(per_page)")
            models_file.write("\n\tpagination = Pagination(page=page, total="+r+".count(), record_name='"+r+"s', css_framework='bootstrap4')")
            models_file.write("\n\treturn render_template('admin/"+r+"/index.html', "+r+"s="+r+", page=page,per_page=per_page, pagination=pagination)")
            models_file.write("\n\n")

            # Edit
            models_file.write("@" + blueprint_name + ".route('/edit/<" + r + "_id" + ">', methods = ['GET'])")
            models_file.write("\n")
            models_file.write("@login_required")
            models_file.write("\n")
            models_file.write("def " + r + "_edit(" + r + "_id" + "):")
            models_file.write("\n\tif "+r+"_id != '0':")
            models_file.write("\n\t\t"+r+" = "+r.title()+".objects.get(id=" + r + "_id" + ")")
            models_file.write("\n\t\treturn render_template('admin/"+r+"/edit.html', "+r+"="+r+")")
            models_file.write("\n\telse:")
            models_file.write("\n\t\treturn render_template('admin/"+r+"/edit.html')")
            models_file.write("\n\n")

            # Create
            models_file.write("@" + blueprint_name + ".route('/create', methods = ['POST'])")
            models_file.write("\n")
            models_file.write("@login_required")
            models_file.write("\n")
            models_file.write("def " + r + "_create():")
            lkey = []
            for key, value in data.get(r).items():
                lkey.append(key)
                models_file.write("\n\t"+key+" = request.values.get('"+key+"')")
            s=""
            for key in lkey:
                s += key + " = " + key
                if lkey.index(key) != len(lkey) - 1:
                    s += ", "
            models_file.write("\n\t"+r+" = "+r.title()+"("+s+").save()")
            models_file.write("\n\tid = str("+r+".id)")
            models_file.write("\n\tif id:")
            models_file.write("\n\t\tflash('Success', 'success')")
            models_file.write("\n\telse:")
            models_file.write("\n\t\tflash('Error', 'error')")
            models_file.write("\n\treturn redirect('/admin/"+r+"/edit/' + id)")
            models_file.write("\n\n")

            # update
            models_file.write("@" + blueprint_name + ".route('/update', methods = ['POST'])")
            models_file.write("\n")
            models_file.write("@login_required")
            models_file.write("\n")
            models_file.write("def " + r + "_update():")
            models_file.write("\n\tid = request.values.get('id')")
            lkey1 = []
            for key, value in data.get(r).items():
                lkey1.append(key)
                models_file.write("\n\t"+key+" = request.values.get('"+key+"')")
            s1=""
            for key in lkey1:
                s1 += key + " = " + key
                if lkey1.index(key) != len(lkey1) - 1:
                    s1+= ", "
            models_file.write("\n\t"+r+" = "+r.title()+"(id=id).update("+s1+")")
            models_file.write("\n\tif "+r+":")
            models_file.write("\n\t\tflash('Success', 'success')")
            models_file.write("\n\telse:")
            models_file.write("\n\t\tflash('Error', 'error')")
            models_file.write("\n\treturn redirect('/admin/"+r+"/edit/' + id)")
            models_file.write("\n\n")

            # Delete
            models_file.write("@" + blueprint_name + ".route('/delete/<" + r + "_id" + ">', methods = ['GET'])")
            models_file.write("\n")
            models_file.write("@login_required")
            models_file.write("\n")
            models_file.write("def " + r + "_delete(" + r + "_id" + "):")
            models_file.write("\n\t"+r.title()+"(id="+r+"_id).update(active=False)")
            models_file.write("\n\treturn redirect('/admin/"+r+"')")
            models_file.write("\n\n")

            models_file.close()

    # register_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    # register_file = os.path.join(register_path, '__init__.py')
    #
    # start_route = "start_route"
    # end_route = "end_route"
    # start_index = 0
    # end_index = 0
    #
    # with open(register_file) as myFile:
    #     for num, line in enumerate(myFile, 1):
    #         if start_route in line:
    #             start_index = num
    #             print('found at line:', num)
    #         if end_route in line:
    #             end_index = num

    # f = open(register_file, "r+")
    # contents = f.readlines()
    # f.close()
    # contents.insert(start_index, "cu cai")
    # f = open(register_file, "w")
    # contents = "".join(contents)
    # f.write(contents)
    # f.close()


gen_route()
