#coding:utf-8

# 响应与编码
#
# import requests
# r = requests.get('http://www.baidu.com')
# # print ('content-->'+r.content.decode())
# print ('text-->'+r.text)
# print ('encoding-->'+r.encoding)
# r.encoding='utf-8'
# print ('new text-->'+r.text)




# chardet:自动识别编码

# import requests,chardet
# r = requests.get('http://www.baidu.com')
# print (chardet.detect(r.content))
# r.encoding = chardet.detect(r.content)['encoding']
# print(r.encoding)
# print (r.text)


