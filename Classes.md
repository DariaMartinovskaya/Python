### Task 1. Rectangle

```
class Rectangle:
    def __init__ (self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

rect = Rectangle(2, 4)

area = rect.area()
perimeter = rect.perimeter()

print(rect)
print(area)
print(perimeter)
```

Console output:
```
<__main__.Rectangle object at 0x103321580>
8
12
```

### Task 2. Car

```
class Car:
    def __init__ (self, make, max_speed):
        self.make = make
        self.max_speed = max_speed
        self.speed = 0

    def display_speed(self):
        print(self.speed)

    def accelerate(self):
        self.speed = min(self.max_speed, self.speed + 10)

    def brake(self):
        self.speed = max(0, self.speed - 10)

my_toyota = Car("Toyota", 180)
my_toyota.accelerate()
my_toyota.accelerate()

my_toyota.accelerate()
my_toyota.display_speed()
```

Console output:
```
30
```

### Task 3. Bank account

```
class BankAccount:

    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if self._balance - amount < 0:
            print("Insufficient funds!")
        else:
            self._balance -= amount

    def get_balance(self):
        return self._balance

account = BankAccount("Maria", 1000)
account.deposit(700)
account.withdraw(200)
print(account.get_balance())
```

Console output:
```
1500
```

### Task 4. Overdraft
```
class OverdraftAccount(BankAccount):
    def withdraw(self, amount):
            self._balance -= amount


jack_account = OverdraftAccount("Jack", 0)
jack_account.withdraw(100)

jack_account.withdraw(100)
jack_account.withdraw(100)
print(jack_account.get_balance())
```

Console output:
```
-300
```
