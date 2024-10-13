### Task 1. Registration (part 1)

```
class RegistrationError(Exception):
    pass

def registration(username, password):
    if type(username) != str:
        raise RegistrationError("Username should be a string.")
    if type(password) != str or (len(password) < 8 or len(password) > 45) or not password.isalnum():
        raise ValueError("Password should be a string of no less than 8 and no more than 45 digitals and/or letters")
    return "Successful registration"

print("VALID DATA")
try:
    result = registration('IvanIvanov', 'abcd12345')
    print(result)
except RegistrationError as e:
    print(f"Error in registration: {e}")
except ValueError as e:
    print(f"Error in password: {e}")
finally:
    print("Done finnaly")

print("")
print("INVALID DATA")

try:
    result = registration(123, '!')
    print(result)
except RegistrationError as e:
    print(f"Error in registration: {e}")
except ValueError as e:
    print(f"Error in password: {e}")
finally:
    print("Done finnaly")
```

Console output:

```
VALID DATA
Successful registration
Done finnaly

INVALID DATA
Error in registration: Username should be a string.
Done finnaly

INVALID DATA
Error in password: Password should be a string of no less than 8 and no more than 45 digitals and/or letters
Done finnaly
```
