#! /usr/bin/python3

filename = 'text_files/pi_30_digits.txt'

with open(filename) as file_object:
    contents = file_object.read()
    print(contents.rstrip())

print('===================')

with open(filename) as file_object2:
    for line in file_object2:
        print(line.strip())

print('===================')

with open(filename) as file_object3:
    lines = file_object3.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)

print('======================')
print('======================')

"""打印大量文本的文件内容示例"""

bigfilename = 'pi_million_digits.txt'

with open(bigfilename) as big_file_object:
    lines = big_file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string[:52] + "...")
print(len(pi_string))