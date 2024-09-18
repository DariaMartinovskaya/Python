### Task 1. Check if a number is even or odd.

```
n = int(input())

if n % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```

Console output:
```
5
Odd number
```

```
345678
Even number
```

### Task 2. What is the day today?

```
day = input()

if day == "Saturday" or day == "Sunday":
    print("Today is weekend!")
elif day == "Wednesday":
    print("Today I have an appointment with a dentist at 3.30 p.m. today")
else:
    print("Today is a simple day.")
```

Console output:
```
Wednesday
Today I have an appointment with a dentist at 3.30 p.m. today
```

```
Monday
Today is a simple day.
```

```
Sunday
Today is weekend!
```

### Task 3. Echo

```
n = int(input())
text = input()

for _ in range(n):
    print(text)
```

Console output:

```
3
Text
Text
Text
Text
```
### Task 4. Counting the amount of vowels letters
```
message = input("Fill in input data (in English): ")
vowels = "aeiou"

message = message.lower()

count = 0
for char in message:
    if char in vowels:
        count += 1

print("Number of vowels:", count)
```
Console input:
```
Fill in input data (in English): Python coding
Number of vowels: 3
```

### Task 5. Sum of numbers input until the minus number

```
total_sum = 0

while True:
    n = int(input("Input a number: "))
    if n < 0:
        break
    total_sum += n

print("Total sum: ", total_sum)
```

Console output:
```
Input a number: 3
Input a number: 4
Input a number: 5
Input a number: 6
Input a number: -5
Total sum:  18
```
