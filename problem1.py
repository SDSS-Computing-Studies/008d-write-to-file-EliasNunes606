import json


file = open("problem1.txt",'r')


read = file.read()
load=json.loads(read)
print(load)