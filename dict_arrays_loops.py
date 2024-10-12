"""

Write a script to get three lists and insert them into a dictionary.

Input:
- List Name = ["Eric", "John", "Michael"]
- List Age = [26, 30, 24]
- List Job = ["programmer", "designer", "manager"]

Intermediate Output:

{"name":"Eric", "age":26, "job":"programmer"}

Final Output:
[
{"name":"Eric", "age":26, "job":"programmer"},
{"name":"John", "age":30, "job":"designer"},
{"name":"Michael", "age":24, "job":"manager"}
]

HMW improve this code? Refactor it!

"""

list_names = ["Eric", "John", "Michael"]
list_ages = [26, 30, 24]
list_jobs = ["programmer", "designer", "manager"]

main_list = []
for each_element in range(len(list_names)):
    person_dict = {
        "name": list_names[each_element],
        "age": list_ages[each_element],
        "job": list_jobs[each_element],
    }
    main_list.append(person_dict)

print(main_list[0])
