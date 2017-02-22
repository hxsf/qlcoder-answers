# coding=utf-8

from pypinyin import pinyin, lazy_pinyin
import pypinyin

fh = open('./145630854135681.txt', 'r', encoding='utf-8')
l = 0
for rawline in fh.readlines():
    l += 1
    line = rawline.strip()
    arr = pinyin(line, heteronym=True, style=pypinyin.STYLE_NORMAL)
    a = [item[0] if len(item) == 1 else '(' + '/'.join(item) + ')' for item in arr]
    print(''.join(a))
    # if len(a) > 0:
    #     print(arr, '##########')
    # else:
    #     print(''.join([arr]))

fh.close()
