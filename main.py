# countries = (
#     ' United Kingdom',
#     'Ghana', 'Nigeria',
#     'Australia',
#     'New Zealand');
# print(type(countries));

# Converting a number to a string.
# number = 55;
# number1 = str(number);
# print(20%6);
# print('number is ' + number1);

# Let's print the absolute value of a number
# abs is a number function used to get the absolute value of a number

# print(abs(-5)); 

# Another number function is max which is used to check the maximum number
# and it is not only focused on 2 numbers but even on a list of numbers,
# same thing happens for the mininmun number and rouding up of nunbers
# Another one is used to convert a given number to a binary number

# print(max(3,9,8,7));
# print(min(3,6,7,40));
# print(bin(3));

# Observe that these are build in functions used in python but there 
# are countless functions in python which are not easily gotten onless you import them.

# A good example is the math function, see the exmple below.

# from math import*
# print(int(sqrt(100)));

# name = input ('Enter Your Name: ')
# age  = (input ('Enter Your Age: '))

# print('Your Name is: ' + name + ' and you are ', age)

# Let's buid a simple word replacement program

class ComplexNumbers:
   def __init__(self, x = 0, y = 0):
       """

       :type x: object
       """
       self.real = x
       self.imagined = y
def getNumbers(self):
       print ("Complex numbers are: {0}+{1}j".format(self.real,
self.imagined))

Object1 = ComplexNumbers(2, 3) #Creates a new ComplexNumbers object
Object1.getNumbers() #Calls getNumbers() function
Object2 = ComplexNumbers(10) #Creates another ComplexNumbers object
Object2.attr = 20 #Creates a new attribute 'attr'

print ((Object2.real, Object2.imagined, Object2.attr))
del ComplexNumbers.getNumbers
Object1.getNumbers()































