# Read string
text = input("Enter a string: ")

# Calculate length without len()
count = 0
for ch in text:
    count = count + 1

print("Length of string:", count)

# Check palindrome
rev = ""
for ch in text:
    rev = ch + rev

if text == rev:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")