```

import functions as func

```

### Test 1. GET

```
def test_get_all_bookings():
    response = func.get_all_bookings()

    assert response.status_code == 200, "Status code is not 200!"
```

### Test 2. POST

```
def test_create_new_booking():

# Expected data
    data = {
        "firstname": "Daria",
        "lastname": "Martinos",
        "totalprice": 333,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-10-10",
            "checkout": "2024-10-13"
        },
        "additionalneeds": "Breakfast"}

# Creating a new booking by using function
    new_booking = func.create_new_booking()

# Receiving new booking's ID
    id_ = new_booking.json()["bookingid"]

# Receiving booking data by ID
    response = func.get_booking_by_id(id_)
    response_data = response.json()

    print(response_data)

# Checking that data is the same as expected data
    assert response_data["firstname"] == data["firstname"]
    assert response_data["lastname"] == data["lastname"]
```

### Test 3. PATCH
```
def test_update_booking():
# Creating new booking (initial data)
    initial_data = {
        "firstname": "Daria",
        "lastname": "Martinos",
        "totalprice": 333,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-10-10",
            "checkout": "2024-10-13"
        },
        "additionalneeds": "Breakfast"}

# Creating a new booking by using function
    new_booking = func.create_new_booking()
    print(new_booking)

# Receiving new booking's ID
    id_ = new_booking.json()["bookingid"]
    print(id_)

# Receiving token
    new_token = func.get_token()
    print(new_token)

# Updating booking data using PATCH (Updated data)
    updated_data = {
        "firstname": "Alex",
        "lastname": "Prokop",}

    updated_booking = func.patch_booking(id_)
    print(updated_booking)

# Receiving booking data by ID
    response = func.get_booking_by_id(id_)
    response_data = response.json()

    print(response_data)

# Checking that data is the same as expected data
    assert response_data["firstname"] == updated_data["firstname"]
    assert response_data["lastname"] == updated_data["lastname"]
```

### Test 4. DELETE
```
def test_delete_booking():
# Creating new booking (initial data)
    initial_data = {
        "firstname": "Daria",
        "lastname": "Martinos",
        "totalprice": 333,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-10-10",
            "checkout": "2024-10-13"
        },
        "additionalneeds": "Breakfast"}

# Creating a new booking by using function
    new_booking = func.create_new_booking()
    print(new_booking)

# Receiving new booking's ID
    id_ = new_booking.json()["bookingid"]
    print(id_)

# Receiving token
    new_token = func.get_token()
    print(new_token)

# Deleting booking data using DELETE
    delete_booking = func.delete_booking(id_)
    print(delete_booking.status_code)

# Receiving booking data by ID (it is expected that there is no booking with requested id)
    response = func.get_booking_by_id(id_)

    print(response.status_code)

# Checking that there is no booking with requested id
    assert response.status_code == 404

```

Test results:

```
/Users/dariamartinovskaya/Documents/pythonProject1/.venv/bin/python /private/var/folders/dc/5w6tkw1d4tj7_rpzlm92m4hh0000gn/T/AppTranslocation/FA4DFE80-556E-418E-BAB5-1AA014BF597E/d/PyCharm CE.app/Contents/plugins/python-ce/helpers/pycharm/_jb_pytest_runner.py --path /Users/dariamartinovskaya/Documents/pythonProject1/test_bookings.py 
Testing started at 21:15 ...
Launching pytest with arguments /Users/dariamartinovskaya/Documents/pythonProject1/test_bookings.py --no-header --no-summary -q in /Users/dariamartinovskaya/Documents/pythonProject1

============================= test session starts ==============================
collecting ... collected 4 items

test_bookings.py::test_get_all_bookings PASSED                           [ 25%]
test_bookings.py::test_create_new_booking PASSED                         [ 50%]{'firstname': 'Daria', 'lastname': 'Martinos', 'totalprice': 333, 'depositpaid': True, 'bookingdates': {'checkin': '2024-10-10', 'checkout': '2024-10-13'}, 'additionalneeds': 'Breakfast'}

test_bookings.py::test_update_booking PASSED                             [ 75%]<Response [200]>
2609
e982849f6c5d198
<Response [200]>
{'firstname': 'Alex', 'lastname': 'Prokop', 'totalprice': 333, 'depositpaid': True, 'bookingdates': {'checkin': '2024-10-10', 'checkout': '2024-10-13'}, 'additionalneeds': 'Breakfast'}

test_bookings.py::test_delete_booking PASSED                             [100%]<Response [200]>
2636
b41f682ed776838
201
404


============================== 4 passed in 12.78s ==============================

Process finished with exit code 0
```
