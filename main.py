# What I learned Today: Day 02

#print(len(123456))

#It throws the traceback error:
'''Traceback (most recent call last):
  File "main.py", line 1, in <module>
    print(len(123456))
TypeError: object of type 'int' has no len()'''

#Because we are trying to know the int's (integer) length & len function isn't trained to do so.

#Len function can tell you string's length. And now, question comes what is string & int? To under it better. Data Types comes into the picture:

#1. String
#2. Integer
#3. Float
#4. Boolean

''' Subscript: The method of pulling out the particular charcter in string is called subscript.
print("helloworld"[0])
This will print out the H since H is the very first element placed at index 0.
'''
print("helloworld"[-1]) #prints the last character. Initial index starts from zero & last index starts from -1

print("123""345") #concatenates two strings

#To do the mathematical calculations. Declare the integer data type which is int

#2.Integer: All no.s no mattter are positive or negative or whole no.

print(1234+1234)
print(123_456_758) #computer visulaises it as large no. & prints it by removing underscore

#3.Float: Decimal Number. Called Floating point no. 314.516

#4. Boolean: Most used. Booleans are either True or False, they don't have quotation marks around them, otherwise it would turn them into a String. Written as:
#True
#False


print(type(len(input("What is your name\n"))))
#output:What is your namekawal
#<class 'int'> because we have printed out the length of the string

#--> Type check allows us to know the type of our number

# Type Conversion: Using it we can implicitly or explicitly changes the data type.
a=100
print(a)

print(type(a)) 
#type of the variable is integer
s=str(a)
#type casted the int vaiable to string
print(s)
print(type(s))
