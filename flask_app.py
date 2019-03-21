from flask import Flask, request, jsonify
from pymongo import MongoClient
app = Flask(__name__)

# connect to mongodb
client = MongoClient()
db = client.test

# a basic rout command


@app.route("/", methods=["GET", "POST"])
def hello():
    # return differejnt results for http requests
    if "POST" == request.method:
        return jsonify(request.json)  # prints a readable json
    if "GET" == request.method:
        text = " <br> I like "  # <br> becasue we are using html
        for fruit in ["apples", "pears", "melons", "bananas"]:
            text = text + fruit + "<br>"
        return "I've got an http GET-request" + text


if __name__ == "__main__":
    app.run(host='0.0.0.0')
