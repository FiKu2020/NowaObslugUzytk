from flask import Flask,jsonify
from flask import request


class UserControlers:
    temp_user_storage = []


    def get_all_aviable_users(self):
        return jsonify(UserControlers.temp_user_storage)

    def create_an_user(self):
        new_temp_user= {
            "id": len(UserControlers.temp_user_storage) + 1,
            "firstName": str,
            "lastName": str,
            "age" : int,
            "group": str
        }
        UserControlers.temp_user_storage.append(new_temp_user)
        return jsonify(new_temp_user),201