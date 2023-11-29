#!/usr/bin/python3
def fizzbuzz():
    temp = ""
    for i in range(1, 100):
        if i % 3 == 0 and i % 5 == 0:
            temp += "FizzBuzz "
        elif i % 3 == 0:
            temp += "Fizz "
        elif i % 5 == 0:
            temp += "Buzz "
        else:
            temp += "{} ".format(i)
    temp += "Buzz "
    print(temp, end="")
