import json
import os.path


def gen_view():
    with open('data.json') as json_file:
        data = json.load(json_file)
        for r in data:
            print(r)

            view_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates/admin/' + r))
            os.makedirs(view_path, exist_ok=True)
            view_index = os.path.join(view_path, 'index.html')
            view_edit = os.path.join(view_path, 'edit.html')

            file_index = open(view_index, "w")
            file_edit = open(view_edit, "w")

            file_index.write("Index page: " + r.title())
            file_edit.write("Edit page: " + r.title())
