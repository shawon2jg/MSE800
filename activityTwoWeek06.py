# region Part One
data = ['a5', 'a2', 'b1', 'b3', 'c2']

# Lambda Key: For multi-level sorting (letter first then number)
# sorted_data = sorted(data, key=lambda x: (x[0], int(x[1:])))
# print(sorted_data)
# endregion

# region Part Two
# sort the dictionary based on the ages using lambda
# students = [
#     {'name': "John", 'grade': "A", 'age': 20},
#     {'name': "Jane", 'grade': "B", 'age': 21},
#     {'name': "Joss", 'grade': "A+", 'age': 19},
#     {'name': "Jack", 'grade': "A-", 'age': 16},
#     {'name': "Dave", 'grade': "C", 'age': 25},
# ]

# Sort the list using lambda to access the 'age' key
# sorted_students = sorted(students, key=lambda x: x['age'], reverse=False)
# print(sorted_students)
# endregion

# region Part Three
students = [
    {'name': "John", 'grade': "A", 'age': 20},
    {'name': "Jane", 'grade': "B", 'age': 21},
    {'name': "Joss", 'grade': "A+", 'age': 19},
    {'name': "Jack", 'grade': "A-", 'age': 16},
    {'name': "Dave", 'grade': "C", 'age': 25},
]

sorted_students = sorted(students, key=lambda x: (x['grade'] != "A+", x['grade'], x['age']), reverse=False)
print(sorted_students)
# endregion

# region Part Four

# endregion