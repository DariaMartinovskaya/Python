1) Create a variable of the String type

```
n1= 'Stringtype'
```

2) Create a variable of the Integer type

```
n2= 13
```

3) Create a variable of the Float type

```
n3= 13.1
```

4) Create a variable of the Bytes type

```
n4= bytes([13,14,15])
```

5) Create a variable of the List type

```
n5= ['first', 'second', 'third']
```

6) Create a variable of the Tuple type

```
n6= (3, 4)
```

7) Create a variable of the Set type

```
n7= set(["cat",True, 123])
```

8) Create a variable of the Frozen set type

```
n8= frozenset(["cat", "dog", "lion"])
```

9) Create a variable of the Dict type

```
n9= dict(short='dict', long='dictionary')
```

10) Output all of the above variables to the console with the addition of the data type

```
print(n1,type(n1))
print(n2,type(n2))
print(n3,type(n3))
print(n4,type(n4))
print(n5,type(n5))
print(n6,type(n6))
print(n7,type(n7))
print(n8,type(n8))
print(n9,type(n9))
```

Console Output:

```
Stringtype <class 'str'>
13 <class 'int'>
13.1 <class 'float'>
b'\r\x0e\x0f' <class 'bytes'>
['first', 'second', 'third'] <class 'list'>
(3, 4) <class 'tuple'>
{True, 123, 'cat'} <class 'set'>
frozenset({'lion', 'dog', 'cat'}) <class 'frozenset'>
{'short': 'dict', 'long': 'dictionary'} <class 'dict'>
```

11) Create 2 String variables, create a variable in which you concatenate these variables. Output to the console.

```
n10='Daria'
n11='QA Engineer'
n12=n10 + " " + n11
print(n12)
```

Console Output:

```
Daria QA Engineer
```

12) Print variables of type String and Integer in one line using “,” (Comma)

```
n13= 'R. Vasco da Gama'
n14= 1
n15= n13 + ", " + str(n14)
print(n15)
```

Console Output:

```
R. Vasco da Gama, 1
```

13) Print variables of type String and Integer in one line using “+” (Plus)

```
n13= 'R. Vasco da Gama'
n14= 1
n15= n13 + " " + str(n14)
print(n15)
```

Console Output:

```
R. Vasco da Gama 1
```

