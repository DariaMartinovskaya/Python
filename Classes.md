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
