Task 1. Check if a number is even or odd.

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

Task 2. What is the day today?

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

Task 3. Echo

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
