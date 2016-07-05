# -*- coding: utf-8 -*-
from apispec import APISpec
from marshmallow import Schema, fields


__all__ = ['spec']


spec = APISpec(
    title='mypackage',
    version='0.0.1',
    info=dict(
        description='${description}'
    ),
    plugins=['apispec.ext.marshmallow']
)


class PersonSchema(Schema):
  age = fields.Int()
  name = fields.String()
    
spec.definition('Person', schema=PersonSchema)


spec.add_path(
    path='/randomPerson',
    operations=dict(
        get=dict(
            responses={
                '${op.responses().success().code()}': {
                    'schema': {'$ref': '#/definitions/Person'}
                }
            }
        )
    )
)
