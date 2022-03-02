from flask import Flask, redirect, url_for, request, jsonify
from project import main
app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
    return "Fetch Assignment is Running!"

@app.route('/classify',methods = ['POST'])
def classify():
    content = request.json
    dimensions = content['dimensions']
    points = content['points']

    result = main(dimensions,points)
    return jsonify({"result":result})


if __name__ == '__main__':
   app.run(debug = True, host='0.0.0.0')