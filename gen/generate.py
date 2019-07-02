import json
import os.path
import sys

from gen.gen_view import gen_view
from gen.gen_route import gen_route
from gen.gen_form import gen_form
from gen.gen_model import gen_model


def write_json():
    data = {}
    data['people'] = []
    data['people'].append({
        'name': 'Scott',
        'website': 'stackabuse.com',
        'from': 'Nebraska'
    })
    data['people'].append({
        'name': 'Larry',
        'website': 'google.com',
        'from': 'Michigan'
    })
    data['people'].append({
        'name': 'Tim',
        'website': 'apple.com',
        'from': 'Alabama'
    })

    with open('data.json', 'w') as outfile:
        json.dump(data, outfile, indent=4, separators=(',', ': '), sort_keys=True)
        outfile.write('\n')


def gen_elements():
    # gen_model()
    # gen_form()
    gen_route()
    # gen_view()


gen_elements()
