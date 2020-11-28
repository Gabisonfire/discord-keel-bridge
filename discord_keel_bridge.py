#!/bin/env python3
import os
import requests
import json
from flask import Flask, request, jsonify
from gevent.pywsgi import WSGIServer

DISCORD_URL = os.environ['DISCORD_BRIDGE_URL']
PORT = int(os.environ['DISCORD_BRIDGE_PORT'])

app = Flask(__name__)

@app.route('/v1/incoming', methods=['POST'])
def incoming():
    original = request.json
    discord = {}
    discord["content"] = f'**{original["name"]}:** {original["message"]}. ({original["createdAt"]}).'
    result = requests.post(DISCORD_URL, data=json.dumps(discord), headers={"Content-Type": "application/json"})
    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
        resp = jsonify(success=False)
        resp.status_code = result.status_code
    else:
        print("Payload delivered successfully, code {}.".format(result.status_code))
        resp = jsonify(success=True)
        resp.status_code = 200
    return resp 

http_server = WSGIServer(('0.0.0.0', PORT), app)
print(f"Bridge listening on port: {PORT}")
http_server.serve_forever()