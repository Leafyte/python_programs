# A3. Write a NumPy program to create a structured array
# from given student name, height, class and their data types.
# Finally sort the array on height.

import numpy as np

# number of students
n = int(input("Enter number of students: "))

# create structured array
students = np.empty(
    n,
    dtype=[('name', 'U20'), ('height', float), ('class', int)]
)

# input data
for i in range(n):
    name = input("Enter name: ")
    height = float(input("Enter height: "))
    cls = int(input("Enter class: "))

    students[i] = (name, height, cls)

# display original array
print("\nOriginal Array:")
print(students)

# sort by height
sorted_students = np.sort(students, order='height')

# display sorted array
print("\nSorted Array:")
print(sorted_students)