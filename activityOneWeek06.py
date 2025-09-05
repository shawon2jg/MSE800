from math import prod

# extract information with age greater than 25 from the following list of dictionaries
data = [{"name": "Alice", "age": 28}, {"name": "Bob", "age": 24}, {"name": "Charlie", "age": 30}]

result = [item for item in data if item["age"] > 25]
print(result)

# use list comprehension to flatten the matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flatten = [num for row in matrix for num in row]
print(flatten)

matrixTwo = [[0, 2, 3], [4, -5, 16], [17, 18, 39]]
# Summation of the Matrix
total_sum = sum(sum(row) for row in matrixTwo)
print(total_sum)

# Multiplication of the Matrix
product = prod(element for row in matrixTwo for element in row)
print(product)