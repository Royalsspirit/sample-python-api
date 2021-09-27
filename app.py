from flask import Flask, jsonify, request
from cerberus import Validator

app = Flask(__name__)

"""
define predicates allowed and its sql translation
If mongo or other databases is needed, we could for each DB its own predicates syntaxe
"""
predicates = {
    "gt": ">",
    "lt": "<",
    "eq": "=",
    "contains": "LIKE"
}


def handleFields(fields):
    """
    manage fields to adapt to sql query
    """
    return ', '.join(fields)


def handleFilters(filters):
    """
    manage filters to adapt to sql query
    """
    arr_filters = []
    for f in [filters]:
        if 'predicate' in f:
            if f['predicate'] == "contains":
                arr_filters.append('%(field)s LIKE "%%%(value)s%%"' % f)
            else:
                arr_filters.append('%s %s %s' % (f['field'], predicates[f['predicate']], f['value']))
        else:
            arr_filters.append('%s = %s' % (f['field'], f['value']))

    return ' '.join(arr_filters)


def toMysql(req):
    """ 
    function to convert current DSL to sql
    we can imagine same kind of functions to convert to mongo query, oracle
    """
    head = "SELECT "
    tail = " FROM tows"
    arr_fields = handleFields(req['fields'])

    arr_filters = [' WHERE']
    
    if 'filters' in req:
        arr_filters.append(handleFilters(req['filters']))
   
    return head + arr_fields + tail + ' '.join(arr_filters)


def validateInput(data):
    """
    Schema to validate input
    """
    schema = {
        "fields": {
            'type': 'list',
            'allowed': [
                 'code',
                 'name',
                 'population',
                 'average_age',
                 'distr_code',
                 'dept_code',
                 'region_code',
                 'region_name'
            ]
        },
        'filters': {
            'type': 'dict',
            'schema': {
                'field': {'type': 'string'},
                'predicate': {'type': 'string'},
                'value': {'type': ['string', 'integer'], 'nullable': True}
            }
        }
    }
    v = Validator(schema)
    return v.validate(data), v


"""
to generate (create) a new query
"""
@app.route('/generate', methods=['POST'])
def generate():
    resp = request.get_json()
    isValidate, v = validateInput(resp)
    if isValidate:
        return toMysql(resp)
    else:
        return v.errors
