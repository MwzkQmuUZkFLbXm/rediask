#!/usr/bin/env python
# -*- coding: utf-8 -*-
# app.py 

import os
import redis

from flask import Flask
from flask import Response
from flask import json

app = Flask(__name__)
app.redis = redis.StrictRedis(host=os.getenv('WERCJER_REDIS_HOST', 'localhost'), port=6379, db=0)

@app.route("/clouds.json")
def clouds():
    date = app.redis.lrange('clouds', 0, -1)
    resp = Response(json.dump(data), status=200, mimetype='application/json')
    return resp

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port,debug=True)
