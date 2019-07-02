import json
import os.path


def gen_form():
    with open('data.json') as json_file:
        data = json.load(json_file)
        for r in data:
            print(r)
            forms_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'form'))

            models_complete = os.path.join(forms_path, r.title() + 'Form.py')
            models_file = open(models_complete, "w")

            models_file.write("from wtforms import Form, validators, StringField ")
            models_file.write("\n")
            models_file.write("class " + r.title() + "Form" + "(Form):")
            models_file.write("\n")
            for key, value in data.get(r).items():
                models_file.write("\t" + key + " = " + "StringField('" + key.title() + "')")
                models_file.write("\n")

            models_file.close()
