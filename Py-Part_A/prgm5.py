phone_book = {}

n = int(input("Enter number of people: "))

for i in range(n):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    phone_book[name] = phone

person = input("Enter the name to search: ")

if person in phone_book:
    print("Phone number:", phone_book[person])
else:
    print("Person not found")