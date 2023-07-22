#!/usr/bin/env python
import json

from flask import Flask
app = Flask(__name__)

def getJSONResponse(obj, r_status=200):
    return app.response_class(
                response=json.dumps(obj),
                status=r_status,
                mimetype='application/json'
            )

@app.errorhandler(404)
def error404(e):
    return getJSONResponse({"error":"All your base are belong to us"}, 404)


@app.route("/the/quick/brown/biba/jumps/over/the/lazy/dog")
def flag():
    return getJSONResponse({"flag":"VSFI_eto_i_est_flag_comrade!"})