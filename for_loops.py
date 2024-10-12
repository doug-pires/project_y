"""
for loops
while

"""

# Base index is 0

# for anything in range(10):
#     print(anything)

array_of_integers = [1, 2, 3, 4, 5]

# for integer in array_of_integers:
#     integer += 1
#     print(integer)

x = 0
while x < 10:
    x += 1
    array_of_integers.append(x)

array_of_integers.sort()
print(array_of_integers)
array_of_integers.sort(reverse=True)
print(array_of_integers)
