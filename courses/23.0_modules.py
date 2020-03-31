# Built-in Modules
import platform

# Use a Module
from .modules import afracode_module as afra

# from .modules import *

afra.greeting("ali")

print(afra.person1["age"])

# Built-in Modules
x = platform.system()
print(x)

# Using the dir() Function
#  list all the function names (or variable names) in a module.

x = dir(platform)
print(x)

x = dir(afra)
print(x)
# // [
# '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__',
# '__package__', '__spec__', 'greeting', 'person1'
# ]
