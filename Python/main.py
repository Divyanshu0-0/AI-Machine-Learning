# This is a sample Python script.
from tkinter import Variable

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


                    #1. Installation

                    #2. Comments and Variable

# This line below is used for Printing
# print("Hello NYC")

# Variable
#
# anything = 12312
# print(anything)
#
# any_thing = 123123123
# print(any_thing)


# ( anything can become a variable )
#           But, There are some rules

# camelCase -> myVariableName
# hellBro = 20

# PascalCase -> MyVariableName
# HellBro = 40

# snake_case -> my_variable_name    # Python prefers this
# hell_bro = 20

# print (hellBro + hell_bro + HellBro )


#      3. DATATYPES ------------------------------------------

# DATATYPES ( Numbers ) ++++++++++++++++++++++
a = -324   # int
b = 34     # int
c = 24     # int
d = 876.24 # float

hell = 75598   # int
Hell = 752/876 # float
d = 876  + 876j # complex

print(type(hell))
print(type(Hell))
print(type(d))


# DATATYPES ( strings ) +++++++++++++++++++++++++

string = "hell bro hdhdhkhdoiwhd 912739 h12h9"
print(type(string))
print(string)

# if you want print Double/Single cots( " , ' ) then:
String = "hell bro 'What the luck is this '"
print(type(String))
print(String)

stRing = 'hell bro "What the luck is this" '
print(type(stRing))
print(stRing)

# DATATYPES ( Boolean ) +++++++++++++++++++++++++++

a = True
b = False

print(type(a))
print(type(b))

# DATATYPES ( NoneType ) NoneType :- Representing Nothing +++++

a = None
print(type(a))
print(a)

# Strings & Type Conversion

# How String work Internally :- Each character in a string is stored with its own UniCode number. That way string use more memory than integers.

print("Strings & Type Conversion")
a = "A"
print(ord(a))    # ->  65  ( Unicode of A )

print(ord('a'))  # ->  97  ( Unicode of a )
print(chr(86))   # ->  V  ( Character from Unicode )