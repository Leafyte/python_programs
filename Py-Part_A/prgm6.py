f1 = open("input.txt", "r")
f2 = open("output.txt", "w")

line_no = 1

for line in f1:
    if line_no % 2 != 0:
        f2.write(line)
    line_no = line_no + 1

f1.close()
f2.close()

print("Odd lines copied successfully")