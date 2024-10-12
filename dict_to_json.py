"""
My script need to get input from the user and insert them into a dictionary.
After we need to convert the dictionary into a JSON object.
The save it into a file

Input:
- Name
- Age
- Job

"""

import json

name = input("Enter your name: ")
age = input("Enter your age: ")
job = input("Enter your job: ")

person_dict = {"name": name, "age": int(age), "job": job}


person_json = json.dumps(person_dict)

with open("data/person.json", "w+") as json_file:
    json_file.write(person_json)
