#!/usr/bin/python3
print("{:02d}".format(1), end="")
for i in range(2, 100):
    digit1 = i // 10
    digit2 = i % 10
    if digit1 >= digit2:
        continue
    else:
        print(", {:02d}".format(i), end='')
print("")
