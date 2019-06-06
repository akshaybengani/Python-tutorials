
# This is my first python program How to print
#You can use both brackets and non brackets
print('Akshay');	# This is the new version
print 'Bengani';	# This is the old version
print('Akshay Bengani');

#Datatypes 
type(2);	#int
type(2.2);	#Float
type('c');	#String no character is there

#Variables
number=2;		#number variable there is no declaration required	
print(number);	#print the number variable

floatvalue=2.54456;		#Float value or double value whatever you say
print(floatvalue);		#print the float value

charactervalue='akshay bengani';	# Takes string and characters both 
print(charactervalue);		#no more array

#We can declare multiple variables and assign a single value to all of them
a=b=c=1.43;		
print(a);
print(b);
print(c);

#we can create multiple variables and assign a specific value at the end of the declaration
one,two,three=1,22.455,'Akshay';	
print(one);
print(two);
print(three);

#we can dynamically assign variables of any datatype to any other
ab=223;
ac='Akshay Bengani';
print(ab);
print(ac);
ab=ac;		#we can assign any value to any varaible without any transformation
print(ab);	#now ab is replaced with ac
print(ac);

# import keyword;	#this is to import keyword function				#This is a comment
# keyword.kwlist;	#this is to show all keywords of python 3

print('#This is a comment')


print(20.4+4.45)		#we can use different datatypes
#print('Akshay Bengani');
print(40*30*0.5)	#we can multiply multiple values 
print(2**5)		#This is used to give power
print(2^5)		#This is an binary operator

print(23.0/5)  #This is to divide and in which format you entered the value u get the output
print(23//5)		# This will return only integer value even if u give a floating point no
print(25.0%4)		#this will give the moded remainder of the value

a = 2+5
b= 3.3*3
c = 10.0/25

print(c)

# Order Operator Precendance
'''
()		This is bracket
**		This is Power
*		This is multiply
/		This is Divide
%		This is Modulus
+		This is Addition
-		This is Subtraction
'''

# There are bitwise operators also such as << and >> these are same as in c

#Strings

string= 'I am a string' # We can assign a string directly
string1= "I am a string"	#We can assign using double quotes also
print(len(string)) # We can  calculate the length of the string by using len() function

print(string[-1]) # This will result the last 1st character what size it may be
print(string[5:11]) # This will print the string characters from 5 to 11 only

print(string[:5]) 	#This will return the characters till 5
print(string[10:])	#This will return last charcters of 

print(string)

string2 =  "con" + "catenation" #This will concate two strings and store them in a varible
print(string2)

string2 = 2 * ("con" + "catenation") # This will multiple the containing string two times
print(string2) # named as repeatation
con= 'con'
cat = 'catenation'
print(con+cat+'Akshay bengani')

word = 'ford'
word = 'L' + word[1:]
print(word) # Lord will be the output

print('today I had {0} cups of {1}'.format(3,'coffee')) 
# This is to insert values like c 
print("prices: ({x},{y},{z})".format(x=1.5,y=5.1,z=54.4))
# we can also use variable arguments in the print function via format function
print("The {vehicle} had {0} crashes in {1} months".format(5,6, vehicle='car'))
# This is the 0 index will be at first position and to use a variable index we use the variable argument
print('{:<20}'.format('text'))
print('{:>20}'.format('text'))

#"'I'm a string in python" #  This is how we can put the entirex
#'I\'m a string in python'
print(r'c:\number\nan')
print("""\Hello:
					User Defined Look
					Python output
	""")


#------------------------------------------------------------
























