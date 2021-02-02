#### Basic Types ###

# Declaring Intergers
my_int = 3
# Typecast
my_int = int(5.0)

# Declaring Floats
# my_float = 2.75
# my_float = float(4)
# Declaring Strings
# my_string = 'hello'
# my_string = "hello"


# Practice
# my_int = 6
# my_float = 9.2
# my_string = "Teresa"


# Print Outputs
# print(my_int)
# print(my_float)
# print(my_string)


#### BASIC LIST OPERATIONS###
# Declar list
#my_list = [1, 2, 3]

# Accsess list
#print(my_list[2])
#my_list.append(4)
#my_list.append(5)
#print(my_list)
# iterate through List
#for element in my_list:
  #print(element)





#--------------------#

#### Basic String Operations######
#my_string = "Hello, World"

# print length
#    print(len(my_string))

# print Index
#   print(my_string.index("o"))


# count occurances
#print(my_string.count("we"))




# slice the string parsing this section
#     print(my_string[1:4])
# what index do we want to start on [1:]ie ell e starts at index 1, we want 1,2,3 so make sure to stop at the point you want is need to stop at 4 to get 1,2,3 

## Skip in the string  
#print(my_string[7:12:2])
#  [7:] is the index we start at in the string 
#  [:12] is the index where we want to stop
#  [7:12:2] The [:2] is how often we need to skip in the letters    

#     print(my_string[::-1]) 
## The [::-1] will reverse the string


# upper case
#print(my_string.upper())# calls the upper function


# lower case
 # print(my_string.lower())
 # calls the lower function


# starts with
#print(my_string.startswith("Help"))
# calls the starts with function

# ends with
#print(my_string.endswith("rld"))
# starts the ends with function


# split string
# print(my_string.split(", "))


#### Conditionals and Booleans  #####
## Boolean is either a true statement or a false statment
# Use Booleans  to control the flow and logic
# when something is True or False you can use 
# this to control the flow and logic of your python program
#  if something is True execute this block of code
#  if something is False execute this other block of code
#


#---------------------------------
#Use comparison Operator
# x = 10
# print(x == 10) # in python == to denote if something is actually that value

#-----------------------------
# Use and + or

# name = "Elon"
# age = 49
# if name == "Elon" or age == 49: # Control Flow here if statment Here
#   print("Yay! we found elon!") 

#-----------------------------------
# use in iteration

# years = [2015, 2017, 2018, 2019, 2020]
# year = 2019
# if year in years:
#   print("booyah!!") 

#-------------------------
# use elif

# first_statement = False
# second_statement = True

# if first_statement:
#   print("first")
# elif second_statement:
#   print("second_statement")
# else:
#   print(" none are true!!")    

#-----------------------------

# use == vs is
# 
# a = [1, 2, 3]
# b = [1, 2, 3]
# print(a == b)
#print(not(10==1))

#------------------------------

####LOOPS###

## For loop iterates over a given sequence(iterator expression)
## The RANGE Function takes in a value that is the exclusive parameter so that you'll print all the values from 0 up to 5 ie: 0, 1, 2, 3, 4, 5

# for x in range(5):
#   print(x)

## Lets say i want all the values between 1 and five but i do not want to include 0

# for x in range(1, 11):
#   print(x)

# do not do the intended target ie 1-10 include 11
# because the first value in range ie(1,) is inclusive
# while the 2nd value ie(, 11) is exclusive when we do a specific range over a set of values


### PRINT ODD NUMBERS 
# for x in range(1, 11, 2):
#   print(x)
 #---------------------------- 


#####WHILE LOOPS#######

# WHILE LOOP repeats as long as a boolean context evaluates to True 
## A while loop will keep going until the condition breaks
# then increment x by one 
# this loop goes five times and print each value then increment 
#x by 1. so as soon as x is five we go ahead and exit the while 
#loop
# x = 0
# while x < 5:
#   print(x)
#   x += 1
  

  
  
  #-----------WHILE LOOP------------------
  
  ##  BREAK: TERMINATES THE LOOP CONTAINING IT
  # in loops you can also use these things called break 
 ## EAMPLE 
  ## X = 0
  ## WHILE X < 5: WE USE BREAK IF WE DO NOT HAVE A CONDITIONAL 
  ##   PRINT(X)
  ##   X += 1
  # x = 0
  # while True:
  #   if x == 11:
  #     break
  #   print(x)
  #   x += 1



#------------WHILE LOOP OD NUMBERS------------------------

## ODD NUMBERS IN WHILE LOOP###
# x = 0
# while x < 10:
#   x += 1
#   if x % 2 == 0:
#     continue
    
#   print(x) 
  
#---------------------------


 ### LIST COMPREHENSION###

 ## LIST COMPREHENSIONS are a powerful tool to the following below 
 # you can do this with a for loop this will allow you to so this in a single line of code

 ## In this single line expression #
 # first you have the mapping expression
 # then the iteration expression
 # lastly the filter expression 
     
     # [map expression> for <name> in <sequence expression> if <filter expression>]  

#iterating

#Mapping

#Filtering#

 #Words
# sentence = "Every moment is a fresh beginning." # This is the sentence
#words = sentence.split()# We want to split the sentence
# word_lengths = [len(word) for word in words] # we want the length of every word in  the sentence we can also truncate to a list comprehension the for loop to one line 

# for word in words:
#     word_lengths.append(len(word))
#print(word_lengths) 


# NUMBERS
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#REFACTOR FOR LOOP INTO A LIST COMPREHENSION ONE LINE OF CODE
# even_numbers = [number for number in numbers if number % 2 == 0]
# print(even_numbers)



# for number in numbers:
#   if number % 2 == 0:
#     even_numbers.append(number)
#print(even_numbers)
#even_numberslist_comp = []    



#---------------------------------
##########USER- DEFINED FUNCTIONS#############
# WHY ARE FUNCTIONS GOOD
# USABLE
# READABLE
# AVOIDS REPEATING 
# NOT REPEATING IS VERY IMPORTANT IN A LARGE PYTHON program
# IN ORDER TO CREATE YOUR OWN FUNCTION YOU HAVE TO USE THIS TERMINOLOGY
  # FIRST YOU HAVE TO DEFINE THE FUNCTION BY USING //def//
  # SECOND YOU HAVE THE FUNCTION NAME
  # THIRD YOU HAVE TO PASS IN THE FUNCTION ARGUMENTS VIS PARENTHESES()
  
  #####CODE EXAMPLE ######
  # GREET FUNCTION
  # This is where we pass in variables 
# def greet(name, greeting):
#   print("Hello %s, %s" % (name, greeting))
# greet("Teresa", "nice to meet you")
# greet("Ronna", "Where did you come from?")  




  
  # DOUBLE FUNCTION RETURN STATEMENTS
# def double(x):
#   return x*2

# eight = double(4)
# print(eight)
# print(double(224545))  

#------------------------------------#


###USER-DEFINED-CLASSES###
# Classes are like templetes, every single object in python is like an instance of this template, we can create as many templates as possiable.

# In classes you can set variables 
#class MyFirstClass:
  # set the variable to equal to the word data
    #variable = "data"
# We can also define functions within classes. for every function we take i our self because we're taking ourselves as an instance of this class. Then we can pass any other parameters we need or want
    #def function(self, number):
        #print("I am in my function! %d" % number)

# in oreder to create an instance of this class we again need to create an object
#create a variable objec and set it equal to MyFirstClass.
#a_class = MyFirstClass()            
# This creates an instance of MyFirstClass. This makes a_class an object we can use a class dot variable to print out data
#print(a_class.variable)
# You can create as many of instance of this class as you want 
#a_class.function(2)


#b_class = MyFirstClass()
#b_class.function(5)

#####---------------------------###
##-------BASIC DICTIONAY OPERATIONS------####
## dICTIONARIES ARE ANOTHER WAY TO STORE data 
#  When using dictionary you have a key value pair
   # KEY: Any type of object(string, number, list, etc)
## This maps out one peice of data to another
## The KEY can be any type of object
## The VALUE can be any type of object
  ## One key diffrence between DICTIONARYS and LISTS is that 
  ## DICTIONARYS do not have any particular sort of order 

      #### CODE EXAMPLE ####

# DECLARING A DICTIONARY
## We have a phonebook and in a phone book we want to map a person's name to their phone number

## In oreder to declare a dictionary you set it equal to the empty curly brace {} 
# phonebook = {
#   "Ronna": 5035555555,
#   "Jugger": 5555555555,
#   "Shrek": 963214789

# }
# phonebook["Teresa"] = 5035419696
# To add a value to a dictionary we will call the name of the dictionary phone book( from above) we will do a bracket [] then we will place the KEY, 
# the KEY in this case is a name ["John"]
#  Set phone book  Ronna equal to  Ronnas  phone number that is the value 
   
   ## dict example one 
# phonebook["Ronna"] = 5035555555
# phonebook["Jugger"] = 555555555
# phonebook["Shrek"] = 963214789
#print(phonebook)

# ITERATING THROUGH A DICTIONARY
  ## Iterating through a dictionary it is like iterating through anything else you can use a FOR LookupError
# for name, number in phonebook.items():
#     print("Name: %s, Phone Number: %d" % (name, number))  
    


# REMOVING ITEMS FROM A DICTIONARY
#del phonebook["Teresa"]
# print(phonebook.pop("Shrek"))
# print(phonebook)



###########IMPORT MODUELS#############
# 
# import math
# print(math.factorial(5))

### If only wanting one of the 
# from math import pow

# print(pow(2,3))


## If wanted to import  all of the math functions
# from math import *

# print(factorial(6))
# print(pow(4, 9))

## if i wanted to get all the functions that go with math we can print the directory compile
# import math
# print(dir(math))

#### CODING EXERCISES###  
# def sort_list(lst):
#     return sorted(lst)
# a = [" Sarahmarie", " Jennie", "Fady", "Anthony"]

# b = sort_list(a)
# print(b)

def XO(txt):
    # numberOfOs = 0
    # numberOfXs = 0
    # for char in txt:
    #     if char == 'x' or char == 'X':
    #         numberOfXs += 1
    #     elif char == 'o' or char == 'O':
    #        numberOfOs  += 1
    # return numberOfOs == numberOfXs         
      
