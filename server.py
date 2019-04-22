#! /usr/bin/env python
# -*- coding: utf-8 -*-


__doc__ = """web server
"""

import json
from flask import Flask, request, send_from_directory, Response
from flask_cors import CORS, cross_origin

import trie
from db import db



app = Flask(__name__)
CORS(app)


@app.route("/")
@cross_origin()
def api_index():

    return send_from_directory('./','index.html')





@app.route("/autocomplete", methods=['GET'])
def autocomplete():
    

    search=request.args.get('word')



    

    names=Trie.find(search,10)

    result=[]

    for name in names:
        dic={}
        dic['id']=name[1]
        dic['type']=name[2]
        dic['name']=name[0]
        result.append(dic)





    return Response(json.dumps(result), mimetype='application/json')


def buildTrie():
    global Trie
    Trie=trie.Trie()

    nm=db.getNM()
    for ID,name in nm:
        Trie.insert(name,ID,'nm')

    mc=db.getMC()
    for ID,name in mc:
        Trie.insert(name,ID,'mc')

    nb=db.getNB()
    for ID,name in nb:
        Trie.insert(name,ID,'nb')

    nc=db.getNC()
    for ID,name in nc:
        Trie.insert(name,ID,'nc')

    ng=db.getNG()
    for ID,name in ng:
        Trie.insert(name,ID,'ng')




if __name__ == '__main__':
    
    buildTrie()
    app.run(host='127.0.0.1', port=8000, debug=True, use_reloader=False)
    



