import urllib.parse
import urllib.request
# 获取posturl的地址
post_url = 'https://fanyi.baidu.com/v2transapi'
word = input("请输入您要查询的英文单词：")
# 构建post表单数据
form_data = {
    'from':'en',
    'to':'zh',
    'query': word,
    'transtype':'realtime',
    'simple_means_flag':'3',
    'sign':'814534.560887',
    'token':'62118056f35d8c231c3cd1abb2df788c',
    'domain':'common',
}
# 发送请求的过程

# headers模拟浏览器的过程 不接受压缩
# 注释掉Accept-Encoding
headers = {
    'Host': 'fanyi.baidu.com',
    'Connection': 'keep-alive',
    # 'Content-Length': '135',
    'Accept':'*/*',
    'Origin': 'https://fanyi.baidu.com',
    'X-Requested-With': 'XMLHttpRequest',
    'Sec-Fetch-Dest': 'empty',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36 Edg/80.0.361.69',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
    # 'Accept-Encoding: gzip, deflate, br
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cookie': 'BAIDUID=E6BE9A1E90CC12D7FFC1419673F44CF3:FG=1; BIDUPSID=86FE10546EA1B11959567CB359E9EA79; PSTM=1563269771; BDUSS=HNQfkdkODRTbG4tOHB4bVdUajhlYU9ZZVN-ZzE2UGo3eTJaZWRZV2l3VllOVXBkRVFBQUFBJCQAAAAAAAAAAAEAAAD-tX1SyMjH6bXE16jK9LWls7UAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFioIl1YqCJdT; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=1; H_PS_PSSID=30975_1443_31117_21104_30826_30907_30824_31085; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1585125144; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1585125144; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; __yjsv5_shitong=1.0_7_844c6b2ae1ef25ec8580f40c542798ed3a01_300_1585125145437_223.78.128.157_6b653272; hibext_instdsigdipv2=1; yjs_js_security_passport=1d0c1766dca6ac0e2844d3bb5636738f55c00c32_1585125146_js; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D',
}
# 处理post表单数据
# 此时是字节类型，应变为字符串类型
# form_data = urllib.parse.urlencode(form_data)
form_data = urllib.parse.urlencode(form_data).encode()

# 构建请求对象
request = urllib.request.Request(url=post_url, headers=headers)
# 发送请求
response = urllib.request.urlopen(request, data=form_data)

print(response.read().decode())