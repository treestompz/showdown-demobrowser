from flask import Flask, render_template, jsonify
import ujson
import os, time


app = Flask(__name__)

DEBUG = False
DEMOS_PATH = os.getcwd() + "/static/demos/"

from config import *

def fast_jsonify(*args, **kwargs):
    if DEBUG:
        serialized = ujson.dumps(dict(*args, **kwargs), indent=2)
    else:
        serialized = ujson.dumps(dict(*args, **kwargs))

    return app.response_class((serialized, '\n'), mimetype='application/json')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/api/get_demos')
def demos():
    demos = []
    for serverPath in os.listdir(DEMOS_PATH):
        demoList = []
        for demoPath in os.listdir(DEMOS_PATH+serverPath+"/"):
            demoList.append(gen_demo(DEMOS_PATH+serverPath+"/" + demoPath, demoPath))

        newServer = {}
        newServer['server_name'] = serverPath
        newServer['server_demos'] = demoList
        demos.append(newServer)

    return fast_jsonify({'success': True, 'demos': demos})

def gen_demo(filepath, filename):
    demo = {}
    demo['time_created'] = time.ctime(os.path.getctime(filepath))
    # TODO: ???
    demo['last_modified'] = time.ctime(os.path.getmtime(filepath))
    sep = len(filename) - filename.index('&') - 1
    demo['map'] = filename[-sep:]
    demo['filename'] = filename
    demo['filesize'] = str(os.path.getsize(filepath) / 1000) + " kb"
    return demo

if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)
