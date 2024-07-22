#Bitwise operators in python are &,|,^,~,<<,>>
#let's see all these operators with two variables
x=3#bitwise 011
y=2#bitwise 010
print("Bitwise AND= ",x&y)
print("Bitwise OR = ",x|y)
print("Bitwise XOR = ",x^y)
print("Bitwise NOT = ",~x)#0's become 1's
print("Bitwise zero fill LEFT shift by 2 bits= ",x<<2)
print("Bitwise Signed RIGHT shift by 2 bits",x>>2)