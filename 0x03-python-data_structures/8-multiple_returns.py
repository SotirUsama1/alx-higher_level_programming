#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)
    if sentence:
        firstChar = sentence[0]
    else:
        firstChar = "None"
    return length, firstChar
