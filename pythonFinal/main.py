from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
import logging
import sys

# Instantiate application
app = Flask(__name__)
CORS(app)

# Ha ezt nem adnánk hozzá amiatt error lenne.
app.secret_key = "megoldando"

# Set configs
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/pythoncrud'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
logging.basicConfig(level=logging.DEBUG)
# Create DB object
db = SQLAlchemy(app)

# Marshmallow object
ma = Marshmallow(app)


# Automaticly create tables
class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    position = db.Column(db.String(100))

    def __repr__(self):
        return self.id


# Create scheme
class dataSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "email", "phone", "position")


# Instance of scheme
data_schemeNotMany = dataSchema(many=False)
data_schemeMany = dataSchema(many=True)


# Default route
@app.route("/", methods=["GET"])
def listing():
    datas = Data.query.all()
    json_str = data_schemeMany.dump(datas)
    return jsonify(json_str)


@app.route("/addData/", methods=["POST"])
def add_data():
    try:
        data = request.get_json(force=True)
        name = data["name"]
        email = data["email"]
        phone = data["phone"]
        position = data["position"]
        print('Hello world!', file=sys.stderr)
        new_data = Data(name=name, email=email, phone=phone, position=position)
        db.session.add(new_data)
        db.session.commit()
        return jsonify(new_data)
    except Exception as e:
        return jsonify({"Error ": e})


@app.route("/updateData/<int:id>", methods=['POST'])
def updateData(id):
    dataToDelete = Data.query.get_or_404(int(id))
    data = request.get_json(force=True)
    id = data["id"]
    id = int(id)
    name = data["name"]
    email = data["email"]
    phone = data["phone"]
    position = data["position"]
    new_data = Data(id = id, name=name, email=email, phone=phone, position=position)
    dataToDelete = Data.query.get_or_404(int(id))
    db.session.delete(dataToDelete)
    db.session.add(new_data)
    db.session.commit()

    return data_schemeNotMany.jsonify(data)


@app.route("/deleteData/<int:id>", methods=['GET', 'POST'])
def deleteData(id):
    data = Data.query.get_or_404(int(id))
    db.session.delete(data)
    db.session.commit()
    return jsonify({"Msg": "Success delete"})


if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Enélkül hibára futna, mert elöbb lére kell hozni a táblát bármi elött.
        app.run(debug=True)