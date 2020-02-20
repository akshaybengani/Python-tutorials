# Welcome to Recap Guide
These small notes are just for a quick recap of python functions, operators, data types, and lot more.

## Print function
Always use String in Double Quotes and all integers, boolean, floats and variables without quotes.
```py
print("Hello World")
```

## Python Interpreter as Calculator
We can use the python interpreter like calculator without any functions or variables, just open the terminal and type python and get started.

## Comments in Python
We can add single line comments by using #.<br>
We can add multiline comments using ''' or """ or ```

## Escape Sequence Characters
*   For next line we use \n
*   If you want to print a quote in String then we need to use \
*   For tabs use \t
```py
print("Akshay is \n Good Boy \t and an Intelligent person")
```
## Variables, type function and typecasting
Storage boxes in python which is used to store some data or value either statically or dynamically.
*   There is a function called ```type()``` which is used to print the type of the variable or value.
```py
var1 = "Akshay Bengani"
var2 = 123
var3 = 23.4
var4 = True

type(var1)
type(var2)
type(var3)
type(var4)
```
*   In case when you need to convert type of a variable then we need to use these special functions used to typecast the entire variable.
```py
var1 = "54"
var2 = "20"
str()
int()
float()
bool()
print(int(var1) + int(var2))
```
*   Print something multiple times
```py
print(100 * "Hello this is Akshay")
```
## Input function
To get a user input we have a function called ```input()```
```py
print("Enter a number")
var1 = input()
print("You entered ", int(var1) + 10)
```
## String Datatypes and Functions
*   To get a particular character of a string use [] with the index position.
```py
var1 = "Akshay is a Good boy"
print(var1[2])
```
*   String Slicing is used to get a particular slice of a string or a part of a string.
*   In case if you entered the ending number more then the length then there is no error it just print the maximum as he can.
```py
var1 = "Akshay is a Good boy"
print(var1[2:6])
print(var1[2:42])
```
*   To get a length of a string use ```len()``` function
```py
var1 = "Akshay is a Good Boy"
print(len(var1))
```
*   In case if I need to skip the characters in a string we use the :: for slicing.
*   To skip 1 character from a part of string or whole string use this ```::```
```py
var1 = "Akshay is a Good Boy"
print(var1[0:20:2])
print(var1[0::2])
print(var1[:20:2])
print(var1[::2])
```
*   Negative indexes in String, this is used when you need to read the string from the end, as such all the string operations will be done reverse from the end.
```py
var1 = "Akshay is a Good Boy"
print(var1[-1])
print(var2[-3])
print(-4:-2)
print()
```
*  Alphanumeric functions check that the string contains anything else then characters and numbers, it checks for symbols and spaces.
```py
var1 = "Akshay is a good boy"
print(var1.isalnum())
print(var1.isalpha())
```
*  Check that the string end with a specific value or not
```py
var1 = "Akshay is a Good Boy"
print(var1.endswith("Boy"))
```
*   Count a specific character or word in the whole string use the ```count()``` function.
```py
var1 = "Akshay is a Good Boy"
print(var1.count('o'))
```
*   To Capitalize the 1st character of a String we use the function ```capitalize()```
```py
var1 = "akshay is a good boy"
print(var1.capitalize())
```
*   To find something position in a String we use the function ```find()``` this will return the starting position of the search item.
```py
var1 = "Akshay is a Good Boy"
print(var1.find("is"))
```
*   To replace something in string with something use the function ```replace()```
```py
var1 = "Akshay is a Good boy"
print(var1.replace('is','are'))
```
*   In case if you need more inbuilt String functions Google it.

## List and List Functions
*   To create a list we use ```[]``` and store it in a variable.
```py
list1 = ['Apple','Vim Bar',12,34.55,True,'Orange']
print(list1[2])
print(list1)
```
*   To sort a list of numbers in ascending or decending order.
```py
numbers = [43,564,353,34,6,3,75,35,5]
# To sort in ascd order
numbers.sort()
# To sort in decd order just reverse the sorted one
numbers.reverse()
print(numbers)
```
*   List Slicing
```py
numbers = [43,564,353,34,6,3,75,35,5]
print(numbers[0:5])
print(numbers[:5])
print(numbers[2:])
print(numbers)
```
*   Extended Slicing
```py
numbers = [43,564,353,34,6,3,75,35,5]
print(numbers[::1])
print(numbers[::2])

print(numbers[::-1])
print(numbers[::-2])
```
*   To add a value in a list use the function ```append()```
```py
numbers = []
numbers.append(21)
numbers.append(22)
numbers.append(23)
numbers.append(24)
print(numbers)
```
*   To add a value in a list at a specific position use the function ```insert()```
```py
numbers = []
numbers.insert(0,53)
numbers.insert(1,53)
numbers.insert(13,53)
```
*   To remove a value from a list use the function ```remove()```, it will remove the 1st occurance of the value.
```py
numbers = [43,564,353,34,6,3,75,35,5]
numbers.remove(564)
```
*   To remove the last value of the list then use the ```pop()``` function.
```py
numbers = [43,564,353,34,6,3,75,35,5]
numbers.pop()
```
## Tuples and Tuple Functions
*   Tuples is used to create Immutable list which cannot be changed.
*   Tuples use ```()``` and list uses ```[]```.
*   You cannot change a value of a Tuple
*   But we can add values in a tuple using append not insert function.
*   When we need to create a single value tuple we need to add a ```,``` after the 1st value.
```py
tp = (1,)
```
## Dictionaries and Dictionary Functions
*   Dictionary is nothing but key value pairs.
```py
d2 = {'Akshay':'Chicken','Aastha':'Roti','Shivank':'Patties'}
print(d2['Akshay'])
print(d2['Aastha'])
```
*  We can create nested Dictionaries within Dictionaries.
```py
d2 = {'Akshay':'Chicken','Aastha':'Roti','Shivank':'Patties','Kirti':{'B':'Poha','L':'Bhindi','D':'Paneer'},'Meenal':'Aalu'}
print(d2['Kirti']['L'])
```
*   In case you need to add data in Dict
```py
d2['Ankit'] = "Junk Food"
```
*   To delete an entry from dict
```py   
d2['Ankit'] = "Junk Food"
del d2['Ankit']  
```
*   In case you need to make a copy of a dictionary you need to use the copy function because when we assign dictionary like variables it returns the pointer as such you should use ```copy()``` function for making a fresh new copy of the Dict.
```py
d2 = {'Akshay':'Chicken','Aastha':'Roti','Shivank':'Patties'}
d3 = d2.copy()
print(d3)
```
*  To update a value in Dict use the update() function
```py
d2 = {'Akshay':'Chicken','Aastha':'Roti','Shivank':'Patties'}
d2.update({'Akshay':'Tandoor'})
```
*   To get keys of the dict
```py
d2 = {'Akshay':'Chicken','Aastha':'Roti','Shivank':'Patties'}
print(d2.keys())
```
## Set and its functions
*   Set is a data structure in Python which is used to store unique values, and it can implement all kind of mathematical operations on set.
```py
s = set()
print(type(s))
l = [1, 2, 3, 4]
s_from_list = set(l)
print(s_from_list)
print(type(s_from_list))
s.add(1)
s.add(2)
s.remove(2)
s1 = {4, 6}
print(s.isdisjoint(s1))
```
## IF Else and Elif
*   I am skipping this part because its very easy and nothing to recap.

