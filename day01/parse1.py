import urllib.parse

url = 'https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6&rsv_spt=1&rsv_iqid=0xa586957600002e01&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_dl=ib&rsv_sug3=9&rsv_sug1=6&rsv_sug7=100'

# url只能由特定字符组成，字母 数字 下划线
# 如果出现其他的，比如 ￥ 空格 中文 要对其进行编码

url1 = "http://www.baidu.com/index.html?name=狗蛋&pwd=12234"
url2 = 'http://www.baidu.com/index.html'
# 假如有参数 name age sex height
name = "gao"
age = 18
sex = 'nan'
height = '180'
data = {
    'name':name,
    "age":age,
    'sex':sex,
    'height':height,
    'weight':180
}

# 遍历字典
lt =[]
for k,v in data:
    lt.append(k + '=' + str(v))

query_string = '&'.join(lt)
url3 = url2 + '?' + query_string

# 上面的功能 是自己拼接的字符串
# 但是有一个封装好的函数
# 给一个字典，将字典拼接为query_string,并且已经编码
# urllib.parse.urlencode()

query_string1 = urllib.parse.urlencode(data)
# 此时已经拼接好了字符串
print(query_string1)

# quote()编码函数
ret = urllib.parse.quote(url1)
# unquote()解码函数
re = urllib.parse.unquote(ret)

print(re)
