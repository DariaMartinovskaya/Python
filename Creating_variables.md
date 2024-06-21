1) Create a variable of the String type

```
n1= 'Stringtype'
```
Str, or string represents sequences of characters such as a message or text.

2) Create a variable of the Integer type

```
n2= 13
```

Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

3) Create a variable of the Float type

```
n3= 13.1
```

Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

4) Create a variable of the Bytes type

```
n4= bytes([13,14,15])
```

The bytes() function returns a bytes object.

It can convert objects into bytes objects, or create empty bytes object of the specified size.

5) Create a variable of the List type

```
n5= ['first', 'second', 'third']
```

Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets.

List items are ordered, changeable, and allow duplicate values.

List items are indexed, the first item has index [0], the second item has index [1] etc.

When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

If you add new items to a list, the new items will be placed at the end of the list.

The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

Since lists are indexed, lists can have items with the same value.

6) Create a variable of the Tuple type

```
n6= (3, 4)
```
Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.

Tuple items are ordered, unchangeable, and allow duplicate values.

Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

7) Create a variable of the Set type

```
n7= set(["cat",True, 123])
```

Sets are used to store multiple items in a single variable. Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

A set is a collection which is unordered, unchangeable, and unindexed.

! Note: Set items are unchangeable, but you can remove items and add new items.

Sets cannot have two items with the same value.

Sets are written with curly brackets.

Bool , or boolean: Represents logical values such as True and False.

8) Create a variable of the Frozen set type

```
n8= frozenset(["cat", "dog", "lion"])
```

The frozenset() function returns an unchangeable frozenset object (which is like a set object, only unchangeable).

9) Create a variable of the Dict type

```
n9= dict(short='dict', long='dictionary')
```

Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered, changeable and do not allow duplicates.


Conclusion:

There are four collection data types in the Python programming language:

- List is a collection which is ordered and changeable. Allows duplicate members.
  
- Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
  
- Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
  
- Dictionary is a collection which is ordered** and changeable. No duplicate members.

*Set items are unchangeable, but you can remove items and add new items.

**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

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

