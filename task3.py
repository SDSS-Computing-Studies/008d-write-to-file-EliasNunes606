#!python3

'''
Ask the user to enter in a list of 5 words.
Convert the word to a string literal JSON object
Write the contents to a file called 'task3.txt'

Example:
Enter a word: frog
Enter a word: french
Enter a word: puppy
Enter a word: escalate
Enter a word: ice

task3.txt contents:
["frog","french","puppy","escalate","ice"]

'''
import json

file = open("task3.txt", "w")
print("Enter 5 words you want in a list")
first = input("Enter your first word")
second = input("Enter your second word")
third = input("Enter your third word")
fourth = input("Enter your fourth word")
fifth = input("Enter your fifth word")
list [first, second, third, fourth, fifth]
x = json.dumps(list)
file.write(x)