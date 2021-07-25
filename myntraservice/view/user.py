


def create_user_object_to_user_json(user):
    return {
        "first_name": user.first_name,
        "middle_name": user.middle_name,
        "last_name": user.last_name,
        "phone_number": user.phone_number,
        "gender": user.gender,
        "primary_address": {
            "village": user.primary_address__village,
            "landmark": user.primary_address__landmark,
            "taluka": user.primary_address__taluka,
            "district": user.primary_address__district,
            "state": user.primary_address__state,
            "pincode": user.primary_address__pincode
            },
        "shipping_address": {
            "village": user.shipping_address__village,
            "landmark": user.shipping_address__landmark,
            "taluka": user.shipping_address__taluka,
            "district": user.shipping_address__district,
            "state": user.shipping_address__state,
            "pincode": user.shipping_address__pincode
            }
        }
