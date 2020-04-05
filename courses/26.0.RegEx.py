import re

# findall	Returns a list containing all matches
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)  # // ['ai', 'ai']

# search	Returns a Match object if there is a match anywhere in the string
txt = "The rain in Spain"
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())

# split	Returns a list where the string has been split at each match
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)  # // ['The', 'rain', 'in', 'Spain']

# sub	Replaces one or many matches with a string
txt = "The rain in Spain"
x = re.sub("\s", "_", txt)
print(x)  # // The-rain-in-Spain
