from flask import Flask,jsonify,request

app = Flask(__name__)
@app.route('/users',methods=['GET'])
def temp():
    pass
@app.route('/users/<int:user_id>', methods=['GET'])
def temp():
    pass
@app.route('/users', methods=['POST'])
def temp():
    pass
@app.route('/users/<int:user_id>', methods=['PATCH'])
def temp():
    pass
@app.route('/users/<int:user_id>', methods=['DELETE'])
def temp():
    pass
