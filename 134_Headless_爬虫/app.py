# coding=utf-8

import requests

url = 'https://mail.163.com/entry/cgi/ntesdoor?funcid=loginone&passtype=1&product=mail163'
s = requests.Session()
params = {
    'username': 'fbkits35395697@163.com',
    'password': 'zz4206',
}

a = s.post(url, params=params, allow_redirects=False)
print(a.headers['Location'])
# r = s.get('https://reg.163.com/account/accountInfo.jsp')
# r.text  # to find it
# print(r.text)
