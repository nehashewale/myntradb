from flask_restful import Resource
from validator.user import validate_user
from flask import request
from dao.user import get_user_by_phone_number, create_user
from view.user import create_user_object_to_user_json

class User(Resource):
    def post(self):
        # getting body 
        payload = request.json

        # validate schema 
        is_valid_schema = validate_user(payload)

        if is_valid_schema == False:
            return {"response" : "Invalid Schema"}
        
        user = get_user_by_phone_number(payload["phone_number"])
        if user != None:
            return {"response" : "user already exist"}
        
        create_user(payload)
        return {"reponse" : "user created successfully"}
    
    def get(self):
        params = request.args.to_dict()
        
        phone_number = params['phone_number']

        user = get_user_by_phone_number(phone_number)
        user_json = create_user_object_to_user_json(user)
        return  {"response" : user_json}
        
        
        
