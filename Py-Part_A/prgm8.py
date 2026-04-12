text = input("Enter a string: ")

count_dict = {}

for ch in text:
    if ch in count_dict:
        count_dict[ch] = count_dict[ch] + 1
    else:
        count_dict[ch] = 1

print("Character occurrences:")
for key in count_dict:
    print(key, ":", count_dict[key])