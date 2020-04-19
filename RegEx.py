import re


"""
findall
Returns a list containing all matches

search
Returns a Match object if there is a match anywhere in the string

split
Returns a list where the string has been split at each match

sub
Replaces one or many matches with a string 

"""


#Check if the string starts with "The" and ends with "Spain":
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if (x):
  print("YES! We have a match!")
else:
  print("No match")

#Find all lower case characters alphabetically between "a" and "m":
x = re.findall("[a-m]", txt)
print(x)

txt = "That will be 59 dollars"
#Find all digit characters:
x = re.findall("\d", txt)
print(x)

txt = "hello world"
#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":
x = re.findall("he..o", txt)
print(x)

#Check if the string starts with 'hello':
x = re.findall("^hello", txt)
print(x)
if (x):
  print("Yes, the string starts with 'hello'")
else:
  print("No match")

#Check if the string ends with 'world':
x = re.findall("world$", txt)
print(x)
if (x):
  print("Yes, the string ends with 'world'")
else:
  print("No match")

txt = "The rain in Spain falls mainly in the plain!"
#Check if the string contains "ai" followed by 0 or more "x" characters:
x = re.findall("aix*", txt)
print(x)
if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

#Check if the string contains "ai" followed by 1 or more "x" characters:
x = re.findall("aix+", txt)
print(x)
if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

#Check if the string contains "a" followed by exactly two "l" characters:
x = re.findall("al{2}", txt)
print(x)
if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

#Check if the string contains either "falls" or "stays":
x = re.findall("falls|stays", txt)
print(x)
if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")


"""Special function""" 
txt = "The rain in Spain"
#Check if the string starts with "The":
x = re.findall("\AThe", txt)
print(x)

#Check if "ain" is present at the beginning of a WORD:
x = re.findall(r"\bain", txt)
print(x)

#Check if "ain" is present at the end of a WORD:
x = re.findall(r"ain\b", txt)
print(x)

#Check if "ain" is present, but NOT at the beginning of a word:
x = re.findall(r"\Bain", txt)
print(x)

#Check if "ain" is present, but NOT at the end of a word:
x = re.findall(r"ain\B", txt)
print(x)

#Check if the string contains any digits (numbers from 0-9):
x = re.findall("\d", txt)
print(x)

#Return a match at every no-digit character:
x = re.findall("\D", txt)
print(x)

#Return a match at every white-space character:
x = re.findall("\s", txt)
print(x)

#Return a match at every NON white-space character:
x = re.findall("\S", txt)
print(x)

#Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):
x = re.findall("\w", txt)
print(x)

#Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.):
x = re.findall("\W", txt)
print(x)

#Check if the string ends with "Spain":
x = re.findall("Spain\Z", txt)
print(x)


"""Sets"""
#Check if the string has any a, r, or n characters:
x = re.findall("[arn]", txt)
print(x)

#Check if the string has any characters between a and n:
x = re.findall("[a-n]", txt)
print(x)

#Check if the string has other characters than a, r, or n:
x = re.findall("[^arn]", txt)
print(x)

#Check if the string has any 0, 1, 2, or 3 digits:
x = re.findall("[0123]", txt)
print(x)

#Check if the string has any digits:
x = re.findall("[0-9]", txt)
print(x)

#Check if the string has any two-digit numbers, from 00 to 59:
x = re.findall("[0-5][0-9]", txt)
print(x)

#Check if the string has any characters from a to z lower case, and A to Z upper case:
x = re.findall("[a-zA-Z]", txt)
print(x)

#Check if the string has any + characters:
x = re.findall("[+]", txt)
print(x)

#Print a list of all matches:
x = re.findall("ai", txt)
print(x)

#Return an empty list if no match was found:
x = re.findall("Portugal", txt)
print(x)
x = re.search("Portugal", txt)
print(x)
#output : None

#Search for the first white-space character in the string:
x = re.search("\s", txt)
print(x)
print("The first white-space character is located in position:", x.start())

#Split the string at every white-space character:
x = re.split("\s", txt)
print(x)

#Split the string at the first white-space character:
x = re.split("\s", txt, 1)

#Replace all white-space characters with the digit "9":
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

#Replace the first two occurrences of a white-space character with the digit 9:
txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)

#The search() function returns a Match object:
x = re.search("ai", txt)
print(x)

"""
.span() returns a tuple containing the start-, and end positions of the match.
.string returns the string passed into the function
.group() returns the part of the string where there was a match
"""

#Search for an upper case "S" character in the beginning of a word, and print its position:
x = re.search(r"\bS\w+", txt)
print(x.span())

#The string property returns the search string:
x = re.search(r"\bS\w+", txt)
print(x.string)

#Search for an upper case "S" character in the beginning of a word, and print the word:
x = re.search(r"\bS\w+", txt)
print(x.group())