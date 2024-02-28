from flask import Flask,jsonify
from flask import request
from src.user import User

class UserControlers:
    temp_user_storage = []


    def get_all_aviable_users(self):
        return jsonify(UserControlers.temp_user_storage)

    def get_single_user(id):
        if id in UserControlers.temp_user_storage:
            return jsonify(UserControlers.temp_user_storage.id)
        else:
            return {f"User not found with following id : {id}"} , 404


    def create_an_user(self):
        new_temp_user = {
            "id": len(UserControlers.temp_user_storage) + 1,
            "first_Name": str,
            "last_Name": str,
            "age" : int,
            "group": str
        }
        UserControlers.temp_user_storage.append(new_temp_user)
        return jsonify(new_temp_user), 201

    def delete_user(self, id):
        if id in UserControlers.temp_user_storage:
            UserControlers.temp_user_storage.remove(User)
            return jsonify(User)
        else:
            return jsonify({f"Following id : {id} not found"}), 404
    def update_user(self):
        pass
