"""Server file to handle JSON posts"""

from flask import Flask, request, jsonify
from project import main
app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    """
    Used for testing to validate server is running
    """
    return "Fetch Assignment is Running!"


@app.route('/classify', methods=['POST'])
def classify():
    """
    Main function, handles JSON posts and connection to project.py
    and its functions
    """
    content = request.json
    dimensions = content['dimensions']
    points = content['points']

    result = main(dimensions, points)
    return jsonify({"result": result})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
