from flask import Flask,render_template
from  pymongo import MongoClient

app = Flask(__name__)
DB_NAME = 'object_detection'
COL_NAME = 'First-try'
MONGO_URI = "mongodb+srv://pandharkardeep35:7762Q0QmsBVhYqLF@deep.pfmz7xz.mongodb.net/"
client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COL_NAME]


# class Room(db.Document):
#     room_number = db.IntField(required=True)
#     number_of_towels = db.IntField(required=True)
#     number_of_mini_bar_items = db.IntField(required=True)
#     status = db.StringField(required=True, choices=['clean', 'not clean'])

@app.route('/')
def index():
    data = collection.find({}, {"_id": 0})
    return render_template("index.html", online_users=data)