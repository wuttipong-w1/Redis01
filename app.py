import os
import json
import redis
from flask import Flask,request,jsonify

app = Flask(__name__)
db = redis.StrictRedis(
        host='10.100.2.138',
        port=6379,
        password='APPatn99455',
        decode_responses=True
        )

#show key
@app.route('/',methods=['GET'])
def Show_keys():
    name=db.keys()#ข้อมูลจากkey
    name.sort()#เรียงข้อมูล
    req = []
    for i in name :
        req.append(db.hgetall(i))
    return jsonify(req)


# Get Single Key
@app.route('/<Key>',methods=['GET'])
def Show_key(Key):
    req = db.hgetall(Key)
    return jsonify(req)

# DELETE Key
@app.route('/<Key>',methods=['DELETE'])
def DELETE_key(Key):
    req = db.delete(Key)
    return "DELETE"

 # Post Key
@app.route('/Car',methods=['POST'])
def Post_key():
    ID = request.json['ID']
    name = request.json['name']
    brand = request.json['brand']
    price = request.json['price']

    user = {"ID":ID, "name":name, "brand":brand, "price":price}

    db.hmset(ID,user)
    
    return jsonify(user)

# update Key
@app.route('/Car/<Key>',methods=['PUT'])
def PUT_key(Key):
    
    name = request.json['name']
    brand = request.json['brand']
    price = request.json['price']

    user = {"Key":Key, "name":name, "brand":brand, "price":price}

    db.hmset(Key,user)
    return jsonify(user)

# @app.route('/')
# def hello_world():
#     name=db.get('name') or'World'
#     return 'Hello %s!' % name

#update ชื่อ
# @app.route('/setname/<name>')
# def setname(name):
#     db.set('name',name)
#     return 'Name updated.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)