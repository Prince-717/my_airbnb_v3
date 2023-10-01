#!/usr/bin/python3
""" connect to api """
from api.v1.views import app_views
from flask import jsonify, Flask
from models import storage

dbClass = {
    "amenities": "Amenity",
    "cities": "City",
    "places": "Place",
    "reviews": "Review",
    "states": "State",
    "users": "User"
}


@app_views.route('/status', strict_slashes=False)
def status():
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def stats():
    """ return the number of objects """
    dic = {}
    for key, val in dbClass.items():
        dic[key] = storage.count(val)
    return jsonify(dic)
