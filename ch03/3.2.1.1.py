#coding:utf-8


# 最简单的形式
# import urllib
# response=urllib.request.urlopen('http://www.zhihu.com')
# html=response.read()
# print (html)




# 上面对http://www.zhihu.com的请求响应分为两步，一步是请求，一步是响应
#
# import urllib
# #请求
# request=urllib.Request('http://www.zhihu.com')
# #响应
# response = urllib.request.urlopen(request)
# html=response.read()
# print html
#



# POST请求

import urllib
# import urllib2
url = 'http://www.xxxxxx.com/login'
postdata = {'username' : 'qiye',
           'password' : 'qiye_pass'}
#info 需要被编码为urllib2能理解的格式，这里用到的是urllib
# data = urllib.urlencode(postdata)
data = urllib.parse.urlencode(postdata).encode("utf-8")
req = urllib.request.Request(url)
with urllib.request.urlopen(req,data=data) as f:
    response = f.read()
    print(response)


