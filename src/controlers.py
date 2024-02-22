from flask import Flask,jsonify
from flask import request


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
            "firstName": str,
            "lastName": str,
            "age" : int,
            "group": str
        }
        UserControlers.temp_user_storage.append(new_temp_user)
        return jsonify(new_temp_user), 201

    def delete_user(id):
        if id in UserControlers.temp_user_storage:
            UserControlers.temp_user_storage.remove(user)
            return jsonify(user)
        else:
            return jsonify({f"Following id : {id} not found"}), 404
