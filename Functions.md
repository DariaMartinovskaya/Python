### Task 1.

```
def sum_ignore_non_numbers(items):

    total = 0

    for i in items:
        if isinstance(i, (int, float)):
            total += i

    return total

print(sum_ignore_non_numbers([3, 'Hello', 45, 6, 0, 'Portugal']))
```

Console output:

```
54
```

### Task 2. 

```
def is_triangle(a, b, c):
    return (a + b) > c and (a + c) > b and (b + c) > a

print(is_triangle(2, 4, 9))
print(is_triangle(3, 4, 5))
```

Console output:

```
False
True
```

### Task 3. 

```
def average(*args):
    if not args:
        return 0

    result = sum(args) / len(args)
    return result

print(average(1, 2, 3, 4, 5, 6, 7, 8))
print(average())
```

Console output:
```
4.5
0
```

### Task 4. 
```
def common_string(list1, list2, ignore_case=True):
    if ignore_case:
        list1 = [i.lower() for i in list1]
        list2 = [i.lower() for i in list2]
    return [i.lower() for i in list1 if i in list2]

fruits_1 = ['apple', 'APPLE', 'watermelon', 'cherry']
fruits_2 = ['Mango', 'apple', 'orange', 'cherry']

result = common_string(fruits_1, fruits_2)
print(result)
```

Console output:
```
['apple', 'apple', 'cherry']
```
