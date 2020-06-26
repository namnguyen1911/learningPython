#Python does not have a character data type, a single character is simply a string with a length of 1
a = "Hello, World!"
print(a[1])
#Get the characters from position 2 to position 5 (not include 5)
print(a[2:5])
#Get the characters from position 5 (not include 5) to position 1, starting the count from the end of the string
print(a[-5:-2])
#Get the length of a string, use the len() function
print(len(a))
#strip() method removes any whitespace from the beginning or the end
b = " Hello, World! "
print(a.strip())
#lower() method returns the string in lower case
print(a.lower())
#upper() method returns the string in upper case
print(a.upper())
#replace() method replaces a string with another string
print(a.replace("H","J"))
#split() method splits the string into substrings if it finds instances of the separator
print(a.split(",")) #return ['Hello', ' World!']
#Check if a certain phrase or character is present in a string, we can use the keywords "in" or "not in"
txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x) #return True
y = "ain" not in txt
print(y) #return false
#We can use format() method to combine a string and a number
age = 36
txt = "My name is John, I am {}"
print(txt.format(age))
#The format() method takes unlimited number of arguments, and are placed into the respective placeholder
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
#You can use index numbers {0} to be sure the arguments are placed in the correct placeholders
myorder = "I want to pay {2} dollars for {0} pieces of items {1}."
print(myorder.format(quantity,itemno, price))
#You cannot use double quotes inside double quotes
# text = "We are the so-called "Vikikngs" from the north." error
#Use \" to insert double quotes inside double quotes
txt = "We are the so-called \"Vikings\" from the north"
"""
Othe escape characters used in Python:
\' Single quote
\\ Backslash
\n New line
\r Carriage return 
\t Tab
\b Backspace
\f Form feed
\ooo Octal value
\xhh Hex value
"""
