# Python Basics
Python is a programming language who do not use semicolon at the end of the statement.

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
# Iteration Statements
Similar like other languages python also have **while** and **for** loop but with different syntax.

## While Loop
While is a loop which actually works like a repeatativly if condition, therefore the while loop continoously checks and works till the if condition become false

```python
n=5
while n>0:
    print(n)
    n = n - 1
print("Blastoff")
print(n)
```

There are two types of loops **definate** and **Infinite**
Definate loops which stops the loop after a set of steps and infinite loops do not stops and runs coontinuously

## Break Statement

The break statement ends the current loop and jumps to the statement immediately following the loop. It is like a loop test that can happpen anywhere in the body of the loop
```python
while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')
```


## Continue
The continue statement ends the current iteration and jumps to the top ooof the loop and starts the next iteration.
```python
while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')
```
The output will be
```
> hello there
hello there
> #don't print this
> print this!
> done
Done!
```

## For Loop
For loop also known as Definite Loops have explicit **iteration variables** that change each time through a looop. These **iteration variables** move through the sequence or set.

### Looking at in
The Iteration variable iterates through the sequence (ordered set).<br>
The block (body) of code is executed once for each value in the sequence.<br>
The iteratioon variables moves through all of the values in the sequence.
```python
for i in [5,4,3,2,1]:
    print(i)
```

## Strings
A string is a sequence of characters A string literal uses quotes '' "" <br>
For strings, + means "concatenate"
when a string contains numbers, it is still a string. we can convert numbers in a string into a number using ```int()```<br>
```python
apple = input("Enter qty ")
# This will give error
x = apple - 10
# We need to convert String into int
x = int(apple) - 10
```
### Looking inside Strings
* We can get at any single character in a string using an index specified in square brackets
* The index value must be an integer and start at zero
* The index value can be an expression that is computed
```python
fruit = "banana"
letter = fruit[1]
print(letter)
# a
x = 3
w = fruit[x - 1]
print(w)
# n
```
###  A Character too far
* You will get a python error if you attempt to index beyond the end of a sting
* So be careful when constructing index values and slices
```python
zot = "abc"
print(zot[5])
# error index out of range
```
### Length Function String
the built in function ```len()``` gives us the length of a string
```python
fruit = "banana"
print(len(fruit))
# 6
```
### Lower and Upper String Functions
* Python has a number of string ```fucntions``` which are in the ```String Liberary```
* These ```functions``` are already ```built into``` every string we invoke them by appending the fuction to the string variable
* These ```functions``` do not modify the orignal String, insteed they return a new string that has been altered
```python
name = "Akshay Bengani"
nameInSmall = name.lower()
# akshay bengani
nameInCapital = name.upper()
# AKSHAY BENGANI
print(name)
# Akshay Bengani
```
For more string functions [visit](https://docs.python.org/3/library/stdtypes.html#sting-methods)

### String Slicing
* We can also look at any continous section of a string using a color operator
* The second number is one beyond the end of the slice = "up to but not including"
* If the second number is beyond the end of the string, it stops at the end
```python
s = "Monty Python"
# M o n t y   P y t h o  n
# 0 1 2 3 4 5 6 7 8 9 10 11

print(s[0:4])
# Mont
print(s[6:7])
# P
print(s[6:20])
# Python
print(s[:2])
# Mo
print(s[8:])
# thon
print(:)
# Monty Python
```
### Parsing and Extracting
When we need partitcular part of the string then we need to find its starting position and ending position and then we can slice the string text
```python
data = "From akshay.16BCAN018@jecrcu.edu.in Wed Jan 23 06:11:16 2019"
startpos = data.find('@')
print(atpos)
#21
endpos = data.find(" ",atpos)
print(endpos)
#34
host = data[startpos + 1 : endpos]
print(host)
# jecrcu.edu.in
```

### Using ```in``` as a logical Operator
* The ```in``` keyword can also be used to check to see if one string is "in" another string
* The ```in``` expression is a logical expression taht returns ```True``` or ```False``` and can be used in an ```if``` statement
```python
fruit = "banana"
'n' in fruit
# True
'm' in fruit
# False
"nan" in fruit
# True
if 'a' in fruit:
    print("Found it")
# Found it
```
### The Newline Character
* We use a special character called the newline to indicate when a line ends.
* We represent it as ```\n``` in strings.
* String value "X```\n```Y" its length is 3 characters not 4

## Files

Right now we will be only dealing  with the text files no pdf no word document no network or database files only text files.
* Before we can read the contents of the file, we must tell python which file we are going to work with and what we  will be doing with the file.
* This is done with the ```open()``` function.
* ```open(filename,mode)``` returns a file handle -a variable used to perform operations on the file.
* Similar to File-> open in a Word Processor
* Mode is optional and should be ```r``` if we are planning to read the file and ```w``` if we are going to write to the file.
* Since printing the file handler will not print its text it will print file detail.
```python
fhand  = open('members.txt')
print(fhand)
# <_io.TextIOWrapper name='members.txt' mode='r' encoding='UTF-8'>
```
### File Handle as a Sequence
* A ```file handle``` open for read can bbe treated as a sequence of strings where each line in the file is a string in the sequence
* We can use the for statement to iterate through a sequence
* Remember-a sequence is an ordered set
```python
myfile = open('members.txt')
for name in myfile:
    print(name)
```
### Counting Lines in a File
* Open a ```file``` read-only
* Use a ```for``` loop to read each line
* ```Count``` the lines and print  out the number of lines
```python
myfile = open('filename.txt')
count = 0

for lines in myfile:
    count = count + 1

print("Line Count:",count)
```
### Reading the whole file
* We can read the whole file including (newlines and all) into a single string
```python
myfile = open('members.txt')
data = myfile.read()
print(len(data))
# 686
print(data)
# So now we have a string which contain whole file
```


 