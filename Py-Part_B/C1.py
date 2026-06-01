# Develop a Python program to store and display Employee details
# such as EID, Name, Place and Department.
# The EID must be auto-generated for each employee.

employees = []
eid = 1

n = int(input("Enter number of employees: "))

for i in range(n):
    print("\nEnter details of Employee", i + 1)

    name = input("Enter Name: ")
    place = input("Enter Place: ")
    dept = input("Enter Department: ")

    emp = {
        "EID": eid,
        "Name": name,
        "Place": place,
        "Department": dept
    }

    employees.append(emp)
    eid += 1

print("\nEmployee Details:")

for emp in employees:
    print(emp)
