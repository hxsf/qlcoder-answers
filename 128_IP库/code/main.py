# coding=utf-8
f = open('./ip.data', 'rb')
d = f.read()
print list(d[0: 20])
print len(d)
f.close()
a = {}
for i in range(0, len(d), 5):
    t = ord(d[i + 2]) * 256 + ord(d[i + 3])
    if a.has_key(t):
        a[t] += 256
    else:
        a[t] = 256

print str(a[242]) + "," + str(a[29]) + "," + str(a[133]) + "," + str(a[75])
