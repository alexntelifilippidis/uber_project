import json
from flask import Flask, jsonify, request, flash
from functools import wraps
from app.models import *
from app import app
import logging

# now we will Create and configure logger
logging.basicConfig(filename="uber.log", format='%(asctime)s %(message)s', filemode='w')
# Let us Create an object
logger = logging.getLogger()
# Now we are going to Set the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)


@app.route("/")
def hello_world():
    logger.debug('hello world')
    print('print', flush=True)
    return jsonify(post='hello world')






