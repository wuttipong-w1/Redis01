import os
import json
import redis
from flask import Flask,request,jsonify

app = Flask(__name__)
db = redis.StrictRedis( # ทำการเอาข้อมูลใน redisCommander มาเก็บไว้ที่ db
        host='10.100.2.138',
        port=6379,
        password='APPatn99455', # รหัสที่ใช้ login เข้า redis
        decode_responses=True
        )

#show key ทั้งหมด
@app.route('/',methods=['GET'])
def Show_keys(): #ทำการสร้างฟังก์ชัน Show_keys
    data=db.keys() #สร้าง data มาเก็บข้อมูลจาก db.key 
    data.sort() #เรียงข้อมูล
    req = [] #ประกาศตัวแปล array ชื่อ req 
    for k in data : # สร้างลูป for เอาค่า k มาเก็บ
        req.append(db.hgetall(k)) # db.hgetall แสดงค่าทั้งหมด จาก k แล้วทำการเรียงข้อมูลแบบ list มาเก็บไว้ที่ req
    return jsonify(req) # ทำการสั่งค่ากลับ


# Get Single Key แสดงข้อมูลที่ละข้อมูล
@app.route('/<Key>',methods=['GET']) # รับค่า Key
def get_key(Key): #ทำการสร้างฟังก์ชัน get_key 
    result = db.hgetall(Key) # แสดงข้อมูลทั้งหมดใน Key ที่เราจะเลือกดู 
    return jsonify(result) # ทำการสั่งค่ากลับ

# DELETE Key ลบข้อมูล
@app.route('/<Key>',methods=['DELETE']) # รับค่า Key 
def DELETE_key(Key): #ทำการสร้างฟังก์ชัน DELETE_key 
    result = db.delete(Key) # ทำการลบข้อมูลใน db ตาม Key ที่เรากำหนด
    return "Delete_Car" # ทำการสั่งค่า Delete_Car ไปแสดง

 # Create Key  เพิ่มข้อมูล  
@app.route('/Car',methods=['POST']) # รับค่า Car 
def Post_key():  # ทำการสร้างฟังก์ชัน Post_key
    ID = request.json['ID'] # แปลงข้อมูล json
    name = request.json['name'] # แปลงข้อมูล json
    brand = request.json['brand'] # แปลงข้อมูล json
    price = request.json['price'] # แปลงข้อมูล json

    data = {"ID":ID, "name":name, "brand":brand, "price":price} # ให้ data เก็บข้อมูลที่ต้องการเพิ่ม

    db.hmset(ID,data) # เก็บข้อมูล data ให้ ID ชี้ไปเราต้องการ
    
    return jsonify(data)  # ทำการสั่งค่ากลับ

# update Key
@app.route('/Car/<Key>',methods=['PUT']) # รับค่า Car ตำแหน่งที่ Key
def PUT_key(Key):  # ทำการสร้างฟังก์ชัน Post_key
    
    name = request.json['name'] # แปลงข้อมูล json
    brand = request.json['brand'] # แปลงข้อมูล json
    price = request.json['price'] # แปลงข้อมูล json

    data = {"name":name, "brand":brand, "price":price}  # ให้ data เก็บข้อมูลที่ต้องการเปลี่ยน

    db.hmset(Key,data) # เก็บข้อมูล data ให้ Key ชี้ไปเราต้องการ
    return jsonify(data) # ทำการสั่งค่ากลับ

# # Get Single Key แสดงข้อมูลที่ละข้อมูล
# @app.route('/<Key>',methods=['GET']) # รับค่า Key
# def get_key(Key): #ทำการสร้างฟังก์ชัน get_key 
#     result = db.hmget(Key) # แสดงข้อมูลทั้งหมดใน Key ที่เราจะเลือกดู 
#     return jsonify(result) # ทำการสั่งค่ากลับ

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)