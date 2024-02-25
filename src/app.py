from flask import Flask,jsonify,request
from controlers import UserControlers
app = Flask(__name__)
@app.route('/users',methods=['GET'])
def get_all_users():
    return jsonify(UserControlers.get_all_aviable_users())
@app.route('/users/<int:user_id>', methods=['GET'])
def get_one_user(id):
    return jsonify(UserControlers.get_single_user(id))
@app.route('/users', methods=['POST'])
def create_user():
    return jsonify(UserControlers.create_an_user(request.json)),201
@app.route('/users/<int:user_id>', methods=['PATCH'])
def update_user(id):
    return jsonify(UserControlers.update_user(id))
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(self,id):
    return jsonify(UserControlers.delete_user(id))