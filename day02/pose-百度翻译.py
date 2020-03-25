import urllib.request
import urllib.parse
# 获取posturl的地址
post_url = 'https://fanyi.baidu.com/sug'
word = input("请输入您要查询的英文单词：")
# 构建post表单数据
form_data = {
    'kw': word,
}
# 处理post表单数据
# 此时是字节类型，应变为字符串类型
# form_data = urllib.parse.urlencode(form_data)
form_data = urllib.parse.urlencode(form_data).encode()
# 发送请求的过程
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36 Edg/80.0.361.69',
}
# 构建请求对象
request = urllib.request.Request(url=post_url, headers=headers)
# 发送请求
response = urllib.request.urlopen(request, data=form_data)

print(response.read().decode())