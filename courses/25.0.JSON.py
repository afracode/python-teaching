import json

# [1] Parse JSON - Convert from JSON to Python

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])  # // 30

# [2] Convert from Python to JSON

# a Python object (dict):
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)  # // "{ \"name\":\"John\", \"age\":30, \"city\":\"New York\"}"

# [3] JSON types

# Python	JSON
# dict		Object
# list		Array
# tuple		Array
# str		String
# int		Number
# float		Number
# True		true
# False		false
# None		null


# [4] Format the Result

x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

print(json.dumps(x, indent=4))

print(json.dumps(x, indent=4, separators=(". ", " = ")))

# [5] Order the Result

# sort the result alphabetically by keys:
print(json.dumps(x, indent=4, sort_keys=True))
