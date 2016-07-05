# -*- coding: utf-8 -*-
import json

from mypackage.models import Person

def test_randomPerson_view(app):
    rv = app.get('/randomPerson')
    data = json.loads(rv.data.decode('utf-8'))
    inst = Person()
    inst.from_dict(data)
    
    assert inst.age is not None
    assert inst.name is not None
  

def test_swagger_info(app):
    rv = app.get('/api')
    spec = json.loads(rv.data.decode('utf-8'), 'utf-8')

    assert "info" in spec

    info = spec["info"]
    assert "title" in info
    assert info["title"] == "mypackage"
    assert "version" in info
    assert info["version"] == "0.0.1"
    assert "description" in info
    assert info["description"] == "${description}"


def test_swagger_Person_definition(app):
    rv = app.get('/api')
    spec = json.loads(rv.data.decode('utf-8'), 'utf-8')

    definitions = spec["definitions"]
    assert "Person" in definitions

    definition = definitions["Person"]
    assert definition["type"] == "object"
    assert "properties" in definition

    props = definition["properties"]
    assert "age" in props
    prop = props["age"]
    
    assert prop["format"] == "int32"
    assert prop["type"] == "integer"

    assert "name" in props
    prop = props["name"]
    
    assert prop["type"] == "string"


def test_swagger_parameters(app):
    rv = app.get('/api')
    spec = json.loads(rv.data.decode('utf-8'), 'utf-8')

    assert "parameters" in spec
    assert len(spec["parameters"]) == 0


def test_swagger_randomPerson_path(app):
    rv = app.get('/api')
    spec = json.loads(rv.data.decode('utf-8'), 'utf-8')

    assert "paths" in spec

    paths = spec["paths"]
    assert "/randomPerson" in paths

    endpoint = paths["/randomPerson"]
    assert "get" in endpoint

    get_op = endpoint["get"]
    assert "responses" in get_op

    responses = get_op["responses"]
    assert "${op.responses().success().code()}" in responses

    response_ok = responses["${op.responses().success().code()}"]
    assert "schema" in response_ok

    schema = response_ok["schema"]
    assert schema == {"$ref": "#/definitions/Person"}
