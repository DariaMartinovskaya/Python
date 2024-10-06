import requests

from pprint import pprint

URL = "https://restful-booker.herokuapp.com/booking/"
URL_AUTH = "https://restful-booker.herokuapp.com/auth"

def get_booking_by_id(id_):
    response = requests.get(URL + f"{id_}")

    return response

# response = get_booking_by_id(482)
# pprint(response.status_code)
# if response.status_code == 200:
#     pprint(response.json())

def get_all_bookings():
    return requests.get(URL)

response = get_all_bookings()

if response.status_code == 200:
    pprint(response.json())

def get_token():
    info = {
        "username" : "admin",
        "password" : "password123"
    }

    response = requests.post(URL_AUTH, json=info)

    return response.json()["token"]

# token = get_token()
# print(token)
def create_new_booking():
    info = {
    "firstname" : "Daria",
    "lastname" : "Martinos",
    "totalprice" : 333,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2024-10-10",
        "checkout" : "2024-10-13"
    },
    "additionalneeds" : "Breakfast"}

    response = requests.post(URL, json=info)

    return response

def patch_booking(id_):
    info = {
        "firstname": "Alex",
        "lastname": "Prokop",
        }

    headers = {
        "Cookie": f"token={get_token()}"
    }

    response = requests.patch(URL + f"{id_}", json=info, headers=headers)

    return response


def delete_booking(id_):
    headers = {
        "Cookie": f"token={get_token()}"
    }

    response = requests.delete(URL + f"{id_}", headers=headers)

    return response

response = create_new_booking()
# pprint(response.json())
# if response.status_code == 200:
pprint(response.json())

my_id = response.json()["bookingid"]
pprint(f"My booking number is {my_id}")

#patch_booking(my_id)
delete_response = delete_booking(my_id)
pprint(f"Delete booking status code: {delete_response.status_code}")

# response = get_booking_by_id(my_id)

#pprint(f"My booking number is {my_id}")
pprint(response.status_code)
pprint(response.json())

get_response = get_booking_by_id(my_id)
pprint(f"Get booking status code after deleting: {get_response.status_code}")
