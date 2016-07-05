# -*- coding: utf-8 -*-
from flask import jsonify

from mypackage.service import app
from mypackage.models import Person

__all__ = ['randomPerson']


@app.route('/randomPerson')
def randomPerson():
    v = Person()
    return jsonify(v.to_dict())
