# coding=utf-8
import os

def build_dict():
    encode_dict = {}
    decode_dict = {}
    i = 0
    for ch in list("abcdefghijklmnopqrstuvwzyx0123456789().!~*'-_/:"):
        i += 1
        encode_dict[ch] = i
        decode_dict[i] = ch

    def encode(str):
        return [encode_dict[item] for item in list(str)]

    def decode(bytes):
        return ''.join([decode_dict[item] for item in bytes])


    return (encode, decode)

(encode, decode) = build_dict()

a = encode("http://baidu.com")
print (a, decode(a))
#
# if not os.path.exists('./1.dat'):
#     f = open("test_text","w")
#     f.seek(1024*1024*1-1)
#     f.write('\0')
#     f.close()
#
# df = open('./1.dat', 'wr')
#
# def read_file (start, count):
#     df.seek(start, 0)
#     return df.read(count)
#
# def write_file(bytes):
#     df.seek(start, 0)
#     df.write(bytes)
#
# mp = {}
# file_len = 0
# # user_code
#
# def get(key):
#     return mp.get(key, 0)
#
# def put(key):
#     key_len = len(key)
#     if (not mp.has_key(key)):
#         bytes = bytearray(s)
#         url_len = len(bytes)
#         write_file(file_len, )
#         mp[key] = [1, file_len + key_len + 1]
#     else:
#         mp[key] = mp[key] + 1
#     s = ''
#     for kv in mp.items():
#         s = '%s:%d\n' % kv + s
#     b_s = bytearray(s)
#     write_file(0, b_s)
#
# def init():
#     ls = map(chr, read_file(0, 102400))
#     for li in ''.join(ls).split():
#         l2 = li.split(':')
#         if len(l2)<2:
#             continue
#         mp[l2[0]] = int(l2[1])
#
#
#
# put('www.baidu.com/1.html')
# put('www.baidu.com/1.html')
# put('www.baidu.com/2.html')
# put('www.baidu.com/3.html')
# put('www.baidu.com/2.html')
# put('www.baidu.com/2.html')
#
# print('1', get('www.baidu.com/1.html'))
#
# df.close()
