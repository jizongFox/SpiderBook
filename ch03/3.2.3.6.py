#coding:utf-8

# 重定向与历史

import requests
r = requests.get('http://github.com',allow_redirects=True)
print (r.url)
print (r.status_code)
print (r.history)
