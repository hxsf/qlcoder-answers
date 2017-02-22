# coding=utf-8

fh = open('./src/145743685778441.txt', 'r')

types = {}
vars = {}

for rawline in fh.readlines():
    line = rawline.strip()
    arr = line.split()
    if arr[0] == 'type' and arr[1] not in types:
        types[arr[1]] = arr[1]
        continue
    if arr[0] not in vars and arr[1] == ':=':
        if (arr[2] == 'new'):
            if arr[3] in types:
                vars[arr[0]] = types[arr[3]]
                continue
        else:
            if arr[2] in vars:
                vars[arr[0]] = vars[arr[2]]

fh.close()

for key in sorted(vars):
    print(key + '-' + vars[key], end = '-')

# print(vars.items(), len(vars))
