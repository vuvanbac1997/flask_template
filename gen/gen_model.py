import json
import os.path


def gen_model():
    with open('data.json') as json_file:
        data = json.load(json_file)
        for r in data:
            print(r)
            models_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'models'))
            forms_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'form'))
            route_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'routes/admin'))

            models_complete = os.path.join(models_path, r + '.py')
            models_file = open(models_complete, "w")

            models_file.write("from mongoengine import Document, ")
            libraries = []
            for key, value in data.get(r).items():
                libraries.append(value)
                print('\t' + key + ': ' + value)

            libraries = list(set(libraries))
            for l in libraries:
                models_file.write(l)
                if libraries.index(l) != len(libraries) - 1:
                    models_file.write(', ')

            models_file.write("\n")
            models_file.write("class " + r.title() + "(Document):")
            models_file.write("\n")
            models_file.write("\tmeta = {'collection': '" + r + "'}")
            models_file.write("\n")
            for key, value in data.get(r).items():
                models_file.write("\t" + key + " = " + value + "()")
                models_file.write("\n")

            models_file.close()
