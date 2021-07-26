import django;django.setup()

from myntradb.user.models import User, Address

def get_user_by_phone_number(phone):
    try:
        user = User.objects.get(phone_number=phone)
        return user
    except Exception as e:
        return None



def create_address(address_data):
    address = Address.objects.create(
        landmark= address_data["landmark"],
        village = address_data["village"],
        taluka = address_data["taluka"],
        district = address_data["district"],
        state = address_data["state"],
        pincode = address_data["pincode"],
        )
    return address


def create_user(user_data):
    primary_address = create_address(user_data["primary_address"])
    shipping_address = create_address(user_data["shipping_address"])

    user = User.objects.create(
        first_name = user_data["first_name"],
        middle_name = user_data["middle_name"],
        last_name = user_data["last_name"],
        phone_number = user_data["phone_number"],
        gender = user_data["gender"],
        primary_address = primary_address,
        shipping_address = shipping_address,
        )
    return user


def update_user(user,user_data):

    user.first_name = user_data["first_name"]
    user.middle_name = user_data["middle_name"]
    user.last_name = user_data["last_name"]
    user.gender = user_data["gender"]

    user.primary_address.landmark= user_data["primary_address"]["landmark"]
    user.primary_address.village = user_data["primary_address"]["village"]
    user.primary_address.taluka = user_data["primary_address"]["taluka"]
    user.primary_address.district = user_data["primary_address"]["district"]
    user.primary_address.state = user_data["primary_address"]["state"]
    user.primary_address.pincode = user_data["primary_address"]["pincode"]

    user.shipping_address.landmark= user_data["shipping_address"]["landmark"]
    user.shipping_address.village = user_data["shipping_address"]["village"]
    user.shipping_address.taluka = user_data["shipping_address"]["taluka"]
    user.shipping_address.district = user_data["shipping_address"]["district"]
    user.shipping_address.state = user_data["shipping_address"]["state"]
    user.shipping_address.pincode = user_data["shipping_address"]["pincode"]

    user.save()
    return 




def get_all_users():
    users = User.objects.all()
    return users 
