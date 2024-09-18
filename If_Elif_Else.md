### Steps

 1. Create a variable int_item with the value 10

```
int_item = 10
```

 2. Create a variable comp_item with the value 18

```
comp_item = 18
```

 3. Create a variable mult_int where int_item * 2

```
mult_int = int_item*2
```

4. Create a variable item_2 with the value True

```
item_2 = True
```

5. Create a variable item_3 with the value False

```
item_3 = False
```

6. Create a variable item_4 with the value 0

```
item_4 = 0
```

7. Create a variable item_5 with the value 1

```
item_5 = 1
```

8. Create a variable usd_item with the value ‘usd’

```
usd_item = 'usd'
```

9. Create a variable usd_usd_rate with the value 1

```
usd_usd_rate = 1
```

10. Create a variable eur_item with the value ‘eur’

```
eur_item = 'eur'
```

11. Create a variable usd_eur_rate with the value 0.86

```
usd_eur_rate = 0.86
```

12. Create a variable uah_item with the value ‘uah’

```
uah_item = 'uah'
```

13. Create a variable usd_uah_rate with the value 26.23

```
usd_uah_rate = 26.23
```

14. Create a variable chf_item with the value ‘chf’

```
chf_item = 'chf'
```

15. Create a variable usd_chf_rate with the value 0.91

```
usd_chf_rate = 0.91
```

16. Create a variable rub_item with the value ‘rub’

```
rub_item = 'rub'
```

17. Create a variable usd_rub_rate with the value 71.88

```
usd_rub_rate = 71.88
```

18. Create a variable byn_item with the value ‘byn’

```
byn_item = 'byn'
```

19. Create a variable usd_byn_rate with the value 2.46

```
usd_byn_rate = 2.46
```

20. Сreate if with the following condition: if mult_int more than comp_item, print into the console (“The variable mult_int is more”, comp_item)

```
print("Step No. 20:")
if mult_int > comp_item:
    print("The variable mult_int is more", comp_item)
print()
```

21. Create a variable div_int with dividing of int_item by 2

```
div_int = int_item/2
```

22. Сreate if with the following condition: if div_int is less than comp_item, print into the console (“The variable div_int is less”, comp_item)

```
print("Step No. 22:")
if div_int < comp_item:
    print("The variable div_int is less", comp_item)
print()
```

23. Create a variable item_1 in which add 10 to the int_item variable

```
item_1 = int_item + 10
```

24. Сreate if with the following condition: if item_1 is less than comp_item, print into the console (“The variable item_1 is less”, comp_item), otherwise, print into the console (“The variable item_1 is more or equal”, comp_item)

```
print("Step No. 24:")
if item_1 < comp_item:
    print("The variable item_1 is less", comp_item)
else:
    print("The variable item_1 is more or equal", comp_item)
print()
```

25. Сreate if with the following condition: if item_2, print into the console (“The variable item_2 = ”, item_2), otherwise, print into the console (“The variable item_2 = ”, item_3)

```
print("Step No. 25:")
if item_2:
    print("The variable item_2 = ", item_2)
else:
    print("The variable item_2 = ", item_3)
print()
```

26. Сreate if with the following condition: if item_3, print into the console (“The variable item_3 = ”, item_2), otherwise, print into the console (“The variable item_3 = ”, item_3)

```
print("Step No. 26:")
if item_3:
    print("The variable item_3 = ", item_2)
else:
    print("The variable item_3 = ", item_3)
print()
```

27. Сreate if with the following condition: if item_5, print into the console (“The variable item_5 = ”, item_5), otherwise, print into the console (“The variable item_5 = ”, item_4)

```
print("Step No. 27:")
if item_5:
    print("The variable item_5 = ", item_5)
else:
    print("The variable item_5 = ", item_4)
print()
```

28. Сreate if with the following condition: if item_4, print into the console (“The variable item_4 = ”, item_5), otherwise, print into the console (“The variable item_4 = ”, item_4)

```
print("Step No. 28:")
if item_4:
    print("The variable item_4 = ", item_5)
else:
    print("The variable item_4 = ", item_4)
print()
```

29. Create a variable currency_convertor with the value item_2

```
currency_convertor = item_2
```

30. Сreate if with the following condition: if currency_convertor, preform the following steps of this task, otherwise, print into the console (“The variable currency_convertor = ”, item_3)

31. Within if currency_convertor create the following If conditions:

31.1 Create a variable currency_usd with the value usd_item

31.2 Create a variable target_currency with the value eur_item

31.3 Create a variable target_currency_amount with the value 50

31.4 Create a variable currency_result with the value 0

31.4 Create if statement with the following condition: if target_currency is equal to ‘eur’, inside this if statement inside the value of the variable currency_result calculate how many dollars you get with target_currency_amount and usd_eur_rate. Print the result into the console (target_currency_amount, eur_item, “=”, currency_result, usd_item)

31.5 Create elif statement with the following condition: if target_currency is equal to ‘uah’, inside this if statement inside the value of the variable currency_result calculate how many dollars you get with target_currency_amount and usd_uah_rate. Print the result into the console (target_currency_amount, uah_item, “=”, currency_result, uah_item)

31.6 Create elif with other currencies

31.7 Create else statement as the last one with prenting into the console (“Unknow currency”) upon fulfillment

```
print("Steps No. 30-31:")

if currency_convertor:
    currency_usd = usd_item
    target_currency = eur_item
    target_currency_amount = 50
    currency_result = 0
    if target_currency == 'eur':
            currency_result = target_currency_amount * usd_eur_rate
            print(target_currency_amount, eur_item, "=", currency_result, usd_item)
    elif target_currency == 'uah':
            currency_result = target_currency_amount * usd_uah_rate
            print(target_currency_amount, uah_item, "=", currency_result, uah_item)
    elif target_currency == 'chf':
            currency_result = target_currency_amount * usd_chf_rate
            print(target_currency_amount, chf_item, "=", currency_result, chf_item)
    elif target_currency == 'rub':
            currency_result = target_currency_amount * usd_rub_rate
            print(target_currency_amount, rub_item, "=", currency_result, rub_item)
    elif target_currency == 'byn':
            currency_result = target_currency_amount * usd_byn_rate
            print(target_currency_amount, byn_item, "=", currency_result, byn_item)
    else:
            print("Unknown currency")
else:
    print("The variable currency_convertor = ", item_3)
```

## Console output:

```
Step No. 20:
The variable mult_int is more 18

Step No. 22:
The variable div_int is less 18

Step No. 24:
The variable item_1 is more or equal 18

Step No. 25:
The variable item_2 =  True

Step No. 26:
The variable item_3 =  False

Step No. 27:
The variable item_5 =  1

Step No. 28:
The variable item_4 =  0

Steps No. 30-31:
50 eur = 43.0 usd
```
