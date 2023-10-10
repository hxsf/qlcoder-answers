# coding=utf-8
import os

max_size = 0
filenames = []

for item in os.walk('./root'):
    for files in item[2]:
        filename = os.path.join(item[0], files)
        size = os.path.getsize(filename)
        if size > max_size:
            filenames = [filename]
            max_size = size
        elif size == max_size:
            filenames.append(filename)

print(max_size)
print(filenames)
