"""
Let´s translate a person to a dictionary

"""

person_dict = {"name": "Eric", "age": 26, "job": "programmer"}

# The way that I reccomend
# print(person_dict.get("another_key"))

# print("The Keys", person_dict.keys())
# print("The Values", person_dict.values())

# Remove a key
person_dict.pop("job")
print(person_dict)
