# Python Basics
Python is a programming language who do not use semicolon inn the end of the statement.

## Print in Python
In Python 2 you can print without using brackets
```
print "Akshay Bengani"
```
This is allowed in Python 2 but not in Python 3 
```
print("Akshay Bengani");
```
This is important we have to use () while in the print function.

## Input in Python
You can take input in python by using the input() function
```
a = input("Enter your name here ");
```
This will take input and store it in a variable

# Python Expressions
Expressions are made up of variables, contants, operators, functions, Reserved Words, Comments and lot more cool stuff.

## Comments in Python
To Comment in python we use \# to comment out something.

## Type conversion 
In Python when we take input we use input() function this function only takes string type so we need to typecast when we needed a Integer operations or any other type operation other then String.

```python
age = input("Enter your age ")
age = int(age) + 5
print(age)
```

In order to do so for example we need to print age with adding +5 in it so we need to typecast String to Integer byusing int() function.

## Print Arguments
In python3 if u want to print multiple things in one print function we use ',' for the case in order to pass multiple arguments for example
```python
name = "Akshay Bengani"
print("My name is ",name)
```
Note '+' operator also works and ',' operator only works in python3 properly.

# Conditional Statements
Similar like other programming language python also uses if statements but with some different programming syntax
<br>In Python we use : insteed of blocks and a tab indentation in order to recorganize the block of code for example
```python
if z>5:
    print("Hey there")
```
## Comparision Operators

* **Boolean Expressions** ask a question and produce a Yes or No result which we use to control program flow.<br>

*  **Boolean Expressions** using **Comparison Operators** evaluate to True/False or Yes/No

* Comparison operators at variables but do not change the variables.

-----------------------------------------
|    Python    |    Meaning             |
|--------------|------------------------|
|    <         |Less Then               |
|    <=        |Less Then or Equal to   |
|    ==        |Equal to                |
|    >=        |Greater than or Equal to|
|    >         |Greater Than            |
|    !=        |Not equal               |
-----------------------------------------

## Indentation
In python indentation is very important in python it is not just for the better understandable of code but also for representing the block of code.
<br>
You can use text editors like VSCode, Atom, Sublime Text. These text editors come with autoarrangement and can handle the automotic indentation.

## Conditional Statements
Similar like other languages we have if else and elseif(elif) in python
```python
x=0
if x<2:
    print("small")
elif x<10:
    print("Medium")
else :
    print("LARGE")
print("All Done")
```
# Functions in Python
Functions are the reuasble code we can call or invoke them to reuse the code inside the code

## In built functions
In Python we have some predefined functions like max() and min() these functions are called as In built functions and are used to calculate the largest value of the parameter passed inside..

```python
big = max("HelloWorld")
small = min("HelloWorld")
print(big)  
print(small)
```
For the above code the big and small will print the output as
```python
W
H
```
## User Defined Functions
Similarly like in other languages we have functions in python with arguments and return types since in python in order to define a function we use **def** keyword which is used to define a function for example
```python
def greet(lang) :
    if lang == 'es' :
        return 'Hola'
    elif lang == 'fr' :
       return 'Bonjour'
    else :
        return 'Hello'
print(greet('en'),'Glenn')
print(greet('es'),'Sally')
print(greet('fr'),'Michael')
```
Output will be
```
Hello Glenn
Hola Sally
Bonjour Micael
```
