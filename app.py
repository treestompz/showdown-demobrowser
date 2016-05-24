from flask import Flask, request, url_for, render_template, redirect
from flask.ext.jsonpify import jsonify
import os


app = Flask(__name__)

HOST = '0.0.0.0'
PORT = 1338
DEBUG = False
DEMOS_PATH = os.getcwd() + "/static/demos/"

try:
    from local_config import *
except ImportError:
    pass

def die_with_error(error_message):
    response = jsonify({
        'error': True,
        'error_message': error_message
    })
    response.status_code = 400
    return response

@app.route("/demo/<server_id>/<showdown_id>/")
def demo(server_id, showdown_id):
    demo_url = gen_demo_url(server_id, showdown_id)
    return redirect(demo_url)

@app.route("/viewdemo/<int:server_id>/<int:showdown_id>/")
def viewdemo(server_id, showdown_id):
    return render_template("demo.html", server_id=server_id, showdown_id=showdown_id)

@app.route("/api/get_demo")
def get_demo():
    if 'server_id' not in request.args:
        die_with_error("Need server_id")
    if 'showdown_id' not in request.args:
        die_with_error("Need showdown_id")

    server_id = request.args.get('server_id')
    showdown_id = request.args.get('showdown_id')

    demo_url = gen_demo_url(server_id, showdown_id)

    if not demo_url:
        return jsonify(success=False)

    return jsonify(success=True, demo_url=demo_url)

def gen_demo_url(server_id, showdown_id):
    for demo in os.listdir(DEMOS_PATH+server_id+"/"):
        print demo
        ids = demo.split(",")
        ids.pop() # this removes the .dem from the list
        for id in ids:
            if id == showdown_id:
                return url_for('static', filename="demos/"+server_id+"/"+demo)
    return None

if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT, host=HOST)