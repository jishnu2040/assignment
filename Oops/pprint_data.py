from pprint import pprint

data = {'name': 'Alice', 'age': 30, 'hobbies': ['reading', 'hiking'], 
        'education': {'degree': 'PhD', 'field': 'Computer Science', 'year': 2015}}

print(data)
pprint(data)



output:

# print
{'name': 'Alice', 'age': 30, 'hobbies': ['reading', 'hiking'], 'education': {'degree': 'PhD', 'field': 'Computer Science', 'year': 2015}}


# pprint
{'age': 30,
 'education': {'degree': 'PhD', 'field': 'Computer Science', 'year': 2015},
 'hobbies': ['reading', 'hiking'],
 'name': 'Alice'}

