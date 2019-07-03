import json
import os.path


def gen_view():
    with open('data.json') as json_file:
        data = json.load(json_file)
        for r in data:
            view_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates/admin/' + r))
            os.makedirs(view_path, exist_ok=True)
            view_index = os.path.join(view_path, 'index.html')
            view_edit = os.path.join(view_path, 'edit.html')

            file_index = open(view_index, "w")
            file_edit = open(view_edit, "w")

            # index.html
            first_key_to_search = next(iter(data.get(r).keys()))
            file_index.write("{% extends 'admin/index.html' %}")
            file_index.write("\n{% block content %}")
            file_index.write('\n<h4 class="card-title d-flex justify-content-between align-items-center">')
            file_index.write('\n'+r.title()+' Datatable')
            file_index.write('\n</h4>')
            file_index.write('\n<div class="row">\n<div class="col-12">\n<div class="card">\n <div class="card-body border-bottom">\n<h4 class="card-title d-flex justify-content-between align-items-center">')
            file_index.write('\n'+r.title()+' Datatable')
            file_index.write('\n<a class="fixed-left-part float-right  mb-3" href="{{ url_for("Admin'+r.title()+'.'+r+'_edit", '+r+'_id = 0) }}"><button class="btn btn-outline-success">Create</button></a>\n</h4>')
            file_index.write('\n<div class="row">')
            file_index.write('\n<div class="col-md-6">\nTotal: {{ pagination.total }}\n</div>')
            file_index.write('\n<div class="col-md-6">\n<form action="/admin/'+r+'">\n<div class="input-group">\n<input class="form-control py-2 border-right-0 border" type="search" name="search" placeholder="Search by '+first_key_to_search+'" id="example-search-input">\n<span class="input-group-append">\n<div class="input-group-text bg-transparent">\n<i class="fa fa-search"></i>\n</div>\n</span>\n</div>\n</form>\n</div>')
            file_index.write('\n</div>\n</div>')
            file_index.write('\n<div class="card-body">\n<div class="table-responsive">')
            file_index.write('\n<table id="zero_config" class="table table-striped table-bordered">\n<thead>\n<tr>')
            file_index.write('\n<th>Id</th>')
            for key, value in data.get(r).items():
                file_index.write('\n<th>'+key+'</th>')
            file_index.write('\n<th width="10%">Action</th>')
            file_index.write('\n </tr>\n</thead>')
            file_index.write('\n<tbody>\n<tr>')
            file_index.write('\n{% for '+r+' in '+r+'s %}\n<tr>')
            file_index.write('\n<td>{{ loop.index }}</td>')
            for key, value in data.get(r).items():
                file_index.write('\n<td>{{ '+r+'.'+key+' }}</td>')
            file_index.write('\n<td width="10%" class="text-center">')
            file_index.write('\n<a class="mr-1" style="color: inherit;" href="{{ url_for("Admin'+r.title()+'.'+r+'_delete", '+r+'_id = '+r+'.id) }}" data-toggle="tooltip" data-placement="top" title="Delete"><i class="fas fa-trash-alt"></i></a>')
            file_index.write('\n<a class="ml-1" style="color: inherit;" href="{{ url_for("Admin'+r.title()+'.'+r+'_edit", '+r+'_id = '+r+'.id) }}" data-toggle="tooltip" data-placement="top" title="Edit"><i class="fas fa-edit"></i></a>')
            file_index.write('\n</td>\n</tr>\n{% endfor %}\n</tbody>\n</table>\n</div>')
            file_index.write('\n<div class="d-flex justify-content-center">\n{{ pagination.links }}\n</div>\n</div>\n</div>\n</div>\n</div>\n{% endblock %}')
            file_index.close()

            #gen edit.html
            file_edit.write('{% extends "admin/index.html" %}\n{% block style %}{% endblock %}\n{% block script %}\n{% endblock %}')
            file_edit.write('\n{% block content %}\n{{ toastr.message() }}')
            file_edit.write('\n<h4 class="card-title d-flex justify-content-between align-items-center">\n'+r.title()+'\n<a href="{{ url_for("Admin'+r.title()+'.'+r+'_index") }}"><button class="btn btn-secondary">Back</button></a>\n</h4>')
            file_edit.write('\n<div class="row">\n<div class="col-12">\n<div class="card">\n<div class="card-body">')
            file_edit.write('\n<form id="identifier" class="form-group" action="{{"/admin/'+r+'/update" if '+r+' else "/admin/'+r+'/create" }}" method="post">\n<input type="hidden" name="csrf_token" value="{{ csrf_token() }}"/>')
            file_edit.write('\n<input type="text" name="id" class="form-control" value="{{ '+r+'.id if '+r+' else ""}}" hidden>')
            for key, value in data.get(r).items():
                file_edit.write('\n<div class="form-group row">')
                file_edit.write('\n<label for="l'+key+'" class="col-sm-3 text-right control-label col-form-label">'+key.title()+'</label>')
                file_edit.write('\n<div class="col-sm-9">\n<input type="text" name="'+key+'" class="form-control" value="{{ '+r+'.'+key+' if '+r+' else ""}}" id="l'+key+'" placeholder="'+key.title()+'">\n</div>\n</div>')
            file_edit.write('\n<div class="row bg-white">\n<div class="card-body text-center">\n<div class="form-group">\n<button type="submit" class="btn btn-primary">Submit</button>\n</div>\n</div>\n</div>')
            file_edit.write('\n</form>\n</div>\n</div>\n</div>\n</div>\n{% endblock %}')
            file_edit.close()


    # insert to sidebar
    register_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates/admin/layout'))
    register_file = os.path.join(register_path, 'left-sidebar.html')
    sidebar_file = open(register_file, "w")
    sidebar_file.write('<aside class="left-sidebar" data-sidebarbg="skin5">\n<div class="scroll-sidebar">\n<nav class="sidebar-nav">\n<ul id="sidebarnav" class="p-t-30">')
    sidebar_file.write('\n<li class="sidebar-item"> <a class="sidebar-link waves-effect waves-dark sidebar-link" href="{{ url_for("Admin'+r.title()+'.'+r+'_index") }}" aria-expanded="false"><i class="mdi mdi-view-dashboard"></i><span class="hide-menu">Post</span></a></li>\n<li class="sidebar-item"> <a class="sidebar-link waves-effect waves-dark sidebar-link" href="{{ url_for("Admin.user_index") }}" aria-expanded="false"><i class="mdi mdi-account"></i><span class="hide-menu">User</span></a></li>')
    with open('data.json') as json_file:
        data = json.load(json_file)
        for r in data:
            print(r)
            sidebar_file.write('\n<li class="sidebar-item"> <a class="sidebar-link waves-effect waves-dark sidebar-link" href="{{ url_for("Admin'+r.title()+'.'+r+'_index") }}" aria-expanded="false"><i class="mdi-folder-outline"></i><span class="hide-menu">'+r.title()+'</span></a></li>')
    sidebar_file.write("\n</ul></nav>\n</div>\n</aside>")

gen_view()