# coding=utf-8


def bfind(li, target):
    vv = target - 1
    left = 0
    right = len(li) - 1
    mid = (left + right) // 2
    while left < right - 2:
        mid = (left + right) // 2
        if li[mid] < vv:
            left = mid + 1
        elif li[mid] > vv:
            right = mid - 1
        else:
            break

    while mid < len(li) - 1 and li[mid] < target:
        mid += 1
    return mid

def bsert(ll, tar):
    index = bfind(ll, tar)
    ll.insert(index, tar)
    return ll

def shop():
    fh = open('./144043063958496.txt', 'r')
    store = {}
    li = []
    cnt = 0
    len = 0
    for rawline in fh.readlines():
        len += 1
        if len % 1000 == 0:
            print(len)
        line = rawline.strip()
        arr = line.split()
        if arr[0] == 'up':
            num = int(arr[1])
            money = int(arr[2])
            if money in store:
                store[money] += num
            else:
                store[money] = num
                bsert(li, money)
            continue
        if arr[0] == 'down':
            num = int(arr[1])
            money = int(arr[2])
            if money in store:
                store[money] -= num
                if store[money] == 0:
                    del store[money]
                    li.remove(money)
            continue
        if arr[0] == 'query':
            n = 0
            _min = bfind(li, min(int(arr[1]), int(arr[2])))
            _max = bfind(li, max(int(arr[1]), int(arr[2])))

            for i in range(_min, _max):
                value = li[i]
                if _min > value:
                    continue
                elif _max < value:
                    break
                else:
                    n += store[value]
            cnt += n
            continue

    print(len, cnt)

    fh.close()

shop()
