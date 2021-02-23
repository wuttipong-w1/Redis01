from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

#Init app
app = Flask(__name__)

#Database
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://webadmin:AOSnqn31435@node8612-advweb-23.app.ruk-com.cloud:11105/CloudDB"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://webadmin:AOSnqn31435@10.100.2.209/CloudDB"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False
#Init db
db = SQLAlchemy(app)
#Init ma
ma = Marshmallow(app)

#Staff Class/Model
class car(db.Model):
    id = db.Column(db.String(20), primary_key=True, unique=True)
    name = db.Column(db.String(50))
    price = db.Column(db.String(50))
    
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

# Staff Schema
class CarSchema(ma.Schema):
    class Meta:
        fields =('id', 'name', 'price')

# Init Schema 
car_schema = CarSchema()
cars_schema = CarSchema(many=True)

# Get All Staffs
@app.route('/car', methods=['GET'])
def get_staffs():
    all_car = car.query.all()
    result = cars_schema.dump(all_car)
    return jsonify(result)

# Web Root Hello
@app.route('/', methods=['GET'])
def get():
    return jsonify({'ms': 'Hello Cloud '})

# Run Server
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)