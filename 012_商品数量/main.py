# coding=utf-8

fh = open('./144043123647536.txt', 'r')
store = {}
cnt = 0
len = 0

for rawline in fh.readlines():
    len += 1
    line = rawline.strip()
    arr = line.split()
    if arr[0] == 'up':
        if arr[2] in store:
            store[arr[2]] += int(arr[1])
        else:
            store[arr[2]] = int(arr[1])
        continue
    if arr[0] == 'down':
        if arr[2] in store:
            store[arr[2]] -= int(arr[1])
            if store[arr[2]] == 0:
                del store[arr[2]]
            print(len, line)
        continue
    if arr[0] == 'query':
        li = list(store.keys())
        n = 0
        _min = min(int(arr[1]), int(arr[2]))
        _max = max(int(arr[1]), int(arr[2]))
        for value in li:
            if _min <= int(value) and int(value) <= _max:
                n += store[value]
        # print(len, line, n)
        cnt += n
        continue

# print(store)
print(len, cnt)

fh.close()
