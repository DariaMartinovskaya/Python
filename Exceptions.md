### Task 1. Registration (part 1)

```
class RegistrationError(Exception):
    pass

def registration(username, password):
    if type(username) != str or (len(username) < 4 or len(username) > 15) or not username.isalpha():
        raise RegistrationError("Username should be a string of no less than 4 and no more than 15 letters")
    if type(password) != str or (len(password) < 8 or len(password) > 45) or not password.isalnum():
        raise ValueError("Password should be a string of no less than 8 and no more than 45 digitals and/or letters")

    return True

print("VALID DATA")
try:
    result = registration('IvanIvanov', 'abcd12345')
    print(result)
except RegistrationError as e:
    print(f"Error in registration: {e}")
except ValueError as e:
    print(f"Error in password: {e}")
finally:
    print("Done finally")

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
    print("Done finally")

print("")
print("INVALID DATA")

try:
    result = registration("Daria", '!')
    print(result)
except RegistrationError as e:
    print(f"Error in registration: {e}")
except ValueError as e:
    print(f"Error in password: {e}")
finally:
    print("Done finally")
```

Console output:

```
VALID DATA
True
Done finally

INVALID DATA
Error in registration: Username should be a string of no less than 4 and no more than 15 letters
Done finally

INVALID DATA
Error in password: Password should be a string of no less than 8 and no more than 45 digitals and/or letters
Done finally
```

### Task 2. Registration (part 2)

```
class RegistrationError(Exception):
    pass

def registration(username, password):
    if type(username) != str or (len(username) < 4 or len(username) > 15) or not username.isalpha():
        raise RegistrationError("Username should be a string of no less than 4 and no more than 15 letters")
    if type(password) != str or (len(password) < 8 or len(password) > 45) or not password.isalnum():
        raise ValueError("Password should be a string of no less than 8 and no more than 45 digitals and/or letters")

    return True

while True:
        username = input("Enter your login ")
        password = input("Enter your password ")

        try:
            registration(username, password)
            print("Success!")
            break
        except RegistrationError:
            print("Error in registration!")
```
Console output:
```
Enter your login DariaM
Enter your password 1234qwer
Success!
```
