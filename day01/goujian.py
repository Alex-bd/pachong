import urllib.request
import urllib.parse
import ssl

# 构建请求头部信息（反爬第一步）
# 伪装自己的UA
# 构建请求对象
url = 'http://www.baidu.com/'
# 自己要伪装的头部
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36 Edg/80.0.361.69',
}
# 构建请求对象
request = urllib.request.Request(url=url, headers=headers)
# 发送请求
response = urllib.request.urlopen(request)

print(response.read().decode())
