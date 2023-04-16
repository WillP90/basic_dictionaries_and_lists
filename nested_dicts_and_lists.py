# #1 Update Values In Dictionary and lists

# Provided code
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#  My code
# Change the value 10 in x to 15
x[1][0] = 15 # changing the fisrt index of the second list
print(x)
# Change the last_name of the first student from 'Jorden' to 'Bryant'
students[0]['last_name'] = 'Bryant'
print(students[0])
# in the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = 'Andres'
print(sports_directory['soccer'])
# change the value 20 in z to 30
z[0]['y'] = 30
print(z)

# #2 Iterate through a list of dictionaries

# My Code
def iterateDictionary(li):
    for i in li:
        for key, val in i.items():
            print(f"{key}' - '{val},")

# Provided Code
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students)
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

# #3 Get values from a List of Dictionaries

# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary.

# My Code
list_of_names = [
    {'first_name' : 'James', 'last_name' : 'Foreman'},
    {'first_name' : 'Baron', 'last_name' : 'Smith'},
    {'first_name' : 'Isagi', 'last_name' : 'Hotoro'},
    {'first_name' : 'Tony', 'last_name' : 'Breadman'},
]
def iterateDictionary2(key_name, lists):
    for i in range(len(lists)):
        for key, val in lists[i].items():
            if key == key_name:
                print(val)

iterateDictionary2('first_name', list_of_names)
iterateDictionary2('last_name', list_of_names)

# #4 Iterate Through a Dictionary with List Values
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list.

# My Code with help of instruction video
dict2 = {
    'locations' : ['San Diego', 'New York', 'Seattle', 'San Jose', 'Chicago', 'Pheonix'],
    'instructors' : ['Will', 'John', 'Francise', 'Danny', 'Leroy', 'Janette', 'Aaron']
}
def printInfo(diction):
    for key, val in diction.items():
        print(f"{len(val)} {key.upper()}")
        for i in range(0, len(val)):
            print(val[i])

printInfo(dict2)