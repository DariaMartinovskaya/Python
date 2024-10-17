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

### Task 3. Dear diary...

```
with open("journal.txt", "r", encoding="utf-8") as file:
    pass

    while True:
        string = input("Write the option: read, write, exit: ").lower()

        if string == 'write':
            with open("journal.txt", "a", encoding="utf-8") as file:
                new_line = input("Enter text to be included into the file: ")
                file.write(new_line + '\n')
                print("Text is added.")
        elif string == 'read':
            with open("journal.txt", "r", encoding="utf-8") as file:
                data = file.read()
                print(data)
                file.close()
        elif string == 'exit':
            with open("journal.txt", "r", encoding="utf-8") as file:
                print("See you later!")
                file.close()
                break
        else:
            continue
```
Console output:
```
Write the option: read, write, exit: write
Enter text to be included into the file: text text text
Text is added.
Write the option: read, write, exit: read
text text text

Write the option: read, write, exit: exit
See you later!
```
