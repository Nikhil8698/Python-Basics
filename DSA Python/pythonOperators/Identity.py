#Identity operators are is,is not
#let's see all these operators with two variables
x=['a','b']
y=['a','b']
z=x
#Prints True if x is equal to y or both x and y are equal
print(x is y)#Note:x and y have same values but they are not same object
print(x is z)#Note:x and z are the same objects
# Prints True if x is not equal to y or both x and y are not equal
print(x is not y)

