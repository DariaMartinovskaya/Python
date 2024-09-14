### Task 1. Special digitals.
Generate a list of numbers consisting of digitals in the range 0 to 100 (inclusive), which are divisible by both 2 and 3.

Print the list of numbers to the screen.

Option 1 (List comprehension)

```
numbers = [i for i in range(101) if i % 2 == 0 and i % 3 == 0]

print(numbers)
```

Option 2 (Cycle)

```
numbers = []

for i in range(101):
    if i % 2 == 0 and i % 3 == 0:
        numbers.append(i)

print(numbers)
```

### Task 2. There is a list items = [1.2, 3, None, 100, {'info': 'bla-bla'}, 44, 'Hi!', 99, 44.32, None]
Create a new list numbers that contains only the integers (int) and real numbers (float) from the list items.
Print the sum of the numbers in numbers.

```
items = [1.2, 3, None, 100, {'info': 'bla-bla'}, 44, 'Hi!', 99, 44.32, None]

numbers = [i for i in items if isinstance(i, (int, float))]

print(sum(numbers))
```

### Task 3. Message history.

- Create a messages list that will store “messages”.
  
- The program should ask the user in an infinite loop to enter a message (string) from the keyboard and save it in the messages list.
  
Moreover, the program should remember no more than 5 last messages.

That is, if the length of the messages list exceeds 5, then the first message in it should be deleted.

If the user entered “Bye”, then the program should display “Okay, bye!” and a list of the last messages on the screen.

Example: if the user entered the following messages (without quotes): “Hello!”, “How are you?”, “How are you?”, “Blah-blah-blah”, “What's new?”, “Sorry, I'm busy”, “Bye”

```
messages = []

while True:
    message = input("Enter your message: ")
    messages.append(message)
    if len(messages) > 5:
        del messages[0]
    if message == "Bye":
        print("Okay, bye!")
        break

print(messages)
```

### Tesk 4. Without duplicates.
There is a list numbers = [15, 3, 8, 42, 3, 23, 8, 7, 42, 1, 9, 23, 15, 5, 9, 4, 6, 1]
- Create a new list where all duplicates will be deleted from the list numbers
- Sort the final list and print
The task should be resolved using set and no

```
numbers = [15, 3, 8, 42, 3, 23, 8, 7, 42, 1, 9, 23, 15, 5, 9, 4, 6, 1]
set_numbers = set(numbers)

sorted_numbers = sorted(set_numbers)

print(sorted_numbers)

numbers = [15, 3, 8, 42, 3, 23, 8, 7, 42, 1, 9, 23, 15, 5, 9, 4, 6, 1]
numbers_new = []

for i in numbers:
    if i not in numbers_new:
        numbers_new.append(i)

sorted_numbers = sorted(numbers_new)

print(sorted_numbers)
```

### Task 5. Market

```
products = {
"apple": {"quantity": 10, "price": 100},
"banana": {"quantity": 20, "price": 50},
"orange": {"quantity": 15, "price": 80},
"grape": {"quantity": 8, "price": 120},
"milk":{"quantity": 12, "price": 90},
"bread": {"quantity": 30, "price": 40}
}

for data in products.values():
    data["price"] *= 1.2

del products["milk"]

products["salt"] = {"quantity": 7, "price": 12}

total = 0

for data in products.values():
    total += data ["quantity"] * data["price"]

print(total)
```

### Task 6.

```
keys = ['name', 'age', 'city', 'occupation', 'email', 'phone', 'hobby', 'education', 'company', 'salary']
values = ['Alice', 30, 'New York', 'Engineer', 'alice@example.com', '+1234567890', 'Reading', 'Masters in Computer Science', 'TechCorp', 90000]

info = {}

for i in range(len(keys)):
    info[keys[i]] = values[i]

print(info)
```

### Task 7.

```
secret_message = "2__234йшDGмёшSDFжкъrrrщзнSDF78юкйфуSDFшёью$#2Sшжйи3%узфsdf34нкфыvvя"

cipher = {
    "а": "щ", "б": "д", "в": "ю", "г": "ф", "д": "з", "е": "м", "ё": "р",
    "ж": "т", "з": "п", "и": "я", "й": "с", "к": "н", "л": "э", "м": "к",
    "н": "л", "о": "ё", "п": "ж", "р": "ц", "с": "б", "т": "у", "у": "в",
    "ф": "о", "х": "и", "ц": "х", "ч": "г", "ш": "е", "щ": "й", "ъ": "ы",
    "ы": "ч", "ь": "ш", "э": "ъ", "ю": "а", "я": "ь"
}
decrypted_message = ""

for c in secret_message:
    if c in cipher:
        decrypted_message += cipher[c]

print(decrypted_message)
```
