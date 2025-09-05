from math import prod

# region Part One
# extract information with age greater than 25 from the following list of dictionaries
data = [{"name": "Alice", "age": 28}, {"name": "Bob", "age": 24}, {"name": "Charlie", "age": 30}]

result = [item for item in data if item["age"] > 25]
# print(result)

# use list comprehension to flatten the matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flatten = [num for row in matrix for num in row]
# print(flatten)

matrixTwo = [[0, 2, 3], [4, -5, 16], [17, 18, 39]]
# Summation of the Matrix
total_sum = sum(sum(row) for row in matrixTwo)
# print(total_sum)

# Multiplication of the Matrix
product = prod(element for row in matrixTwo for element in row)
# print(product)
#endregion

# region Part two
# use enumerate() for looping to add 5 extra point to each grade in the list, the 5th one add 10
grades = [88, 92, 78, 65, 50, 94]

for index, grade in enumerate(grades):
    if index == 4:
        grades[index] = grade + 10
    else:
        grades[index] = grade + 5

print(grades)

# filter out elements depend on their index:
# use list comprehension and enumerate() to get elements with even index
data = [100, 200, 300, 400, 500]

even_index_elements = [value for index, value in enumerate(data, start=0) if index % 2 == 0]
print(even_index_elements)

# create a dictionary from lists using zip()
keys = ['name', 'age', 'grade']
values = ['Alice', 25, 'A']

result = dict(zip(keys, values))
print(result)
#endregion