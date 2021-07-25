


def create_user_object_to_user_json(user):
    return {
        "first_name": user.first_name,
        "middle_name": user.middle_name,
        "last_name": user.last_name,
        "phone_number": user.phone_number,
        "gender": user.gender,
        "primary_address": {
            "village": user.primary_address.village,
            "landmark": user.primary_address.landmark,
            "taluka": user.primary_address.taluka,
            "district": user.primary_address.district,
            "state": user.primary_address.state,
            "pincode": user.primary_address.pincode
            },
        "shipping_address": {
            "village": user.shipping_address.village,
            "landmark": user.shipping_address.landmark,
            "taluka": user.shipping_address.taluka,
            "district": user.shipping_address.district,
            "state": user.shipping_address.state,
            "pincode": user.shipping_address.pincode
            }
        }



def multiple_user_view(users):
    view_user = []
    for user in users:
        u = create_user_object_to_user_json(user)
        view_user.append(u)
    return view_user