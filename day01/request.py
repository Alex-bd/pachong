import urllib.request

url = "http://www.baidu.com"   # 要完整
# http://www.baidu.com/index.html?name=alex&password=123#lala

# 发送请求
response = urllib.request.urlopen(url=url)

# 把响应读成字符串类型
# print(response.read().encode())

# 读取字节类型
# response.read()
# response.geturl()
dict(response.getheaders())  # 字典 头类型
response.getcode()

#
# with open("baidu.html","w", encoding="utf8") as fp:
#     fp.write(response.read().decode())

with open("baidu1.html", "wb") as fp:
    fp.write(response.read())

